# LocalizationCreate

A Pydantic model class representing data required to create a Localization object in the ACROSS system. Inherits from LocalizationBase  Methods ---------- to_orm:     Returns an ORM Localization instance with the supplied data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra** | **float** |  | [optional] 
**dec** | **float** |  | [optional] 
**contours** | [**List[LocalizationContourBase]**](LocalizationContourBase.md) |  | [optional] 
**probability_enclosed** | **float** |  | [optional] 

## Example

```python
from across.sdk.v1.models.localization_create import LocalizationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationCreate from a JSON string
localization_create_instance = LocalizationCreate.from_json(json)
# print the JSON string representation of the object
print(LocalizationCreate.to_json())

# convert the object into a dict
localization_create_dict = localization_create_instance.to_dict()
# create an instance of LocalizationCreate from a dict
localization_create_from_dict = LocalizationCreate.from_dict(localization_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


