# Bandpass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_name** | **str** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**type** | **str** |  | [optional] [default to 'ENERGY']
**unit** | [**WavelengthUnit**](WavelengthUnit.md) |  | 
**central_wavelength** | **float** |  | [optional] 
**peak_wavelength** | **float** |  | [optional] 
**bandwidth** | **float** |  | [optional] 

## Example

```python
from across/sdk.models.bandpass import Bandpass

# TODO update the JSON string below
json = "{}"
# create an instance of Bandpass from a JSON string
bandpass_instance = Bandpass.from_json(json)
# print the JSON string representation of the object
print(Bandpass.to_json())

# convert the object into a dict
bandpass_dict = bandpass_instance.to_dict()
# create an instance of Bandpass from a dict
bandpass_from_dict = Bandpass.from_dict(bandpass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


