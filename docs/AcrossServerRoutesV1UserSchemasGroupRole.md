# AcrossServerRoutesV1UserSchemasGroupRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**permissions** | [**List[Permission]**](Permission.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_user_schemas_group_role import AcrossServerRoutesV1UserSchemasGroupRole

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1UserSchemasGroupRole from a JSON string
across_server_routes_v1_user_schemas_group_role_instance = AcrossServerRoutesV1UserSchemasGroupRole.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1UserSchemasGroupRole.to_json())

# convert the object into a dict
across_server_routes_v1_user_schemas_group_role_dict = across_server_routes_v1_user_schemas_group_role_instance.to_dict()
# create an instance of AcrossServerRoutesV1UserSchemasGroupRole from a dict
across_server_routes_v1_user_schemas_group_role_from_dict = AcrossServerRoutesV1UserSchemasGroupRole.from_dict(across_server_routes_v1_user_schemas_group_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


