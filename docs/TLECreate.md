# TLECreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**norad_id** | **int** |  | 
**satellite_name** | **str** |  | 
**tle1** | **str** |  | 
**tle2** | **str** |  | 

## Example

```python
from across/sdk.models.tle_create import TLECreate

# TODO update the JSON string below
json = "{}"
# create an instance of TLECreate from a JSON string
tle_create_instance = TLECreate.from_json(json)
# print the JSON string representation of the object
print(TLECreate.to_json())

# convert the object into a dict
tle_create_dict = tle_create_instance.to_dict()
# create an instance of TLECreate from a dict
tle_create_from_dict = TLECreate.from_dict(tle_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


