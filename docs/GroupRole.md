# GroupRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**permissions** | [**List[Permission]**](Permission.md) |  | 
**id** | **str** |  | 
**group** | [**AcrossServerRoutesV1GroupRoleSchemasGroup**](AcrossServerRoutesV1GroupRoleSchemasGroup.md) |  | 
**users** | [**List[AcrossServerRoutesV1GroupRoleSchemasUser]**](AcrossServerRoutesV1GroupRoleSchemasUser.md) |  | 
**service_accounts** | [**List[ServiceAccount]**](ServiceAccount.md) |  | 

## Example

```python
from across.sdk.v1.models.group_role import GroupRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRole from a JSON string
group_role_instance = GroupRole.from_json(json)
# print the JSON string representation of the object
print(GroupRole.to_json())

# convert the object into a dict
group_role_dict = group_role_instance.to_dict()
# create an instance of GroupRole from a dict
group_role_from_dict = GroupRole.from_dict(group_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


