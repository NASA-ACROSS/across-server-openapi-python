# AltAzConstraint

For a given Alt/Az constraint, is a given coordinate inside this constraint? Constraint is both defined by a polygon exclusion region and a minimum and maximum altitude. By default the minimum and maximum altitude values are 0 and 90 degrees respectively. Polygon restriction regions can be combined with minimum and maximum altitude restrictions.  Parameters ---------- polygon     The polygon defining the exclusion region. min     The minimum altitude in degrees. max     The maximum altitude in degrees.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'AltAz']
**name** | **str** |  | [optional] [default to 'Altitude/Azimuth Avoidance']
**polygon** | **List[List[float]]** |  | [optional] 
**altitude_min** | **float** |  | [optional] 
**altitude_max** | **float** |  | [optional] 
**azimuth_min** | **float** |  | [optional] 
**azimuth_max** | **float** |  | [optional] 

## Example

```python
from across.sdk.v1.models.alt_az_constraint import AltAzConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of AltAzConstraint from a JSON string
alt_az_constraint_instance = AltAzConstraint.from_json(json)
# print the JSON string representation of the object
print(AltAzConstraint.to_json())

# convert the object into a dict
alt_az_constraint_dict = alt_az_constraint_instance.to_dict()
# create an instance of AltAzConstraint from a dict
alt_az_constraint_from_dict = AltAzConstraint.from_dict(alt_az_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


