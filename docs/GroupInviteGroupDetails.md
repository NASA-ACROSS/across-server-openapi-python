# GroupInviteGroupDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 
**created_on** | **datetime** |  | 

## Example

```python
from across.sdk.v1.models.group_invite_group_details import GroupInviteGroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInviteGroupDetails from a JSON string
group_invite_group_details_instance = GroupInviteGroupDetails.from_json(json)
# print the JSON string representation of the object
print(GroupInviteGroupDetails.to_json())

# convert the object into a dict
group_invite_group_details_dict = group_invite_group_details_instance.to_dict()
# create an instance of GroupInviteGroupDetails from a dict
group_invite_group_details_from_dict = GroupInviteGroupDetails.from_dict(group_invite_group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


