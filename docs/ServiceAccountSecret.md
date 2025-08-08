# ServiceAccountSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**expiration** | **datetime** |  | 
**expiration_duration** | **int** |  | 
**group_roles** | [**List[GroupRoleRead]**](GroupRoleRead.md) |  | 
**secret_key** | **str** |  | [optional] 

## Example

```python
from across.sdk.v1.models.service_account_secret import ServiceAccountSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountSecret from a JSON string
service_account_secret_instance = ServiceAccountSecret.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountSecret.to_json())

# convert the object into a dict
service_account_secret_dict = service_account_secret_instance.to_dict()
# create an instance of ServiceAccountSecret from a dict
service_account_secret_from_dict = ServiceAccountSecret.from_dict(service_account_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


