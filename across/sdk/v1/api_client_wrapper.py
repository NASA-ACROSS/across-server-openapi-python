import threading
import logging
import os
from datetime import datetime, timedelta, timezone

import across.sdk.v1 as sdk
from across.sdk.v1 import rest

from .abstract_credential_storage import CredentialStorage as ICredStorage

logger = logging.getLogger("ACROSS_API_CLIENT_WRAPPER")


class ApiClientWrapper(sdk.ApiClient):
    _client = None
    _cred_store: ICredStorage | None = None
    _exp: datetime | None = None

    def __init__(
        self,
        configuration: sdk.Configuration,
        creds_store: ICredStorage | None = None,
        *args,
        **kwargs,
    ):
        super().__init__(configuration, *args, **kwargs)

        self._cred_store = creds_store
        self._lock = threading.Lock()

    @classmethod
    def get_client(
        cls,
        configuration: sdk.Configuration,
        creds: ICredStorage | None = None,
    ):
        """
        Retrieve (or lazily initialize) a singleton API client.

        This method ensures that only one client instance is created per class.
        If no client exists, it will initialize one using the provided
        `configuration` and optional `creds` (credentials storage).

        Credentials resolution order:
            1. Use `configuration.username` and `configuration.password` if they are provided.
            2. If not provided and `creds` is passed in, fetch credentials from it.
            3. Otherwise, fall back to environment variables:
                - `ACROSS_SERVER_ID`
                - `ACROSS_SERVER_SECRET`

        ⚠️ Note:
            This is a **singleton** accessor. Once the client is created,
            subsequent calls to `get_client` will reuse the same instance,
            regardless of whether a different `configuration` or `creds` is passed.
            To reset or replace the client, `_client` must be cleared explicitly.

        Args:
            configuration (sdk.Configuration): The base configuration object
                for the SDK client.
            creds (ICredStorage | None, optional): Optional credential storage
                provider for resolving `id` and `secret`. Defaults to None.

        Returns:
            ApiClientWrapper: A singleton instance of the API client wrapper.

        Example:
                from my_sdk import Configuration, ApiClientWrapper, CredentialStorage, SomeApi
                from my_creds import CredStorage

                config = Configuration(host="https://api.example.com")
                creds: CredentialStorage = CredStorage()

                client = ApiClientWrapper.get_client(configuration=config, creds=creds)

                response = SomeApi(client).some_method()
                print(response)
        """
        if cls._client is None:
            if not configuration.username and not configuration.password:
                # Use the creds store if it is passed in, otherwise use env vars
                if creds:
                    configuration.username = creds.id(force=True)
                    configuration.password = creds.secret(force=True)
                else:
                    configuration.username = os.getenv("ACROSS_SERVER_ID")
                    configuration.password = os.getenv("ACROSS_SERVER_SECRET")

            cls._client = ApiClientWrapper(
                configuration=configuration,
                creds_store=creds,
            )

        return cls._client

    def call_api(self, *args, **kwargs) -> rest.RESTResponse:
        self.refresh()

        try:
            return super().call_api(*args, **kwargs)
        except sdk.ApiException as err:
            if err.status == 401:
                logger.debug("Access token is unauthenticated or it has expired.")

                refreshed = self.refresh_token()

                # Attempt the call again
                if refreshed:
                    return super().call_api(*args, **kwargs)
                else:
                    raise err
            else:
                raise err

    def refresh(self) -> None:
        if not self.configuration.access_token:
            self.refresh_token()

        if self._cred_store:
            with self._lock:
                if self._should_rotate(self._cred_store):
                    res = sdk.InternalApi(super()).service_account_rotate_key(
                        service_account_id=self._cred_store.id()
                    )

                    self._set_exp(res.expiration)
                    self._cred_store.update_key(res.secret_key)
                    self.configuration.password = res.secret_key

    def refresh_token(self) -> bool:
        if self.configuration.username and self.configuration.password:
            logger.debug("Refreshing access token...")

            # Instantiate with super to avoid infinite recursion through call_api
            token = sdk.AuthApi(super()).token(
                grant_type=sdk.GrantType.CLIENT_CREDENTIALS
            )

            self.configuration.access_token = token.access_token

            logger.debug("Successfully refreshed token!")

            return True

        return False

    def _should_rotate(self, cred_store: ICredStorage) -> bool:
        now = datetime.now(timezone.utc)

        expiration = self._expiration(cred_store)

        if expiration:
            will_expire_soon = expiration <= now + timedelta(
                days=cred_store.days_before_exp
            )

            return will_expire_soon

        return True

    def _expiration(self, cred_store: ICredStorage) -> datetime | None:
        if self._exp:
            return self._exp

        res = sdk.InternalApi(super()).get_service_account(
            service_account_id=cred_store.id()
        )

        self._set_exp(res.expiration)

        return self._exp

    def _set_exp(self, date: datetime):
        if date.tzinfo is None:
            self._exp = date.replace(tzinfo=timezone.utc)
        else:
            self._exp = date
