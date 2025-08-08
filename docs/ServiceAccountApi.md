# across/sdk.ServiceAccountApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_to_service_account**](ServiceAccountApi.md#assign_to_service_account) | **POST** /user/{user_id}/service-account/{service_account_id}/group-role/{group_role_id} | Assign group role
[**create_service_account**](ServiceAccountApi.md#create_service_account) | **POST** /user/{user_id}/service_account/ | Create a service account
[**delete_service_account**](ServiceAccountApi.md#delete_service_account) | **DELETE** /user/{user_id}/service_account/{service_account_id} | Delete a service_account
[**get_service_account**](ServiceAccountApi.md#get_service_account) | **GET** /user/{user_id}/service_account/{service_account_id} | Read a service account
[**get_service_accounts**](ServiceAccountApi.md#get_service_accounts) | **GET** /user/{user_id}/service_account/ | Read service accounts
[**remove_from_service_account**](ServiceAccountApi.md#remove_from_service_account) | **DELETE** /user/{user_id}/service-account/{service_account_id}/group-role/{group_role_id} | Remove group role
[**rotate_key**](ServiceAccountApi.md#rotate_key) | **PATCH** /user/{user_id}/service_account/{service_account_id}/rotate_key | Rotate a service account key
[**update_service_account**](ServiceAccountApi.md#update_service_account) | **PATCH** /user/{user_id}/service_account/{service_account_id} | Update a service account


# **assign_to_service_account**
> AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount assign_to_service_account(service_account_id, group_role_id, user_id)

Assign group role

Assign a group role to a service account.

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.across_server_routes_v1_user_service_account_schemas_service_account import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount
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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    service_account_id = 'service_account_id_example' # str | 
    group_role_id = 'group_role_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Assign group role
        api_response = api_instance.assign_to_service_account(service_account_id, group_role_id, user_id)
        print("The response of ServiceAccountApi->assign_to_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->assign_to_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 
 **group_role_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount**](AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group Role has been assigned to service account |  -  |
**404** | The service account, user, or group role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account**
> ServiceAccountSecret create_service_account(user_id, service_account_create)

Create a service account

Create a new service account for an ACROSS user.

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.service_account_create import ServiceAccountCreate
from across/sdk.models.service_account_secret import ServiceAccountSecret
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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    user_id = 'user_id_example' # str | 
    service_account_create = across/sdk.ServiceAccountCreate() # ServiceAccountCreate | 

    try:
        # Create a service account
        api_response = api_instance.create_service_account(user_id, service_account_create)
        print("The response of ServiceAccountApi->create_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->create_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **service_account_create** | [**ServiceAccountCreate**](ServiceAccountCreate.md)|  | 

### Return type

[**ServiceAccountSecret**](ServiceAccountSecret.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created service account |  -  |
**404** | The service account does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_account**
> delete_service_account(service_account_id, user_id)

Delete a service_account

Expire a service account, the account will still exist for log/record purposes, but it will not be usable anymore.

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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    service_account_id = 'service_account_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Delete a service_account
        api_instance.delete_service_account(service_account_id, user_id)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->delete_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**404** | The service account does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_account**
> AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount get_service_account(service_account_id, user_id)

Read a service account

Read a service account by an ID.

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.across_server_routes_v1_user_service_account_schemas_service_account import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount
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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    service_account_id = 'service_account_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Read a service account
        api_response = api_instance.get_service_account(service_account_id, user_id)
        print("The response of ServiceAccountApi->get_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->get_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount**](AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a service account |  -  |
**404** | The service account does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_accounts**
> List[AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount] get_service_accounts(user_id)

Read service accounts

Read many service accounts

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.across_server_routes_v1_user_service_account_schemas_service_account import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount
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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Read service accounts
        api_response = api_instance.get_service_accounts(user_id)
        print("The response of ServiceAccountApi->get_service_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->get_service_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount]**](AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | The service account does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_service_account**
> AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount remove_from_service_account(service_account_id, group_role_id, user_id)

Remove group role

Remove a group role from a service account.

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.across_server_routes_v1_user_service_account_schemas_service_account import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount
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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    service_account_id = 'service_account_id_example' # str | 
    group_role_id = 'group_role_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove group role
        api_response = api_instance.remove_from_service_account(service_account_id, group_role_id, user_id)
        print("The response of ServiceAccountApi->remove_from_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->remove_from_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 
 **group_role_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount**](AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group Role has been removed from the service account |  -  |
**404** | The service account, user, or group role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_key**
> AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount rotate_key(service_account_id, user_id)

Rotate a service account key

Rotate service account key and reset expiration based on expiration_duration

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.across_server_routes_v1_user_service_account_schemas_service_account import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount
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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    service_account_id = 'service_account_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Rotate a service account key
        api_response = api_instance.rotate_key(service_account_id, user_id)
        print("The response of ServiceAccountApi->rotate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->rotate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount**](AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rotated service account |  -  |
**404** | The service account does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account**
> AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount update_service_account(service_account_id, user_id, service_account_update)

Update a service account

Update a service account's information.

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.across_server_routes_v1_user_service_account_schemas_service_account import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount
from across/sdk.models.service_account_update import ServiceAccountUpdate
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
    api_instance = across/sdk.ServiceAccountApi(api_client)
    service_account_id = 'service_account_id_example' # str | 
    user_id = 'user_id_example' # str | 
    service_account_update = across/sdk.ServiceAccountUpdate() # ServiceAccountUpdate | 

    try:
        # Update a service account
        api_response = api_instance.update_service_account(service_account_id, user_id, service_account_update)
        print("The response of ServiceAccountApi->update_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountApi->update_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 
 **user_id** | **str**|  | 
 **service_account_update** | [**ServiceAccountUpdate**](ServiceAccountUpdate.md)|  | 

### Return type

[**AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount**](AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated service account |  -  |
**404** | The service account does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

