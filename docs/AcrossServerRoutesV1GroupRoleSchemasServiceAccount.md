# AcrossServerRoutesV1GroupRoleSchemasServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**user** | [**AcrossServerRoutesV1GroupRoleSchemasUser**](AcrossServerRoutesV1GroupRoleSchemasUser.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_group_role_schemas_service_account import AcrossServerRoutesV1GroupRoleSchemasServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1GroupRoleSchemasServiceAccount from a JSON string
across_server_routes_v1_group_role_schemas_service_account_instance = AcrossServerRoutesV1GroupRoleSchemasServiceAccount.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1GroupRoleSchemasServiceAccount.to_json())

# convert the object into a dict
across_server_routes_v1_group_role_schemas_service_account_dict = across_server_routes_v1_group_role_schemas_service_account_instance.to_dict()
# create an instance of AcrossServerRoutesV1GroupRoleSchemasServiceAccount from a dict
across_server_routes_v1_group_role_schemas_service_account_from_dict = AcrossServerRoutesV1GroupRoleSchemasServiceAccount.from_dict(across_server_routes_v1_group_role_schemas_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


