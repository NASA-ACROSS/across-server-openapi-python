# across/sdk.RoleApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_role**](RoleApi.md#get_role) | **GET** /role/{role_id} | Read a role
[**get_roles**](RoleApi.md#get_roles) | **GET** /role/ | Read roles


# **get_role**
> Role get_role(role_id)

Read a role

Read a role by role ID.

### Example


```python
import across/sdk
from across/sdk.models.role import Role
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
    api_instance = across/sdk.RoleApi(api_client)
    role_id = 'role_id_example' # str | 

    try:
        # Read a role
        api_response = api_instance.get_role(role_id)
        print("The response of RoleApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_role: %s\n" % e)
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
**200** | The requested role |  -  |
**404** | The role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> List[Role] get_roles()

Read roles

Read many roles.

### Example


```python
import across/sdk
from across/sdk.models.role import Role
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
    api_instance = across/sdk.RoleApi(api_client)

    try:
        # Read roles
        api_response = api_instance.get_roles()
        print("The response of RoleApi->get_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_roles: %s\n" % e)
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
**200** | A list of roles |  -  |
**404** | The role does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

