# GroupRoleCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**permission_ids** | **List[str]** |  | 

## Example

```python
from across/sdk.models.group_role_create import GroupRoleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRoleCreate from a JSON string
group_role_create_instance = GroupRoleCreate.from_json(json)
# print the JSON string representation of the object
print(GroupRoleCreate.to_json())

# convert the object into a dict
group_role_create_dict = group_role_create_instance.to_dict()
# create an instance of GroupRoleCreate from a dict
group_role_create_from_dict = GroupRoleCreate.from_dict(group_role_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


