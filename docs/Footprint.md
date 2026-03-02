# Footprint

Class to represent a astronomical instrument's imaging footprint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detectors** | [**List[Polygon]**](Polygon.md) |  | 

## Example

```python
from across.sdk.v1.models.footprint import Footprint

# TODO update the JSON string below
json = "{}"
# create an instance of Footprint from a JSON string
footprint_instance = Footprint.from_json(json)
# print the JSON string representation of the object
print(Footprint.to_json())

# convert the object into a dict
footprint_dict = footprint_instance.to_dict()
# create an instance of Footprint from a dict
footprint_from_dict = Footprint.from_dict(footprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


