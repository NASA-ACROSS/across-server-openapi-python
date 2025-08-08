# IDNameSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 

## Example

```python
from across/sdk.models.id_name_schema import IDNameSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IDNameSchema from a JSON string
id_name_schema_instance = IDNameSchema.from_json(json)
# print the JSON string representation of the object
print(IDNameSchema.to_json())

# convert the object into a dict
id_name_schema_dict = id_name_schema_instance.to_dict()
# create an instance of IDNameSchema from a dict
id_name_schema_from_dict = IDNameSchema.from_dict(id_name_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


