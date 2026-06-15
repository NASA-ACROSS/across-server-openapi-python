# BrokerEvent

A Pydantic model class representing a BrokerEvent in the ACROSS system.  Parameters ---------- localizations : list[Localization]     Localizations associated with this event alerts : list[BrokerAlert]     Alerts associated with this event  Methods -------- from_orm:     Converts ORM BrokerEvent model to a schemas.BrokerEvent object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**event_datetime** | **datetime** |  | 
**type** | [**BrokerEventType**](BrokerEventType.md) |  | 
**name** | **str** |  | 
**localizations** | [**List[Localization]**](Localization.md) |  | 
**broker_alerts** | [**List[BrokerAlert]**](BrokerAlert.md) |  | 

## Example

```python
from across.sdk.v1.models.broker_event import BrokerEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerEvent from a JSON string
broker_event_instance = BrokerEvent.from_json(json)
# print the JSON string representation of the object
print(BrokerEvent.to_json())

# convert the object into a dict
broker_event_dict = broker_event_instance.to_dict()
# create an instance of BrokerEvent from a dict
broker_event_from_dict = BrokerEvent.from_dict(broker_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


