# across/sdk.AuthApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /auth/login | Login
[**refresh**](AuthApi.md#refresh) | **POST** /auth/refresh | Refresh Token
[**token**](AuthApi.md#token) | **POST** /auth/token | Token
[**verify**](AuthApi.md#verify) | **GET** /auth/verify | Verify


# **login**
> Dict[str, object] login(email)

Login

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across/sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = across/sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with across/sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across/sdk.AuthApi(api_client)
    email = 'email_example' # str | 

    try:
        # Login
        api_response = api_instance.login(email)
        print("The response of AuthApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh**
> AccessTokenResponse refresh()

Refresh Token

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.access_token_response import AccessTokenResponse
from across/sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across/sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = across/sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with across/sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across/sdk.AuthApi(api_client)

    try:
        # Refresh Token
        api_response = api_instance.refresh()
        print("The response of AuthApi->refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token**
> AccessTokenResponse token(grant_type)

Token

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.access_token_response import AccessTokenResponse
from across/sdk.models.grant_type import GrantType
from across/sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across/sdk.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = across/sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with across/sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across/sdk.AuthApi(api_client)
    grant_type = across/sdk.GrantType() # GrantType | 

    try:
        # Token
        api_response = api_instance.token(grant_type)
        print("The response of AuthApi->token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | [**GrantType**](GrantType.md)|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> AccessTokenResponse verify(token)

Verify

### Example


```python
import across/sdk
from across/sdk.models.access_token_response import AccessTokenResponse
from across/sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across/sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with across/sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across/sdk.AuthApi(api_client)
    token = 'token_example' # str | 

    try:
        # Verify
        api_response = api_instance.verify(token)
        print("The response of AuthApi->verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

