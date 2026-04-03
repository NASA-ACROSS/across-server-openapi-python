# GalacticBulgeConstraint

Constraint that avoids observing too close to the Galactic Bulge.  The Galactic Bulge is a crowded region with extremely high stellar density, making it difficult to observe individual sources. This constraint ensures observations avoid this region.  Parameters ---------- min_separation : float     Minimum angular separation (degrees) required from the Galactic Bulge.     Observations closer than this will be constrained.  Methods ------- __call__(time, ephemeris, coordinate)     Checks if the coordinate is too close to the Galactic Bulge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Galactic Bulge']
**name** | **str** |  | [optional] [default to 'Galactic Bulge Avoidance']
**min_separation** | **float** | Minimum angular separation (degrees) from Galactic Bulge | [optional] [default to 10.0]

## Example

```python
from across.sdk.v1.models.galactic_bulge_constraint import GalacticBulgeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of GalacticBulgeConstraint from a JSON string
galactic_bulge_constraint_instance = GalacticBulgeConstraint.from_json(json)
# print the JSON string representation of the object
print(GalacticBulgeConstraint.to_json())

# convert the object into a dict
galactic_bulge_constraint_dict = galactic_bulge_constraint_instance.to_dict()
# create an instance of GalacticBulgeConstraint from a dict
galactic_bulge_constraint_from_dict = GalacticBulgeConstraint.from_dict(galactic_bulge_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


