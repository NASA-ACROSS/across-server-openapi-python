# across.sdk.v1.PermissionApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissions**](PermissionApi.md#get_permissions) | **GET** /permission/ | Read permissions


# **get_permissions**
> List[Permission] get_permissions()

Read permissions

Read many permissions.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.permission import Permission
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.PermissionApi(api_client)

    try:
        # Read permissions
        api_response = api_instance.get_permissions()
        print("The response of PermissionApi->get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->get_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Permission]**](Permission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of permissions |  -  |
**404** | The permission does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

