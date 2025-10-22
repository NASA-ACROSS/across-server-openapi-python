# InstrumentConstraintsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'AltAz']
**name** | **str** |  | [optional] [default to 'Altitude/Azimuth Avoidance']
**min_angle** | **float** |  | [optional] 
**max_angle** | **float** |  | [optional] 
**polygon** | **List[List[float]]** |  | 
**altitude_min** | **float** |  | [optional] 
**altitude_max** | **float** |  | [optional] 
**azimuth_min** | **float** |  | [optional] 
**azimuth_max** | **float** |  | [optional] 

## Example

```python
from across.sdk.v1.models.instrument_constraints_inner import InstrumentConstraintsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentConstraintsInner from a JSON string
instrument_constraints_inner_instance = InstrumentConstraintsInner.from_json(json)
# print the JSON string representation of the object
print(InstrumentConstraintsInner.to_json())

# convert the object into a dict
instrument_constraints_inner_dict = instrument_constraints_inner_instance.to_dict()
# create an instance of InstrumentConstraintsInner from a dict
instrument_constraints_inner_from_dict = InstrumentConstraintsInner.from_dict(instrument_constraints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


