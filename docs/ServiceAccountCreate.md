# ServiceAccountCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**expiration_duration** | **int** |  | 

## Example

```python
from across.sdk.v1.models.service_account_create import ServiceAccountCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountCreate from a JSON string
service_account_create_instance = ServiceAccountCreate.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountCreate.to_json())

# convert the object into a dict
service_account_create_dict = service_account_create_instance.to_dict()
# create an instance of ServiceAccountCreate from a dict
service_account_create_from_dict = ServiceAccountCreate.from_dict(service_account_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


