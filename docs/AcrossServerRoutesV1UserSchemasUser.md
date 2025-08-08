# AcrossServerRoutesV1UserSchemasUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**id** | **str** |  | 
**groups** | [**List[AcrossServerRoutesV1UserSchemasGroup]**](AcrossServerRoutesV1UserSchemasGroup.md) |  | 
**roles** | [**List[RoleBase]**](RoleBase.md) |  | 
**group_roles** | [**List[AcrossServerRoutesV1UserSchemasGroupRole]**](AcrossServerRoutesV1UserSchemasGroupRole.md) |  | 
**received_invites** | [**List[AcrossServerRoutesV1UserSchemasGroupInvite]**](AcrossServerRoutesV1UserSchemasGroupInvite.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_user_schemas_user import AcrossServerRoutesV1UserSchemasUser

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1UserSchemasUser from a JSON string
across_server_routes_v1_user_schemas_user_instance = AcrossServerRoutesV1UserSchemasUser.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1UserSchemasUser.to_json())

# convert the object into a dict
across_server_routes_v1_user_schemas_user_dict = across_server_routes_v1_user_schemas_user_instance.to_dict()
# create an instance of AcrossServerRoutesV1UserSchemasUser from a dict
across_server_routes_v1_user_schemas_user_from_dict = AcrossServerRoutesV1UserSchemasUser.from_dict(across_server_routes_v1_user_schemas_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


