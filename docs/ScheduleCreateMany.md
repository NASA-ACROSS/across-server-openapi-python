# ScheduleCreateMany

A Pydantic model class representing bulk schedule creation  Parameters -------------- schedules: list[ScheduleCreate]     A list of ScheduleCreate objects to be added in bulk telescope_id: uuid     The ID of the telescope belonging to the schedules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedules** | [**List[ScheduleCreate]**](ScheduleCreate.md) |  | 
**telescope_id** | **str** |  | 

## Example

```python
from across.sdk.v1.models.schedule_create_many import ScheduleCreateMany

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCreateMany from a JSON string
schedule_create_many_instance = ScheduleCreateMany.from_json(json)
# print the JSON string representation of the object
print(ScheduleCreateMany.to_json())

# convert the object into a dict
schedule_create_many_dict = schedule_create_many_instance.to_dict()
# create an instance of ScheduleCreateMany from a dict
schedule_create_many_from_dict = ScheduleCreateMany.from_dict(schedule_create_many_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


