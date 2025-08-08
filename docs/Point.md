# Point

A Pydantic model class representing a 2D Point.  Parameters ---------- x: float y: float

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | 
**y** | **float** |  | 

## Example

```python
from across/sdk.models.point import Point

# TODO update the JSON string below
json = "{}"
# create an instance of Point from a JSON string
point_instance = Point.from_json(json)
# print the JSON string representation of the object
print(Point.to_json())

# convert the object into a dict
point_dict = point_instance.to_dict()
# create an instance of Point from a dict
point_from_dict = Point.from_dict(point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


