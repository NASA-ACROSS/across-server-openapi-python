# SAAPolygonConstraint

Polygon based SAA constraint. The SAA is defined by a Shapely Polygon, and this constraint will calculate for a given set of times and a given ephemeris whether the spacecraft is in that SAA polygon.  Attributes ---------- polygon     Shapely Polygon object defining the SAA polygon.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'SAA']
**name** | **str** |  | [optional] [default to 'South Atlantic Anomaly']
**polygon** | **List[List[float]]** |  | [optional] 

## Example

```python
from across.sdk.v1.models.saa_polygon_constraint import SAAPolygonConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of SAAPolygonConstraint from a JSON string
saa_polygon_constraint_instance = SAAPolygonConstraint.from_json(json)
# print the JSON string representation of the object
print(SAAPolygonConstraint.to_json())

# convert the object into a dict
saa_polygon_constraint_dict = saa_polygon_constraint_instance.to_dict()
# create an instance of SAAPolygonConstraint from a dict
saa_polygon_constraint_from_dict = SAAPolygonConstraint.from_dict(saa_polygon_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


