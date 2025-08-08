# ObservatoryEphemerisType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ephemeris_type** | [**EphemerisType**](EphemerisType.md) |  | 
**priority** | **int** |  | 
**parameters** | [**Parameters**](Parameters.md) |  | 

## Example

```python
from across/sdk.models.observatory_ephemeris_type import ObservatoryEphemerisType

# TODO update the JSON string below
json = "{}"
# create an instance of ObservatoryEphemerisType from a JSON string
observatory_ephemeris_type_instance = ObservatoryEphemerisType.from_json(json)
# print the JSON string representation of the object
print(ObservatoryEphemerisType.to_json())

# convert the object into a dict
observatory_ephemeris_type_dict = observatory_ephemeris_type_instance.to_dict()
# create an instance of ObservatoryEphemerisType from a dict
observatory_ephemeris_type_from_dict = ObservatoryEphemerisType.from_dict(observatory_ephemeris_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


