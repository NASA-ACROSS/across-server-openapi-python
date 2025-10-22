# Instrument

A Pydantic model class representing a created Instrument  Notes ----- Inherits from InstrumentBase  Methods ------- from_orm(instrument: InstrumentModel) -> Instrument     Static method that instantiates this class from a Instrument database record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_on** | **datetime** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 
**telescope** | [**IDNameSchema**](IDNameSchema.md) |  | [optional] 
**footprints** | **List[List[Point]]** |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 
**constraints** | [**List[InstrumentConstraintsInner]**](InstrumentConstraintsInner.md) |  | [optional] 
**visibility_type** | [**VisibilityType**](VisibilityType.md) |  | [optional] 

## Example

```python
from across.sdk.v1.models.instrument import Instrument

# TODO update the JSON string below
json = "{}"
# create an instance of Instrument from a JSON string
instrument_instance = Instrument.from_json(json)
# print the JSON string representation of the object
print(Instrument.to_json())

# convert the object into a dict
instrument_dict = instrument_instance.to_dict()
# create an instance of Instrument from a dict
instrument_from_dict = Instrument.from_dict(instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


