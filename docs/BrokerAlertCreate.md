# BrokerAlertCreate

A Pydantic model class representing a BrokerEvent to be created in the ACROSS system.  Parameters ---------- broker_event_datetime : datetime     Datetime the associated broker event was discovered or detected broker_event_type : BrokerEventType     Astrophysical type or classification of the broker event broker_event_name : str     Name of the broker event localization: Localization     Localization of the event from this alert  Methods to_orm(self) -> BrokerAlertModel     Method that creates the ORM record for a broker alert to be serialized into the database.     This method does not instantiate the associated broker event or localization;     these records are created within the broker alert service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**BrokerAlertStatus**](BrokerAlertStatus.md) |  | 
**broker_name** | **str** |  | 
**data_source** | [**BrokerAlertDataSource**](BrokerAlertDataSource.md) |  | 
**broker_received_on** | **datetime** |  | 
**payload** | **Dict[str, object]** |  | 
**broker_event_datetime** | **datetime** |  | 
**broker_event_type** | [**BrokerEventType**](BrokerEventType.md) |  | 
**broker_event_name** | **str** |  | 
**localizations** | [**List[LocalizationCreate]**](LocalizationCreate.md) |  | 

## Example

```python
from across.sdk.v1.models.broker_alert_create import BrokerAlertCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerAlertCreate from a JSON string
broker_alert_create_instance = BrokerAlertCreate.from_json(json)
# print the JSON string representation of the object
print(BrokerAlertCreate.to_json())

# convert the object into a dict
broker_alert_create_dict = broker_alert_create_instance.to_dict()
# create an instance of BrokerAlertCreate from a dict
broker_alert_create_from_dict = BrokerAlertCreate.from_dict(broker_alert_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


