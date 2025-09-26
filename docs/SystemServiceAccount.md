# SystemServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**expiration** | **datetime** |  | 
**expiration_duration** | **int** |  | 
**roles** | [**List[RoleBase]**](RoleBase.md) |  | [optional] [default to []]
**group_roles** | [**List[GroupRoleRead]**](GroupRoleRead.md) |  | [optional] [default to []]

## Example

```python
from across.sdk.v1.models.system_service_account import SystemServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceAccount from a JSON string
system_service_account_instance = SystemServiceAccount.from_json(json)
# print the JSON string representation of the object
print(SystemServiceAccount.to_json())

# convert the object into a dict
system_service_account_dict = system_service_account_instance.to_dict()
# create an instance of SystemServiceAccount from a dict
system_service_account_from_dict = SystemServiceAccount.from_dict(system_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


