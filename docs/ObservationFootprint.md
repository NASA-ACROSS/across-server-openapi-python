# ObservationFootprint

A Pydantic model class representing a created ObservationFootprint  Notes ----- Inherits from ObservationFootprintBase  Methods ------- from_orm(obj: ObservationFootprintModel) -> ObservationFootprint     Static method that instantiates this class from an observation footprint database record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polygon** | [**List[Point]**](Point.md) |  | 
**id** | **str** |  | 
**observation_id** | **str** |  | 

## Example

```python
from across.sdk.v1.models.observation_footprint import ObservationFootprint

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationFootprint from a JSON string
observation_footprint_instance = ObservationFootprint.from_json(json)
# print the JSON string representation of the object
print(ObservationFootprint.to_json())

# convert the object into a dict
observation_footprint_dict = observation_footprint_instance.to_dict()
# create an instance of ObservationFootprint from a dict
observation_footprint_from_dict = ObservationFootprint.from_dict(observation_footprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


