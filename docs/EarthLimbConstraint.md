# EarthLimbConstraint

For a given Earth limb avoidance angle, is a given coordinate inside this constraint?  Parameters ---------- name     The name of the constraint. short_name     The short name of the constraint. min_angle     The minimum angle from the Earth limb that the spacecraft can point.  Methods ------- __call__(coord, ephemeris, earth_radius_angle=None)     Checks if a given coordinate is inside the constraint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Earth']
**name** | **str** |  | [optional] [default to 'Earth Limb']
**min_angle** | **float** |  | [optional] 
**max_angle** | **float** |  | [optional] 

## Example

```python
from across.sdk.v1.models.earth_limb_constraint import EarthLimbConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of EarthLimbConstraint from a JSON string
earth_limb_constraint_instance = EarthLimbConstraint.from_json(json)
# print the JSON string representation of the object
print(EarthLimbConstraint.to_json())

# convert the object into a dict
earth_limb_constraint_dict = earth_limb_constraint_instance.to_dict()
# create an instance of EarthLimbConstraint from a dict
earth_limb_constraint_from_dict = EarthLimbConstraint.from_dict(earth_limb_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


