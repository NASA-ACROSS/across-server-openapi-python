# ObservationCreate


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
**created_on** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | [optional] 

## Example

```python
from across/sdk.models.observation_create import ObservationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationCreate from a JSON string
observation_create_instance = ObservationCreate.from_json(json)
# print the JSON string representation of the object
print(ObservationCreate.to_json())

# convert the object into a dict
observation_create_dict = observation_create_instance.to_dict()
# create an instance of ObservationCreate from a dict
observation_create_from_dict = ObservationCreate.from_dict(observation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


