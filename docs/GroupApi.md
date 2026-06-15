# across.sdk.v1.GroupApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group**](GroupApi.md#get_group) | **GET** /group/{group_id} | Read a group
[**get_many_group_get**](GroupApi.md#get_many_group_get) | **GET** /group/ | Read groups
[**remove_user**](GroupApi.md#remove_user) | **DELETE** /group/{group_id}/user/{user_id} | Remove a user from a group


# **get_group**
> AcrossServerRoutesV1GroupSchemasGroup get_group(group_id)

Read a group

Read a group by role ID.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_group_schemas_group import AcrossServerRoutesV1GroupSchemasGroup
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/v1"
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
    api_instance = across.sdk.v1.GroupApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Read a group
        api_response = api_instance.get_group(group_id)
        print("The response of GroupApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1GroupSchemasGroup**](AcrossServerRoutesV1GroupSchemasGroup.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested group |  -  |
**404** | The group does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_many_group_get**
> List[AcrossServerRoutesV1GroupSchemasGroup] get_many_group_get()

Read groups

Read many groups

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_group_schemas_group import AcrossServerRoutesV1GroupSchemasGroup
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.GroupApi(api_client)

    try:
        # Read groups
        api_response = api_instance.get_many_group_get()
        print("The response of GroupApi->get_many_group_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_many_group_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AcrossServerRoutesV1GroupSchemasGroup]**](AcrossServerRoutesV1GroupSchemasGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | The group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user**
> remove_user(user_id, group_id)

Remove a user from a group

Remove a user from a group by ID

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/v1"
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
    api_instance = across.sdk.v1.GroupApi(api_client)
    user_id = 'user_id_example' # str | 
    group_id = 'group_id_example' # str | 

    try:
        # Remove a user from a group
        api_instance.remove_user(user_id, group_id)
    except Exception as e:
        print("Exception when calling GroupApi->remove_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **group_id** | **str**|  | 

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
**404** | The group does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

