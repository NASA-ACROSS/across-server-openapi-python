# GroupRoleRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**permissions** | [**List[Permission]**](Permission.md) |  | 
**id** | **str** |  | 

## Example

```python
from across/sdk.models.group_role_read import GroupRoleRead

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRoleRead from a JSON string
group_role_read_instance = GroupRoleRead.from_json(json)
# print the JSON string representation of the object
print(GroupRoleRead.to_json())

# convert the object into a dict
group_role_read_dict = group_role_read_instance.to_dict()
# create an instance of GroupRoleRead from a dict
group_role_read_from_dict = GroupRoleRead.from_dict(group_role_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


