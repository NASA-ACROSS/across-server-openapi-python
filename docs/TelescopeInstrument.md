# TelescopeInstrument

A Pydantic model class representing a created Instrument for the Telescope Endpoint  Notes ----- Inherits from InstrumentBase  Methods ------- from_orm(instrument: InstrumentModel, include_footprints: bool, include_filters: bool) -> Instrument     Static method that instantiates this class from a Instrument database record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_on** | **datetime** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 
**telescope** | [**IDNameSchema**](IDNameSchema.md) |  | [optional] 
**footprints** | **List[List[Point]]** |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] [default to []]

## Example

```python
from across.sdk.v1.models.telescope_instrument import TelescopeInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of TelescopeInstrument from a JSON string
telescope_instrument_instance = TelescopeInstrument.from_json(json)
# print the JSON string representation of the object
print(TelescopeInstrument.to_json())

# convert the object into a dict
telescope_instrument_dict = telescope_instrument_instance.to_dict()
# create an instance of TelescopeInstrument from a dict
telescope_instrument_from_dict = TelescopeInstrument.from_dict(telescope_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


