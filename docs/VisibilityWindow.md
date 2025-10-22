# VisibilityWindow

Represents a Visibility Window with max visibility duration and information about the start and end constraints reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window** | [**Window**](Window.md) |  | 
**max_visibility_duration** | **int** |  | 
**constraint_reason** | [**ConstraintReason**](ConstraintReason.md) |  | 

## Example

```python
from across.sdk.v1.models.visibility_window import VisibilityWindow

# TODO update the JSON string below
json = "{}"
# create an instance of VisibilityWindow from a JSON string
visibility_window_instance = VisibilityWindow.from_json(json)
# print the JSON string representation of the object
print(VisibilityWindow.to_json())

# convert the object into a dict
visibility_window_dict = visibility_window_instance.to_dict()
# create an instance of VisibilityWindow from a dict
visibility_window_from_dict = VisibilityWindow.from_dict(visibility_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


