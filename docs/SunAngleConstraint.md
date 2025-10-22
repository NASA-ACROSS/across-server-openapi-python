# SunAngleConstraint

For a given Sun avoidance angle, is a given coordinate inside this constraint?  Parameters ---------- min_angle     The minimum angle from the Sun that the spacecraft can point.  max_angle     The maximum angle from the Sun that the spacecraft can point.  Methods ------- __call__(coord, ephemeris, sun_radius_angle=None)     Checks if a given coordinate is inside the constraint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Sun']
**name** | **str** |  | [optional] [default to 'Sun Angle']
**min_angle** | **float** |  | [optional] 
**max_angle** | **float** |  | [optional] 

## Example

```python
from across.sdk.v1.models.sun_angle_constraint import SunAngleConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of SunAngleConstraint from a JSON string
sun_angle_constraint_instance = SunAngleConstraint.from_json(json)
# print the JSON string representation of the object
print(SunAngleConstraint.to_json())

# convert the object into a dict
sun_angle_constraint_dict = sun_angle_constraint_instance.to_dict()
# create an instance of SunAngleConstraint from a dict
sun_angle_constraint_from_dict = SunAngleConstraint.from_dict(sun_angle_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


