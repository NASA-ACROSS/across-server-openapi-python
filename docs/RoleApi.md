# across.sdk.v1.RoleApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_many_role_get**](RoleApi.md#get_many_role_get) | **GET** /role/ | Read roles
[**get_role_role_id_get**](RoleApi.md#get_role_role_id_get) | **GET** /role/{role_id} | Read a role


# **get_many_role_get**
> List[Role] get_many_role_get()

Read roles

Read many roles

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.role import Role
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
    api_instance = across.sdk.v1.RoleApi(api_client)

    try:
        # Read roles
        api_response = api_instance.get_many_role_get()
        print("The response of RoleApi->get_many_role_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_many_role_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | The role does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_role_id_get**
> Role get_role_role_id_get(role_id)

Read a role

Read a role by role ID.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.role import Role
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
    api_instance = across.sdk.v1.RoleApi(api_client)
    role_id = 'role_id_example' # str | 

    try:
        # Read a role
        api_response = api_instance.get_role_role_id_get(role_id)
        print("The response of RoleApi->get_role_role_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_role_role_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | The role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

