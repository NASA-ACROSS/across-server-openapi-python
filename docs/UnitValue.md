# UnitValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**unit** | **object** |  | 

## Example

```python
from across/sdk.models.unit_value import UnitValue

# TODO update the JSON string below
json = "{}"
# create an instance of UnitValue from a JSON string
unit_value_instance = UnitValue.from_json(json)
# print the JSON string representation of the object
print(UnitValue.to_json())

# convert the object into a dict
unit_value_dict = unit_value_instance.to_dict()
# create an instance of UnitValue from a dict
unit_value_from_dict = UnitValue.from_dict(unit_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


