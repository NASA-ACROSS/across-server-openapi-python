# Filter

A Pydantic model class representing a created Filter  Notes ----- Inherits from FilterBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_on** | **datetime** |  | 
**name** | **str** |  | 
**peak_wavelength** | **float** |  | 
**min_wavelength** | **float** |  | 
**max_wavelength** | **float** |  | 
**is_operational** | **bool** |  | 
**sensitivity_depth_unit** | **float** |  | 
**sensitivity_depth** | **float** |  | 
**sensitivity_time_seconds** | **float** |  | 
**reference_url** | **str** |  | 
**instrument_id** | **str** |  | 

## Example

```python
from across/sdk.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print(Filter.to_json())

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_from_dict = Filter.from_dict(filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


