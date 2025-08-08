# AcrossServerRoutesV1GroupSchemasUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**group_roles** | [**List[GroupRoleRead]**](GroupRoleRead.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_group_schemas_user import AcrossServerRoutesV1GroupSchemasUser

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1GroupSchemasUser from a JSON string
across_server_routes_v1_group_schemas_user_instance = AcrossServerRoutesV1GroupSchemasUser.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1GroupSchemasUser.to_json())

# convert the object into a dict
across_server_routes_v1_group_schemas_user_dict = across_server_routes_v1_group_schemas_user_instance.to_dict()
# create an instance of AcrossServerRoutesV1GroupSchemasUser from a dict
across_server_routes_v1_group_schemas_user_from_dict = AcrossServerRoutesV1GroupSchemasUser.from_dict(across_server_routes_v1_group_schemas_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


