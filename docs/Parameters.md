# Parameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**norad_id** | **int** |  | 
**norad_satellite_name** | **str** |  | 
**naif_id** | **int** |  | 
**spice_kernel_url** | **str** |  | 
**longitude** | **float** |  | 
**latitude** | **float** |  | 
**height** | **float** |  | 

## Example

```python
from across.sdk.v1.models.parameters import Parameters

# TODO update the JSON string below
json = "{}"
# create an instance of Parameters from a JSON string
parameters_instance = Parameters.from_json(json)
# print the JSON string representation of the object
print(Parameters.to_json())

# convert the object into a dict
parameters_dict = parameters_instance.to_dict()
# create an instance of Parameters from a dict
parameters_from_dict = Parameters.from_dict(parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


