# Pointing

Class describing an astronomical pointing A pointing is described as a footprint valid for a given time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**footprint** | [**Footprint**](Footprint.md) |  | 
**start_time** | [**StartTime**](StartTime.md) |  | 
**end_time** | [**EndTime**](EndTime.md) |  | 

## Example

```python
from across.sdk.v1.models.pointing import Pointing

# TODO update the JSON string below
json = "{}"
# create an instance of Pointing from a JSON string
pointing_instance = Pointing.from_json(json)
# print the JSON string representation of the object
print(Pointing.to_json())

# convert the object into a dict
pointing_dict = pointing_instance.to_dict()
# create an instance of Pointing from a dict
pointing_from_dict = Pointing.from_dict(pointing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


