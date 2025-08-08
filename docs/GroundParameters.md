# GroundParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**longitude** | **float** |  | 
**latitude** | **float** |  | 
**height** | **float** |  | 

## Example

```python
from across.sdk.v1.models.ground_parameters import GroundParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GroundParameters from a JSON string
ground_parameters_instance = GroundParameters.from_json(json)
# print the JSON string representation of the object
print(GroundParameters.to_json())

# convert the object into a dict
ground_parameters_dict = ground_parameters_instance.to_dict()
# create an instance of GroundParameters from a dict
ground_parameters_from_dict = GroundParameters.from_dict(ground_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


