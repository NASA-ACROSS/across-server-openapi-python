# WavelengthBandpass

A class representing a bandpass filter defined in terms of wavelength.  Inherits from `BaseBandpass`, this class specializes the filter to operate in the wavelength domain and provides additional functionality for wavelength-based filters.  Attributes:     type (Literal['WAVELENGTH']): A constant string indicating the type of the bandpass filter.     central_wavelength (float | None): The central wavelength of the filter.     bandwidth (float | None): The bandwidth of the filter.     unit (WavelengthUnit): The unit of measurement for the wavelength.  Methods:     model_post_init(__context: Any) -> None:         Performs validation and calculation of central wavelength and bandwidth based on the min/max range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_name** | **str** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**type** | **str** |  | [optional] [default to 'WAVELENGTH']
**central_wavelength** | **float** |  | [optional] 
**peak_wavelength** | **float** |  | [optional] 
**bandwidth** | **float** |  | [optional] 
**unit** | [**WavelengthUnit**](WavelengthUnit.md) |  | 

## Example

```python
from across/sdk.models.wavelength_bandpass import WavelengthBandpass

# TODO update the JSON string below
json = "{}"
# create an instance of WavelengthBandpass from a JSON string
wavelength_bandpass_instance = WavelengthBandpass.from_json(json)
# print the JSON string representation of the object
print(WavelengthBandpass.to_json())

# convert the object into a dict
wavelength_bandpass_dict = wavelength_bandpass_instance.to_dict()
# create an instance of WavelengthBandpass from a dict
wavelength_bandpass_from_dict = WavelengthBandpass.from_dict(wavelength_bandpass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


