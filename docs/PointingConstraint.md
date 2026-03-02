# PointingConstraint

Footprint based pointing constraint. A Pointing is defined as a Footprint with a start and end time. This constraint will calculate whether a target was within any set of pointings.  Attributes ---------- pointings     List of Pointing objects. start_time     AstropyDateTime defining the start of the pointing end_time     AstropyDateTime defining the end of the pointing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Pointing']
**name** | **str** |  | [optional] [default to 'Pointing']
**pointings** | [**List[Pointing]**](Pointing.md) |  | 

## Example

```python
from across.sdk.v1.models.pointing_constraint import PointingConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of PointingConstraint from a JSON string
pointing_constraint_instance = PointingConstraint.from_json(json)
# print the JSON string representation of the object
print(PointingConstraint.to_json())

# convert the object into a dict
pointing_constraint_dict = pointing_constraint_instance.to_dict()
# create an instance of PointingConstraint from a dict
pointing_constraint_from_dict = PointingConstraint.from_dict(pointing_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


