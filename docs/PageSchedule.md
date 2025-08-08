# PageSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_number** | **int** |  | 
**page** | **int** |  | 
**page_limit** | **int** |  | 
**items** | [**List[Schedule]**](Schedule.md) |  | 

## Example

```python
from across.sdk.v1.models.page_schedule import PageSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of PageSchedule from a JSON string
page_schedule_instance = PageSchedule.from_json(json)
# print the JSON string representation of the object
print(PageSchedule.to_json())

# convert the object into a dict
page_schedule_dict = page_schedule_instance.to_dict()
# create an instance of PageSchedule from a dict
page_schedule_from_dict = PageSchedule.from_dict(page_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


