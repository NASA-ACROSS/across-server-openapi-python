# BrokerAlert

A Pydantic model class representing a BrokerAlert in the ACROSS system.  Parameters ---------- id : UUID     Broker alert id status : BrokerAlertStatus     Status of the alert broker_name : str     Name of the broker issuing the alert data_source : BrokerAlertDataSource     Source of the alert external_event_id: str     External name of the BrokerEvent associated with this alert broker_event_id: uuid     ID of the associated BrokerEvent in the ACROSS system broker_received_on: datetime     Datetime the broker received this alert payload: dict     The alert payload, containing unstructured data about the event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**BrokerAlertStatus**](BrokerAlertStatus.md) |  | 
**broker_name** | **str** |  | 
**data_source** | [**BrokerAlertDataSource**](BrokerAlertDataSource.md) |  | 
**external_event_id** | **str** |  | 
**broker_event_id** | **str** |  | 
**broker_received_on** | **datetime** |  | 
**payload** | **Dict[str, object]** |  | 

## Example

```python
from across.sdk.v1.models.broker_alert import BrokerAlert

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerAlert from a JSON string
broker_alert_instance = BrokerAlert.from_json(json)
# print the JSON string representation of the object
print(BrokerAlert.to_json())

# convert the object into a dict
broker_alert_dict = broker_alert_instance.to_dict()
# create an instance of BrokerAlert from a dict
broker_alert_from_dict = BrokerAlert.from_dict(broker_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


