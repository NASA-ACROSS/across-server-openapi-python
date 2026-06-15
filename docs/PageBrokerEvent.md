# PageBrokerEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_number** | **int** |  | 
**page** | **int** |  | 
**page_limit** | **int** |  | 
**items** | [**List[BrokerEvent]**](BrokerEvent.md) |  | 

## Example

```python
from across.sdk.v1.models.page_broker_event import PageBrokerEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PageBrokerEvent from a JSON string
page_broker_event_instance = PageBrokerEvent.from_json(json)
# print the JSON string representation of the object
print(PageBrokerEvent.to_json())

# convert the object into a dict
page_broker_event_dict = page_broker_event_instance.to_dict()
# create an instance of PageBrokerEvent from a dict
page_broker_event_from_dict = PageBrokerEvent.from_dict(page_broker_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


