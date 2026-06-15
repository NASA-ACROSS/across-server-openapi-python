# GroupBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 

## Example

```python
from across.sdk.v1.models.group_base import GroupBase

# TODO update the JSON string below
json = "{}"
# create an instance of GroupBase from a JSON string
group_base_instance = GroupBase.from_json(json)
# print the JSON string representation of the object
print(GroupBase.to_json())

# convert the object into a dict
group_base_dict = group_base_instance.to_dict()
# create an instance of GroupBase from a dict
group_base_from_dict = GroupBase.from_dict(group_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


