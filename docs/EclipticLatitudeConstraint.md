# EclipticLatitudeConstraint

Constraint that avoids observing at low ecliptic latitudes.  The ecliptic plane contains zodiacal dust that scatters sunlight, creating zodiacal light that can contaminate observations. This constraint ensures observations are conducted at sufficient ecliptic latitude to avoid this background light.  Parameters ---------- min_latitude : float     Minimum ecliptic latitude (degrees) required for observation.     Observations closer to the ecliptic plane than this will be constrained.  Methods ------- __call__(time, ephemeris, coordinate)     Checks if the coordinate is too close to the ecliptic plane.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Ecliptic Latitude']
**name** | **str** |  | [optional] [default to 'Ecliptic Latitude']
**min_latitude** | **float** | Minimum ecliptic latitude (degrees) for valid observations | [optional] [default to 15.0]

## Example

```python
from across.sdk.v1.models.ecliptic_latitude_constraint import EclipticLatitudeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of EclipticLatitudeConstraint from a JSON string
ecliptic_latitude_constraint_instance = EclipticLatitudeConstraint.from_json(json)
# print the JSON string representation of the object
print(EclipticLatitudeConstraint.to_json())

# convert the object into a dict
ecliptic_latitude_constraint_dict = ecliptic_latitude_constraint_instance.to_dict()
# create an instance of EclipticLatitudeConstraint from a dict
ecliptic_latitude_constraint_from_dict = EclipticLatitudeConstraint.from_dict(ecliptic_latitude_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


