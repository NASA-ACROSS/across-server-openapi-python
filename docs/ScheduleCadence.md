# ScheduleCadence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**telescope_id** | **str** |  | 
**cron** | **str** |  | 
**schedule_status** | [**ScheduleStatus**](ScheduleStatus.md) |  | 

## Example

```python
from across.sdk.v1.models.schedule_cadence import ScheduleCadence

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCadence from a JSON string
schedule_cadence_instance = ScheduleCadence.from_json(json)
# print the JSON string representation of the object
print(ScheduleCadence.to_json())

# convert the object into a dict
schedule_cadence_dict = schedule_cadence_instance.to_dict()
# create an instance of ScheduleCadence from a dict
schedule_cadence_from_dict = ScheduleCadence.from_dict(schedule_cadence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


