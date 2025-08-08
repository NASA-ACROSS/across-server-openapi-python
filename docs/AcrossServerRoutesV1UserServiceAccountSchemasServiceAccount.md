# AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**expiration** | **datetime** |  | 
**expiration_duration** | **int** |  | 
**group_roles** | [**List[AcrossServerRoutesV1UserSchemasGroupRole]**](AcrossServerRoutesV1UserSchemasGroupRole.md) |  | 

## Example

```python
from across/sdk.models.across_server_routes_v1_user_service_account_schemas_service_account import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount from a JSON string
across_server_routes_v1_user_service_account_schemas_service_account_instance = AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.to_json())

# convert the object into a dict
across_server_routes_v1_user_service_account_schemas_service_account_dict = across_server_routes_v1_user_service_account_schemas_service_account_instance.to_dict()
# create an instance of AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount from a dict
across_server_routes_v1_user_service_account_schemas_service_account_from_dict = AcrossServerRoutesV1UserServiceAccountSchemasServiceAccount.from_dict(across_server_routes_v1_user_service_account_schemas_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


