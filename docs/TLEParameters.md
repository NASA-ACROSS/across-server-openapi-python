# TLEParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**norad_id** | **int** |  | 
**norad_satellite_name** | **str** |  | 

## Example

```python
from across/sdk.models.tle_parameters import TLEParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TLEParameters from a JSON string
tle_parameters_instance = TLEParameters.from_json(json)
# print the JSON string representation of the object
print(TLEParameters.to_json())

# convert the object into a dict
tle_parameters_dict = tle_parameters_instance.to_dict()
# create an instance of TLEParameters from a dict
tle_parameters_from_dict = TLEParameters.from_dict(tle_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


