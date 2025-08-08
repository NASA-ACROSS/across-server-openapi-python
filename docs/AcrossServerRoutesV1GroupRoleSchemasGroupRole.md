# AcrossServerRoutesV1GroupRoleSchemasGroupRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**permissions** | [**List[Permission]**](Permission.md) |  | 
**id** | **str** |  | 
**users** | [**List[AcrossServerRoutesV1GroupRoleSchemasUser]**](AcrossServerRoutesV1GroupRoleSchemasUser.md) |  | 
**service_accounts** | [**List[AcrossServerRoutesV1GroupRoleSchemasServiceAccount]**](AcrossServerRoutesV1GroupRoleSchemasServiceAccount.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_group_role_schemas_group_role import AcrossServerRoutesV1GroupRoleSchemasGroupRole

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1GroupRoleSchemasGroupRole from a JSON string
across_server_routes_v1_group_role_schemas_group_role_instance = AcrossServerRoutesV1GroupRoleSchemasGroupRole.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1GroupRoleSchemasGroupRole.to_json())

# convert the object into a dict
across_server_routes_v1_group_role_schemas_group_role_dict = across_server_routes_v1_group_role_schemas_group_role_instance.to_dict()
# create an instance of AcrossServerRoutesV1GroupRoleSchemasGroupRole from a dict
across_server_routes_v1_group_role_schemas_group_role_from_dict = AcrossServerRoutesV1GroupRoleSchemasGroupRole.from_dict(across_server_routes_v1_group_role_schemas_group_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


