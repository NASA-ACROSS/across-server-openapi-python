# SystemServiceAccountSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**expiration** | **datetime** |  | 
**expiration_duration** | **int** |  | 
**roles** | [**List[RoleBase]**](RoleBase.md) |  | 
**group_roles** | [**List[GroupRoleRead]**](GroupRoleRead.md) |  | 
**secret_key** | **str** |  | 

## Example

```python
from across.sdk.v1.models.system_service_account_secret import SystemServiceAccountSecret

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceAccountSecret from a JSON string
system_service_account_secret_instance = SystemServiceAccountSecret.from_json(json)
# print the JSON string representation of the object
print(SystemServiceAccountSecret.to_json())

# convert the object into a dict
system_service_account_secret_dict = system_service_account_secret_instance.to_dict()
# create an instance of SystemServiceAccountSecret from a dict
system_service_account_secret_from_dict = SystemServiceAccountSecret.from_dict(system_service_account_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


