# across/sdk.GroupRoleApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_to_user**](GroupRoleApi.md#assign_to_user) | **PUT** /group/{group_id}/user/{user_id}/role/{group_role_id} | Assign a group role to a user
[**create_group_role**](GroupRoleApi.md#create_group_role) | **POST** /group/{group_id}/role | Create a group role
[**delete_group_role**](GroupRoleApi.md#delete_group_role) | **DELETE** /group/{group_id}/role/{group_role_id} | Delete a group role
[**get_group_role**](GroupRoleApi.md#get_group_role) | **GET** /group/{group_id}/role/{group_role_id} | Read a group role
[**get_group_roles**](GroupRoleApi.md#get_group_roles) | **GET** /group/{group_id}/role | Read group roles
[**remove_from_user**](GroupRoleApi.md#remove_from_user) | **DELETE** /group/{group_id}/user/{user_id}/role/{group_role_id} | Remove a group role from a user
[**update_group_role**](GroupRoleApi.md#update_group_role) | **PUT** /group/{group_id}/role/{group_role_id} | Update a group role


# **assign_to_user**
> assign_to_user(group_role_id, group_id, user_id)

Assign a group role to a user

Assign a group role by id to a user id within that group.

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
    api_instance = across/sdk.GroupRoleApi(api_client)
    group_role_id = 'group_role_id_example' # str | 
    group_id = 'group_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Assign a group role to a user
        api_instance.assign_to_user(group_role_id, group_id, user_id)
    except Exception as e:
        print("Exception when calling GroupRoleApi->assign_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_role_id** | **str**|  | 
 **group_id** | **str**|  | 
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
**204** | Group role successfully assigned to user |  -  |
**404** | The group or role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_role**
> GroupRoleRead create_group_role(group_id, group_role_create)

Create a group role

Create a group role with a set of permissions in a group that you control

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.group_role_create import GroupRoleCreate
from across/sdk.models.group_role_read import GroupRoleRead
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
    api_instance = across/sdk.GroupRoleApi(api_client)
    group_id = 'group_id_example' # str | 
    group_role_create = across/sdk.GroupRoleCreate() # GroupRoleCreate | 

    try:
        # Create a group role
        api_response = api_instance.create_group_role(group_id, group_role_create)
        print("The response of GroupRoleApi->create_group_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRoleApi->create_group_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **group_role_create** | [**GroupRoleCreate**](GroupRoleCreate.md)|  | 

### Return type

[**GroupRoleRead**](GroupRoleRead.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created group role |  -  |
**404** | The group or role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_role**
> delete_group_role(group_id, group_role_id)

Delete a group role

Delete a group role by role ID.

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
    api_instance = across/sdk.GroupRoleApi(api_client)
    group_id = 'group_id_example' # str | 
    group_role_id = 'group_role_id_example' # str | 

    try:
        # Delete a group role
        api_instance.delete_group_role(group_id, group_role_id)
    except Exception as e:
        print("Exception when calling GroupRoleApi->delete_group_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **group_role_id** | **str**|  | 

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
**204** | Group role successfully deleted |  -  |
**404** | The group or role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_role**
> AcrossServerRoutesV1GroupRoleSchemasGroupRole get_group_role(group_id, group_role_id)

Read a group role

Read a group role by role ID.

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.across_server_routes_v1_group_role_schemas_group_role import AcrossServerRoutesV1GroupRoleSchemasGroupRole
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
    api_instance = across/sdk.GroupRoleApi(api_client)
    group_id = 'group_id_example' # str | 
    group_role_id = 'group_role_id_example' # str | 

    try:
        # Read a group role
        api_response = api_instance.get_group_role(group_id, group_role_id)
        print("The response of GroupRoleApi->get_group_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRoleApi->get_group_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **group_role_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1GroupRoleSchemasGroupRole**](AcrossServerRoutesV1GroupRoleSchemasGroupRole.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested group role |  -  |
**404** | The group or role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_roles**
> List[GroupRoleRead] get_group_roles(group_id)

Read group roles

Read many group roles.

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.group_role_read import GroupRoleRead
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
    api_instance = across/sdk.GroupRoleApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Read group roles
        api_response = api_instance.get_group_roles(group_id)
        print("The response of GroupRoleApi->get_group_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRoleApi->get_group_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**List[GroupRoleRead]**](GroupRoleRead.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of group roles |  -  |
**404** | The group or role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_user**
> remove_from_user(group_role_id, group_id, user_id)

Remove a group role from a user

Remove a group role by id from a user id within that group.

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
    api_instance = across/sdk.GroupRoleApi(api_client)
    group_role_id = 'group_role_id_example' # str | 
    group_id = 'group_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove a group role from a user
        api_instance.remove_from_user(group_role_id, group_id, user_id)
    except Exception as e:
        print("Exception when calling GroupRoleApi->remove_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_role_id** | **str**|  | 
 **group_id** | **str**|  | 
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
**204** | Group role successfully removed from user |  -  |
**404** | The group or role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_role**
> GroupRoleCreate update_group_role(group_role_id, group_id, group_role_create)

Update a group role

Update a group role and its permissions in a group that you control

### Example

* Bearer Authentication (Authorization):

```python
import across/sdk
from across/sdk.models.group_role_create import GroupRoleCreate
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
    api_instance = across/sdk.GroupRoleApi(api_client)
    group_role_id = 'group_role_id_example' # str | 
    group_id = 'group_id_example' # str | 
    group_role_create = across/sdk.GroupRoleCreate() # GroupRoleCreate | 

    try:
        # Update a group role
        api_response = api_instance.update_group_role(group_role_id, group_id, group_role_create)
        print("The response of GroupRoleApi->update_group_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRoleApi->update_group_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_role_id** | **str**|  | 
 **group_id** | **str**|  | 
 **group_role_create** | [**GroupRoleCreate**](GroupRoleCreate.md)|  | 

### Return type

[**GroupRoleCreate**](GroupRoleCreate.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated group role |  -  |
**404** | The group or role does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

