# MoonAngleConstraint

For a given Moon avoidance angle, is a given coordinate inside this constraint?  Parameters ---------- min_angle     The minimum angle from the Moon that the spacecraft can point.  Methods ------- __call__(coord, ephemeris, moon_radius_angle=None)     Checks if a given coordinate is inside the constraint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Moon']
**name** | **str** |  | [optional] [default to 'Moon Angle']
**min_angle** | **float** |  | [optional] 
**max_angle** | **float** |  | [optional] 

## Example

```python
from across.sdk.v1.models.moon_angle_constraint import MoonAngleConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of MoonAngleConstraint from a JSON string
moon_angle_constraint_instance = MoonAngleConstraint.from_json(json)
# print the JSON string representation of the object
print(MoonAngleConstraint.to_json())

# convert the object into a dict
moon_angle_constraint_dict = moon_angle_constraint_instance.to_dict()
# create an instance of MoonAngleConstraint from a dict
moon_angle_constraint_from_dict = MoonAngleConstraint.from_dict(moon_angle_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


