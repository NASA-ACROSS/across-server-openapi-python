# BrightStarConstraint

Constraint that avoids observing too close to bright stars.  Bright stars can cause detector saturation, blooming, or scattered light issues. This constraint ensures observations are conducted at sufficient angular distance from bright stars.  Parameters ---------- min_separation : float     Minimum angular separation (degrees) required from bright stars.     Observations closer than this to bright stars will be constrained. magnitude_limit : float     Magnitude limit for bright stars to avoid. Stars brighter than this     magnitude will be considered for avoidance. Default is 6.0 (naked eye visible).  Methods ------- __call__(time, ephemeris, coordinate)     Checks if the coordinate is too close to any bright star.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Bright Star']
**name** | **str** |  | [optional] [default to 'Bright Star Avoidance']
**min_separation** | **float** | Minimum angular separation (degrees) from bright stars | [optional] [default to 5.0]
**magnitude_limit** | **float** | Magnitude limit for stars to avoid (brighter than this) | [optional] [default to 6.0]

## Example

```python
from across.sdk.v1.models.bright_star_constraint import BrightStarConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of BrightStarConstraint from a JSON string
bright_star_constraint_instance = BrightStarConstraint.from_json(json)
# print the JSON string representation of the object
print(BrightStarConstraint.to_json())

# convert the object into a dict
bright_star_constraint_dict = bright_star_constraint_instance.to_dict()
# create an instance of BrightStarConstraint from a dict
bright_star_constraint_from_dict = BrightStarConstraint.from_dict(bright_star_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


