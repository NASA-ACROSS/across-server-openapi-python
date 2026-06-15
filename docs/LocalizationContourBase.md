# LocalizationContourBase

A Pydantic model class representing a base LocalizationContour in the ACROSS system.  Parameters ---------- contour: list[Point]     List of vertices mapping the localization region contours  Methods --------- region_to_wkt:     Convert the contour polygon to a WKT element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contour** | [**List[Point]**](Point.md) |  | 

## Example

```python
from across.sdk.v1.models.localization_contour_base import LocalizationContourBase

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationContourBase from a JSON string
localization_contour_base_instance = LocalizationContourBase.from_json(json)
# print the JSON string representation of the object
print(LocalizationContourBase.to_json())

# convert the object into a dict
localization_contour_base_dict = localization_contour_base_instance.to_dict()
# create an instance of LocalizationContourBase from a dict
localization_contour_base_from_dict = LocalizationContourBase.from_dict(localization_contour_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


