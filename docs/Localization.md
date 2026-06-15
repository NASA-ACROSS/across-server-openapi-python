# Localization

A Pydantic model class representing a Localization in the ACROSS system. Inherits from LocalizationBase  Parameters ---------- id : UUID     Localization id broker_alert_id : UUID     ID of the alert associated with this localization broker_event_id: UUID     ID of the event associated with this localization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra** | **float** |  | [optional] 
**dec** | **float** |  | [optional] 
**contours** | [**List[LocalizationContourBase]**](LocalizationContourBase.md) |  | [optional] 
**probability_enclosed** | **float** |  | [optional] 
**id** | **str** |  | 
**broker_event_id** | **str** |  | 
**broker_alert_id** | **str** |  | 

## Example

```python
from across.sdk.v1.models.localization import Localization

# TODO update the JSON string below
json = "{}"
# create an instance of Localization from a JSON string
localization_instance = Localization.from_json(json)
# print the JSON string representation of the object
print(Localization.to_json())

# convert the object into a dict
localization_dict = localization_instance.to_dict()
# create an instance of Localization from a dict
localization_from_dict = Localization.from_dict(localization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


