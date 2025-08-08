# across.sdk.v1.UserApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invite**](UserApi.md#accept_invite) | **PATCH** /user/{user_id}/invite/{invite_id} | Accept a group invitation
[**create_user**](UserApi.md#create_user) | **POST** /user/ | Create a user
[**decline_invite**](UserApi.md#decline_invite) | **DELETE** /user/{user_id}/invite/{invite_id} | Decline a group invitation
[**delete_user**](UserApi.md#delete_user) | **DELETE** /user/{user_id} | Delete a user
[**get_group_invites**](UserApi.md#get_group_invites) | **GET** /user/{user_id}/invite | Read a user&#39;s group invites
[**get_user**](UserApi.md#get_user) | **GET** /user/{user_id} | Read a user
[**get_users**](UserApi.md#get_users) | **GET** /user/ | Get Many
[**leave_group**](UserApi.md#leave_group) | **DELETE** /user/{user_id}/group/{group_id} | Leave a group
[**update_user**](UserApi.md#update_user) | **PATCH** /user/{user_id} | Update a user


# **accept_invite**
> accept_invite(user_id, invite_id)

Accept a group invitation

Accept a group invitation to join a user group.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    invite_id = 'invite_id_example' # str | 

    try:
        # Accept a group invitation
        api_instance.accept_invite(user_id, invite_id)
    except Exception as e:
        print("Exception when calling UserApi->accept_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invite_id** | **str**|  | 

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
**204** | The group invitation has been accepted |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> object create_user(user_create)

Create a user

Create a new user for ACROSS.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.user_create import UserCreate
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_create = across.sdk.v1.UserCreate() # UserCreate | 

    try:
        # Create a user
        api_response = api_instance.create_user(user_create)
        print("The response of UserApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decline_invite**
> decline_invite(user_id, invite_id)

Decline a group invitation

Decline a group invitation to refuse joining a user group.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    invite_id = 'invite_id_example' # str | 

    try:
        # Decline a group invitation
        api_instance.decline_invite(user_id, invite_id)
    except Exception as e:
        print("Exception when calling UserApi->decline_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **invite_id** | **str**|  | 

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
**204** | The group invitation has been declined |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> AcrossServerRoutesV1UserSchemasUser delete_user(user_id)

Delete a user

Permanently delete a user from the ACROSS system. This will also delete all associated relations for the user.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_user_schemas_user import AcrossServerRoutesV1UserSchemasUser
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Delete a user
        api_response = api_instance.delete_user(user_id)
        print("The response of UserApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1UserSchemasUser**](AcrossServerRoutesV1UserSchemasUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upon successful deletion, the user is returned |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_invites**
> List[AcrossServerRoutesV1UserSchemasGroupInvite] get_group_invites(user_id)

Read a user's group invites

Read a user's group invites by a user ID.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_user_schemas_group_invite import AcrossServerRoutesV1UserSchemasGroupInvite
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Read a user's group invites
        api_response = api_instance.get_group_invites(user_id)
        print("The response of UserApi->get_group_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_group_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[AcrossServerRoutesV1UserSchemasGroupInvite]**](AcrossServerRoutesV1UserSchemasGroupInvite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of group invites for a user id |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> AcrossServerRoutesV1UserSchemasUser get_user(user_id)

Read a user

Read a user by a user ID.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_user_schemas_user import AcrossServerRoutesV1UserSchemasUser
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Read a user
        api_response = api_instance.get_user(user_id)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1UserSchemasUser**](AcrossServerRoutesV1UserSchemasUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a user |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[AcrossServerRoutesV1UserSchemasUser] get_users()

Get Many

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_user_schemas_user import AcrossServerRoutesV1UserSchemasUser
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
    api_instance = across.sdk.v1.UserApi(api_client)

    try:
        # Get Many
        api_response = api_instance.get_users()
        print("The response of UserApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AcrossServerRoutesV1UserSchemasUser]**](AcrossServerRoutesV1UserSchemasUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | The user does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_group**
> leave_group(user_id, group_id)

Leave a group

Leave a group by id

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    group_id = 'group_id_example' # str | 

    try:
        # Leave a group
        api_instance.leave_group(user_id, group_id)
    except Exception as e:
        print("Exception when calling UserApi->leave_group: %s\n" % e)
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
**204** | Successfully left the group |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> AcrossServerRoutesV1UserSchemasUser update_user(user_id, user_update)

Update a user

Update a user's information for the allowed properties.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_user_schemas_user import AcrossServerRoutesV1UserSchemasUser
from across.sdk.v1.models.user_update import UserUpdate
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
    api_instance = across.sdk.v1.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    user_update = across.sdk.v1.UserUpdate() # UserUpdate | 

    try:
        # Update a user
        api_response = api_instance.update_user(user_id, user_update)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**AcrossServerRoutesV1UserSchemasUser**](AcrossServerRoutesV1UserSchemasUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated user |  -  |
**404** | The user does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

