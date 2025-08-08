# Schedule

A Pydantic model class representing a created observing schedule for a telescope.  Parameters ---------- id : UUID     Schedule id observations : list[schemas.Observation]     A list of observations for the schedule created_on : datetime     Datetime the schedule was created created_by_id : UUID     AuthUser id checksum : str     Unique string representation of the schedule and observations  Notes ----- Inherits from ScheduleBase  Methods ------- create_checksum(schedule: ScheduleModel) -> str     Static method that creates the checksum from the schedule metadata and observation list metadata from_orm(schedule: ScheduleModel) -> Schedule     Static method that instantiates this class from a schedule database record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**telescope_id** | **str** |  | 
**name** | **str** |  | 
**date_range** | [**DateRange**](DateRange.md) |  | 
**status** | [**ScheduleStatus**](ScheduleStatus.md) |  | 
**external_id** | **str** |  | [optional] 
**fidelity** | [**ScheduleFidelity**](ScheduleFidelity.md) |  | [optional] 
**id** | **str** |  | 
**observations** | [**List[Observation]**](Observation.md) |  | 
**created_on** | **datetime** |  | 
**created_by_id** | **str** |  | 
**checksum** | **str** |  | [optional] [default to '']

## Example

```python
from across.sdk.v1.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


