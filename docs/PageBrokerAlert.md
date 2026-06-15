# PageBrokerAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_number** | **int** |  | 
**page** | **int** |  | 
**page_limit** | **int** |  | 
**items** | [**List[BrokerAlert]**](BrokerAlert.md) |  | 

## Example

```python
from across.sdk.v1.models.page_broker_alert import PageBrokerAlert

# TODO update the JSON string below
json = "{}"
# create an instance of PageBrokerAlert from a JSON string
page_broker_alert_instance = PageBrokerAlert.from_json(json)
# print the JSON string representation of the object
print(PageBrokerAlert.to_json())

# convert the object into a dict
page_broker_alert_dict = page_broker_alert_instance.to_dict()
# create an instance of PageBrokerAlert from a dict
page_broker_alert_from_dict = PageBrokerAlert.from_dict(page_broker_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


