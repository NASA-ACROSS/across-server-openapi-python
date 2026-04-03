# VisibilityComputedValues

A class to hold computed values used in constraint calculations.  Attributes ---------- sun_angle     Angular distance between the Sun and the target coordinate. moon_angle     Angular distance between the Moon and the target coordinate. earth_angle     Angular distance between the Earth limb and the target coordinate. alt_az     Altitude-azimuth coordinates of the target from the observatory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sun_angle** | [**SunAngle**](SunAngle.md) |  | [optional] 
**moon_angle** | [**MoonAngle**](MoonAngle.md) |  | [optional] 
**earth_angle** | [**EarthAngle**](EarthAngle.md) |  | [optional] 
**alt_az** | **List[Dict[str, Optional[float]]]** |  | [optional] 
**air_mass** | **List[object]** |  | [optional] 
**sun_altitude** | [**SunAltitude**](SunAltitude.md) |  | [optional] 
**body_separation** | [**Dict[str, VisibilityComputedValuesBodySeparationValue]**](VisibilityComputedValuesBodySeparationValue.md) |  | [optional] 
**body_coordinates** | **Dict[str, List[Dict[str, float]]]** |  | [optional] 
**body_magnitude** | **Dict[str, List[object]]** |  | [optional] 
**galactic_bulge_separation** | [**GalacticBulgeSeparation**](GalacticBulgeSeparation.md) |  | [optional] 

## Example

```python
from across.sdk.v1.models.visibility_computed_values import VisibilityComputedValues

# TODO update the JSON string below
json = "{}"
# create an instance of VisibilityComputedValues from a JSON string
visibility_computed_values_instance = VisibilityComputedValues.from_json(json)
# print the JSON string representation of the object
print(VisibilityComputedValues.to_json())

# convert the object into a dict
visibility_computed_values_dict = visibility_computed_values_instance.to_dict()
# create an instance of VisibilityComputedValues from a dict
visibility_computed_values_from_dict = VisibilityComputedValues.from_dict(visibility_computed_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


