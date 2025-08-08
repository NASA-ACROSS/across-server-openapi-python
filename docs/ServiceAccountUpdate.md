# ServiceAccountUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expiration_duration** | **int** |  | [optional] 

## Example

```python
from across.sdk.v1.models.service_account_update import ServiceAccountUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountUpdate from a JSON string
service_account_update_instance = ServiceAccountUpdate.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountUpdate.to_json())

# convert the object into a dict
service_account_update_dict = service_account_update_instance.to_dict()
# create an instance of ServiceAccountUpdate from a dict
service_account_update_from_dict = ServiceAccountUpdate.from_dict(service_account_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


