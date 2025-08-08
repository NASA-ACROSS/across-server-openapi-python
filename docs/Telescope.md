# Telescope

A Pydantic model class representing a created telescope  Notes ----- Inherits from TelescopeBase  Methods ------- from_orm(telescope: TelescopeModel) -> Telescope     Static method that instantiates this class from a telescope database record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_on** | **datetime** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 
**observatory** | [**IDNameSchema**](IDNameSchema.md) |  | [optional] 
**instruments** | [**List[IDNameSchema]**](IDNameSchema.md) |  | [optional] 

## Example

```python
from across/sdk.models.telescope import Telescope

# TODO update the JSON string below
json = "{}"
# create an instance of Telescope from a JSON string
telescope_instance = Telescope.from_json(json)
# print the JSON string representation of the object
print(Telescope.to_json())

# convert the object into a dict
telescope_dict = telescope_instance.to_dict()
# create an instance of Telescope from a dict
telescope_from_dict = Telescope.from_dict(telescope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


