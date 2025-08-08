# TLE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**norad_id** | **int** |  | 
**satellite_name** | **str** |  | 
**tle1** | **str** |  | 
**tle2** | **str** |  | 
**epoch** | **datetime** | Calculate the Epoch of the TLE file. See https://celestrak.org/columns/v04n03/#FAQ04 for more information on how the year / epoch encoding works.  Returns -------     The calculated epoch of the TLE. | [readonly] 

## Example

```python
from across/sdk.models.tle import TLE

# TODO update the JSON string below
json = "{}"
# create an instance of TLE from a JSON string
tle_instance = TLE.from_json(json)
# print the JSON string representation of the object
print(TLE.to_json())

# convert the object into a dict
tle_dict = tle_instance.to_dict()
# create an instance of TLE from a dict
tle_from_dict = TLE.from_dict(tle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


