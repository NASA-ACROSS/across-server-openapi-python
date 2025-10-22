# VisibilityResult

A Pydantic model class representing the visibility calculation parameters.  This class is used for visibility calculations in the ACROSS SSA system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** |  | 
**visibility_windows** | [**List[VisibilityWindow]**](VisibilityWindow.md) |  | 

## Example

```python
from across.sdk.v1.models.visibility_result import VisibilityResult

# TODO update the JSON string below
json = "{}"
# create an instance of VisibilityResult from a JSON string
visibility_result_instance = VisibilityResult.from_json(json)
# print the JSON string representation of the object
print(VisibilityResult.to_json())

# convert the object into a dict
visibility_result_dict = visibility_result_instance.to_dict()
# create an instance of VisibilityResult from a dict
visibility_result_from_dict = VisibilityResult.from_dict(visibility_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


