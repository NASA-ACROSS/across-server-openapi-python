# AcrossServerRoutesV1GroupInviteSchemasGroupInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group** | [**GroupRead**](GroupRead.md) |  | 
**receiver** | [**UserInfo**](UserInfo.md) |  | 
**sender** | [**UserInfo**](UserInfo.md) |  | 

## Example

```python
from across.sdk.v1.models.across_server_routes_v1_group_invite_schemas_group_invite import AcrossServerRoutesV1GroupInviteSchemasGroupInvite

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1GroupInviteSchemasGroupInvite from a JSON string
across_server_routes_v1_group_invite_schemas_group_invite_instance = AcrossServerRoutesV1GroupInviteSchemasGroupInvite.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1GroupInviteSchemasGroupInvite.to_json())

# convert the object into a dict
across_server_routes_v1_group_invite_schemas_group_invite_dict = across_server_routes_v1_group_invite_schemas_group_invite_instance.to_dict()
# create an instance of AcrossServerRoutesV1GroupInviteSchemasGroupInvite from a dict
across_server_routes_v1_group_invite_schemas_group_invite_from_dict = AcrossServerRoutesV1GroupInviteSchemasGroupInvite.from_dict(across_server_routes_v1_group_invite_schemas_group_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


