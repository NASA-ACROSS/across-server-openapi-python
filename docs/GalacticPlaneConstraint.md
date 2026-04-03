# GalacticPlaneConstraint

Constraint that avoids observing too close to the Galactic Plane.  The Galactic Plane contains high densities of stars and dust, making it difficult to observe faint sources. This constraint ensures observations are conducted at sufficient latitude from the galactic equator.  Parameters ---------- min_latitude : float     Minimum galactic latitude (degrees) required for observation.     Observations closer to the galactic plane than this will be constrained.  Methods ------- __call__(time, ephemeris, coordinate)     Checks if the coordinate is too close to the galactic plane.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Galactic Plane']
**name** | **str** |  | [optional] [default to 'Galactic Plane Avoidance']
**min_latitude** | **float** | Minimum galactic latitude (degrees) for valid observations | [optional] [default to 10.0]

## Example

```python
from across.sdk.v1.models.galactic_plane_constraint import GalacticPlaneConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of GalacticPlaneConstraint from a JSON string
galactic_plane_constraint_instance = GalacticPlaneConstraint.from_json(json)
# print the JSON string representation of the object
print(GalacticPlaneConstraint.to_json())

# convert the object into a dict
galactic_plane_constraint_dict = galactic_plane_constraint_instance.to_dict()
# create an instance of GalacticPlaneConstraint from a dict
galactic_plane_constraint_from_dict = GalacticPlaneConstraint.from_dict(galactic_plane_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


