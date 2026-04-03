# InstrumentConstraintsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Pointing']
**name** | **str** |  | [optional] [default to 'Pointing']
**min_angle** | **float** |  | [optional] 
**max_angle** | **float** |  | [optional] 
**polygon** | **List[List[float]]** |  | [optional] 
**altitude_min** | **float** |  | [optional] 
**altitude_max** | **float** |  | [optional] 
**azimuth_min** | **float** |  | [optional] 
**azimuth_max** | **float** |  | [optional] 
**min_latitude** | **float** | Minimum ecliptic latitude (degrees) for valid observations | [optional] [default to 15.0]
**min_separation** | **float** | Minimum angular separation (degrees) from Solar System objects | [optional] [default to 10.0]
**magnitude_limit** | **float** | Magnitude limit for stars to avoid (brighter than this) | [optional] [default to 6.0]
**max_air_mass** | **float** | Maximum allowed airmass for observations | [optional] [default to 2.0]
**max_magnitude** | **float** | Maximum apparent magnitude of Solar System objects to consider | [optional] [default to 5.0]
**bodies** | [**List[SolarSystemConstraintBodiesInner]**](SolarSystemConstraintBodiesInner.md) | List of Solar System bodies to avoid | [optional] [default to [mercury, venus, mars, jupiter, saturn]]
**twilight_type** | [**TwilightType**](TwilightType.md) | Type of twilight defining daytime boundaries | [optional] 
**pointings** | [**List[Pointing]**](Pointing.md) |  | 

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


