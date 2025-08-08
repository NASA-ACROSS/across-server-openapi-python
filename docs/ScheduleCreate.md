# ScheduleCreate

A Pydantic model class representing the a schedule to be created in the database  Parameters ---------- observations : list[schemas.Observation]     A list of observations for the schedule  Notes --------- Inherits from ScheduleBase  Methods to_orm(self, created_by_id: UUID) -> ScheduleModel     Method that creates the ORM record for a schedule to be serialized into the database.     This method does not instantiate the list of observations, the observation schema requires     a schedule ID so it is instantiated after the model id is flushed within the service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**telescope_id** | **str** |  | 
**name** | **str** |  | 
**date_range** | [**DateRange**](DateRange.md) |  | 
**status** | [**ScheduleStatus**](ScheduleStatus.md) |  | 
**external_id** | **str** |  | [optional] 
**fidelity** | [**ScheduleFidelity**](ScheduleFidelity.md) |  | [optional] 
**observations** | [**List[ObservationCreate]**](ObservationCreate.md) |  | 

## Example

```python
from across/sdk.models.schedule_create import ScheduleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCreate from a JSON string
schedule_create_instance = ScheduleCreate.from_json(json)
# print the JSON string representation of the object
print(ScheduleCreate.to_json())

# convert the object into a dict
schedule_create_dict = schedule_create_instance.to_dict()
# create an instance of ScheduleCreate from a dict
schedule_create_from_dict = ScheduleCreate.from_dict(schedule_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


