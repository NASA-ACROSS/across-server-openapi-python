# across.sdk.v1.GroupInviteApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_invite**](GroupInviteApi.md#delete_invite) | **DELETE** /group/{group_id}/invite/{invite_id} | Delete a group invite
[**get_invite**](GroupInviteApi.md#get_invite) | **GET** /group/{group_id}/invite/{invite_id} | Read a group invite
[**get_invites**](GroupInviteApi.md#get_invites) | **GET** /group/{group_id}/invite | Read group invites
[**send_invite**](GroupInviteApi.md#send_invite) | **POST** /group/{group_id}/invite | Create and send a group invite


# **delete_invite**
> delete_invite(invite_id, group_id)

Delete a group invite

Delete a group invite by ID

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
    api_instance = across.sdk.v1.GroupInviteApi(api_client)
    invite_id = 'invite_id_example' # str | 
    group_id = 'group_id_example' # str | 

    try:
        # Delete a group invite
        api_instance.delete_invite(invite_id, group_id)
    except Exception as e:
        print("Exception when calling GroupInviteApi->delete_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
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
**404** | The group or invite does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite**
> AcrossServerRoutesV1GroupInviteSchemasGroupInvite get_invite(group_id, invite_id)

Read a group invite

Read a single group invite by ID

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_group_invite_schemas_group_invite import AcrossServerRoutesV1GroupInviteSchemasGroupInvite
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
    api_instance = across.sdk.v1.GroupInviteApi(api_client)
    group_id = 'group_id_example' # str | 
    invite_id = 'invite_id_example' # str | 

    try:
        # Read a group invite
        api_response = api_instance.get_invite(group_id, invite_id)
        print("The response of GroupInviteApi->get_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupInviteApi->get_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **invite_id** | **str**|  | 

### Return type

[**AcrossServerRoutesV1GroupInviteSchemasGroupInvite**](AcrossServerRoutesV1GroupInviteSchemasGroupInvite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested group invite |  -  |
**404** | The group or invite does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invites**
> List[AcrossServerRoutesV1GroupInviteSchemasGroupInvite] get_invites(group_id)

Read group invites

Read all group invites for a group

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_group_invite_schemas_group_invite import AcrossServerRoutesV1GroupInviteSchemasGroupInvite
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
    api_instance = across.sdk.v1.GroupInviteApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Read group invites
        api_response = api_instance.get_invites(group_id)
        print("The response of GroupInviteApi->get_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupInviteApi->get_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**List[AcrossServerRoutesV1GroupInviteSchemasGroupInvite]**](AcrossServerRoutesV1GroupInviteSchemasGroupInvite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of group invites |  -  |
**404** | The group or invite does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_invite**
> AcrossServerRoutesV1GroupInviteSchemasGroupInvite send_invite(group_id, group_invite_create)

Create and send a group invite

Create and send a group invite to a user

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.across_server_routes_v1_group_invite_schemas_group_invite import AcrossServerRoutesV1GroupInviteSchemasGroupInvite
from across.sdk.v1.models.group_invite_create import GroupInviteCreate
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
    api_instance = across.sdk.v1.GroupInviteApi(api_client)
    group_id = 'group_id_example' # str | 
    group_invite_create = across.sdk.v1.GroupInviteCreate() # GroupInviteCreate | 

    try:
        # Create and send a group invite
        api_response = api_instance.send_invite(group_id, group_invite_create)
        print("The response of GroupInviteApi->send_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupInviteApi->send_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **group_invite_create** | [**GroupInviteCreate**](GroupInviteCreate.md)|  | 

### Return type

[**AcrossServerRoutesV1GroupInviteSchemasGroupInvite**](AcrossServerRoutesV1GroupInviteSchemasGroupInvite.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created group invite |  -  |
**404** | The group or invite does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

