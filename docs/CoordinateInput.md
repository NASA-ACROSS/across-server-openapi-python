# CoordinateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra** | **float** |  | 
**dec** | **float** |  | 

## Example

```python
from across.sdk.v1.models.coordinate_input import CoordinateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinateInput from a JSON string
coordinate_input_instance = CoordinateInput.from_json(json)
# print the JSON string representation of the object
print(CoordinateInput.to_json())

# convert the object into a dict
coordinate_input_dict = coordinate_input_instance.to_dict()
# create an instance of CoordinateInput from a dict
coordinate_input_from_dict = CoordinateInput.from_dict(coordinate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


