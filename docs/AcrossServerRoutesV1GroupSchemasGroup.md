# AcrossServerRoutesV1GroupSchemasGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**short_name** | **str** |  | 
**id** | **str** |  | 
**users** | [**List[AcrossServerRoutesV1GroupSchemasUser]**](AcrossServerRoutesV1GroupSchemasUser.md) |  | 
**roles** | [**List[AcrossServerRoutesV1GroupRoleSchemasGroupRole]**](AcrossServerRoutesV1GroupRoleSchemasGroupRole.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_group_schemas_group import AcrossServerRoutesV1GroupSchemasGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1GroupSchemasGroup from a JSON string
across_server_routes_v1_group_schemas_group_instance = AcrossServerRoutesV1GroupSchemasGroup.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1GroupSchemasGroup.to_json())

# convert the object into a dict
across_server_routes_v1_group_schemas_group_dict = across_server_routes_v1_group_schemas_group_instance.to_dict()
# create an instance of AcrossServerRoutesV1GroupSchemasGroup from a dict
across_server_routes_v1_group_schemas_group_from_dict = AcrossServerRoutesV1GroupSchemasGroup.from_dict(across_server_routes_v1_group_schemas_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


