# GroupInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group** | [**GroupRead**](GroupRead.md) |  | 
**receiver** | [**UserInfo**](UserInfo.md) |  | 
**sender** | [**UserInfo**](UserInfo.md) |  | 

## Example

```python
from across.sdk.v1.models.group_invite import GroupInvite

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInvite from a JSON string
group_invite_instance = GroupInvite.from_json(json)
# print the JSON string representation of the object
print(GroupInvite.to_json())

# convert the object into a dict
group_invite_dict = group_invite_instance.to_dict()
# create an instance of GroupInvite from a dict
group_invite_from_dict = GroupInvite.from_dict(group_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


