# Observation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** |  | 
**object_name** | **str** |  | 
**pointing_position** | [**Coordinate**](Coordinate.md) |  | [optional] 
**date_range** | [**DateRange**](DateRange.md) |  | 
**external_observation_id** | **str** |  | 
**type** | [**ObservationType**](ObservationType.md) |  | 
**status** | [**ObservationStatus**](ObservationStatus.md) |  | 
**pointing_angle** | **float** |  | [optional] 
**exposure_time** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**proposal_reference** | **str** |  | [optional] 
**object_position** | [**Coordinate**](Coordinate.md) |  | [optional] 
**depth** | [**UnitValue**](UnitValue.md) |  | [optional] 
**bandpass** | [**Bandpass**](Bandpass.md) |  | 
**t_resolution** | **float** |  | [optional] 
**em_res_power** | **float** |  | [optional] 
**o_ucd** | **str** |  | [optional] 
**pol_states** | **str** |  | [optional] 
**pol_xel** | **str** |  | [optional] 
**category** | [**IVOAObsCategory**](IVOAObsCategory.md) |  | [optional] 
**priority** | **int** |  | [optional] 
**tracking_type** | [**IVOAObsTrackingType**](IVOAObsTrackingType.md) |  | [optional] 
**id** | **str** |  | 
**schedule_id** | **str** |  | 
**created_on** | **datetime** |  | 
**created_by_id** | **str** |  | [optional] 

## Example

```python
from across/sdk.models.observation import Observation

# TODO update the JSON string below
json = "{}"
# create an instance of Observation from a JSON string
observation_instance = Observation.from_json(json)
# print the JSON string representation of the object
print(Observation.to_json())

# convert the object into a dict
observation_dict = observation_instance.to_dict()
# create an instance of Observation from a dict
observation_from_dict = Observation.from_dict(observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


