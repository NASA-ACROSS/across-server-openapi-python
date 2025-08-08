# EnergyBandpass

A class representing a bandpass filter defined in terms of energy.  Inherits from `BaseBandpass`, this class specializes the filter to operate in the energy domain.  Attributes:     type (Literal['ENERGY']): A constant string indicating the type of the bandpass filter.     unit (EnergyUnit): The unit of measurement for the energy.  Methods:     model_post_init(__context: Any) -> None:         Ensures the min and max energy values are positive and valid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_name** | **str** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**type** | **str** |  | [optional] [default to 'ENERGY']
**unit** | [**EnergyUnit**](EnergyUnit.md) |  | 

## Example

```python
from across/sdk.models.energy_bandpass import EnergyBandpass

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyBandpass from a JSON string
energy_bandpass_instance = EnergyBandpass.from_json(json)
# print the JSON string representation of the object
print(EnergyBandpass.to_json())

# convert the object into a dict
energy_bandpass_dict = energy_bandpass_instance.to_dict()
# create an instance of EnergyBandpass from a dict
energy_bandpass_from_dict = EnergyBandpass.from_dict(energy_bandpass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


