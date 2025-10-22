# Window

Visibility Window

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | [**ConstrainedDate**](ConstrainedDate.md) |  | 
**end** | [**ConstrainedDate**](ConstrainedDate.md) |  | 

## Example

```python
from across.sdk.v1.models.window import Window

# TODO update the JSON string below
json = "{}"
# create an instance of Window from a JSON string
window_instance = Window.from_json(json)
# print the JSON string representation of the object
print(Window.to_json())

# convert the object into a dict
window_dict = window_instance.to_dict()
# create an instance of Window from a dict
window_from_dict = Window.from_dict(window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


