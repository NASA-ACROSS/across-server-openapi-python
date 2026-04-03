# ObservationFootprintCreate

A Pydantic model class representing the data required to create an ObservationFootprint in the ACROSS SSA system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polygon** | [**List[Point]**](Point.md) |  | 

## Example

```python
from across.sdk.v1.models.observation_footprint_create import ObservationFootprintCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationFootprintCreate from a JSON string
observation_footprint_create_instance = ObservationFootprintCreate.from_json(json)
# print the JSON string representation of the object
print(ObservationFootprintCreate.to_json())

# convert the object into a dict
observation_footprint_create_dict = observation_footprint_create_instance.to_dict()
# create an instance of ObservationFootprintCreate from a dict
observation_footprint_create_from_dict = ObservationFootprintCreate.from_dict(observation_footprint_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


