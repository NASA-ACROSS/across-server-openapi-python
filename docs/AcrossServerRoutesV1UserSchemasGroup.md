# AcrossServerRoutesV1UserSchemasGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 
**roles** | [**List[AcrossServerRoutesV1UserSchemasGroupRole]**](AcrossServerRoutesV1UserSchemasGroupRole.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_user_schemas_group import AcrossServerRoutesV1UserSchemasGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1UserSchemasGroup from a JSON string
across_server_routes_v1_user_schemas_group_instance = AcrossServerRoutesV1UserSchemasGroup.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1UserSchemasGroup.to_json())

# convert the object into a dict
across_server_routes_v1_user_schemas_group_dict = across_server_routes_v1_user_schemas_group_instance.to_dict()
# create an instance of AcrossServerRoutesV1UserSchemasGroup from a dict
across_server_routes_v1_user_schemas_group_from_dict = AcrossServerRoutesV1UserSchemasGroup.from_dict(across_server_routes_v1_user_schemas_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


