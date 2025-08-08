# GroupInviteCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver_email** | **str** |  | 

## Example

```python
from across.sdk.v1.models.group_invite_create import GroupInviteCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInviteCreate from a JSON string
group_invite_create_instance = GroupInviteCreate.from_json(json)
# print the JSON string representation of the object
print(GroupInviteCreate.to_json())

# convert the object into a dict
group_invite_create_dict = group_invite_create_instance.to_dict()
# create an instance of GroupInviteCreate from a dict
group_invite_create_from_dict = GroupInviteCreate.from_dict(group_invite_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


