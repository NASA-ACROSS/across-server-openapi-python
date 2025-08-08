# AcrossServerRoutesV1UserServiceAccountSchemasServiceAccountSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**expiration** | **datetime** |  | 
**expiration_duration** | **int** |  | 
**group_roles** | [**List[AcrossServerRoutesV1UserSchemasGroupRole]**](AcrossServerRoutesV1UserSchemasGroupRole.md) |  | 
**secret_key** | **str** |  | [optional] 

## Example

```python
from across.sdk.v1.models.across_server_routes_v1_user_service_account_schemas_service_account_secret import AcrossServerRoutesV1UserServiceAccountSchemasServiceAccountSecret

# TODO update the JSON string below
json = "{}"
# create an instance of AcrossServerRoutesV1UserServiceAccountSchemasServiceAccountSecret from a JSON string
across_server_routes_v1_user_service_account_schemas_service_account_secret_instance = AcrossServerRoutesV1UserServiceAccountSchemasServiceAccountSecret.from_json(json)
# print the JSON string representation of the object
print(AcrossServerRoutesV1UserServiceAccountSchemasServiceAccountSecret.to_json())

# convert the object into a dict
across_server_routes_v1_user_service_account_schemas_service_account_secret_dict = across_server_routes_v1_user_service_account_schemas_service_account_secret_instance.to_dict()
# create an instance of AcrossServerRoutesV1UserServiceAccountSchemasServiceAccountSecret from a dict
across_server_routes_v1_user_service_account_schemas_service_account_secret_from_dict = AcrossServerRoutesV1UserServiceAccountSchemasServiceAccountSecret.from_dict(across_server_routes_v1_user_service_account_schemas_service_account_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


