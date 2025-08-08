# Observatory

A Pydantic model class representing a created observatory  Notes ----- Inherits from ObservatoryBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_on** | **datetime** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 
**type** | [**ObservatoryType**](ObservatoryType.md) |  | 
**telescopes** | [**List[IDNameSchema]**](IDNameSchema.md) |  | [optional] 
**ephemeris_types** | [**List[ObservatoryEphemerisType]**](ObservatoryEphemerisType.md) |  | [optional] 

## Example

```python
from across.sdk.v1.models.observatory import Observatory

# TODO update the JSON string below
json = "{}"
# create an instance of Observatory from a JSON string
observatory_instance = Observatory.from_json(json)
# print the JSON string representation of the object
print(Observatory.to_json())

# convert the object into a dict
observatory_dict = observatory_instance.to_dict()
# create an instance of Observatory from a dict
observatory_from_dict = Observatory.from_dict(observatory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


