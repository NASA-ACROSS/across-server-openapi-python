# across.sdk.v1.InternalApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_account**](InternalApi.md#get_service_account) | **GET** /service-account/{service_account_id} | Get a system service account
[**service_account_rotate_key**](InternalApi.md#service_account_rotate_key) | **PATCH** /service-account/{service_account_id}/rotate_key | Rotate a service account key


# **get_service_account**
> SystemServiceAccount get_service_account(service_account_id)

Get a system service account

Rotate service account key and reset expiration based on expiration duration

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.system_service_account import SystemServiceAccount
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = across.sdk.v1.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.InternalApi(api_client)
    service_account_id = 'service_account_id_example' # str | 

    try:
        # Get a system service account
        api_response = api_instance.get_service_account(service_account_id)
        print("The response of InternalApi->get_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->get_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 

### Return type

[**SystemServiceAccount**](SystemServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rotated service account |  -  |
**404** | Service account not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_account_rotate_key**
> SystemServiceAccount service_account_rotate_key(service_account_id)

Rotate a service account key

Rotate service account key and reset expiration based on expiration duration

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.system_service_account import SystemServiceAccount
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = across.sdk.v1.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.InternalApi(api_client)
    service_account_id = 'service_account_id_example' # str | 

    try:
        # Rotate a service account key
        api_response = api_instance.service_account_rotate_key(service_account_id)
        print("The response of InternalApi->service_account_rotate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->service_account_rotate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **str**|  | 

### Return type

[**SystemServiceAccount**](SystemServiceAccount.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rotated service account |  -  |
**404** | Service account not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

