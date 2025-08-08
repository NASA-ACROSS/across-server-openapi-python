# FrequencyBandpass

A class representing a bandpass filter defined in terms of frequency.  Inherits from `BaseBandpass`, this class specializes the filter to operate in the frequency domain.  Attributes:     type (Literal['FREQUENCY']): A constant string indicating the type of the bandpass filter.     unit (FrequencyUnit): The unit of measurement for the frequency.  Methods:     model_post_init(__context: Any) -> None:         Ensures the min and max frequency values are positive and valid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_name** | **str** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**type** | **str** |  | [optional] [default to 'FREQUENCY']
**unit** | [**FrequencyUnit**](FrequencyUnit.md) |  | 

## Example

```python
from across/sdk.models.frequency_bandpass import FrequencyBandpass

# TODO update the JSON string below
json = "{}"
# create an instance of FrequencyBandpass from a JSON string
frequency_bandpass_instance = FrequencyBandpass.from_json(json)
# print the JSON string representation of the object
print(FrequencyBandpass.to_json())

# convert the object into a dict
frequency_bandpass_dict = frequency_bandpass_instance.to_dict()
# create an instance of FrequencyBandpass from a dict
frequency_bandpass_from_dict = FrequencyBandpass.from_dict(frequency_bandpass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


