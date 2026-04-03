# SolarSystemConstraint

Constraint that avoids observing too close to bright Solar System objects.  Planets and other bright Solar System objects can contaminate observations or cause detector issues. This constraint ensures observations avoid these objects by maintaining sufficient angular separation.  Parameters ---------- min_separation : float     Minimum angular separation (degrees) required from Solar System objects.     Observations closer than this will be constrained. bodies : list[str]     List of Solar System bodies to avoid. Defaults to major planets.     Options include: 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'.  Methods ------- __call__(time, ephemeris, coordinate)     Checks if the coordinate is too close to any Solar System object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Solar System']
**name** | **str** |  | [optional] [default to 'Solar System Object Avoidance']
**min_separation** | **float** | Minimum angular separation (degrees) from Solar System objects | [optional] [default to 10.0]
**max_magnitude** | **float** | Maximum apparent magnitude of Solar System objects to consider | [optional] [default to 5.0]
**bodies** | [**List[SolarSystemConstraintBodiesInner]**](SolarSystemConstraintBodiesInner.md) | List of Solar System bodies to avoid | [optional] [default to [mercury, venus, mars, jupiter, saturn]]

## Example

```python
from across.sdk.v1.models.solar_system_constraint import SolarSystemConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of SolarSystemConstraint from a JSON string
solar_system_constraint_instance = SolarSystemConstraint.from_json(json)
# print the JSON string representation of the object
print(SolarSystemConstraint.to_json())

# convert the object into a dict
solar_system_constraint_dict = solar_system_constraint_instance.to_dict()
# create an instance of SolarSystemConstraint from a dict
solar_system_constraint_from_dict = SolarSystemConstraint.from_dict(solar_system_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


