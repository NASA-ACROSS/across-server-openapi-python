# ConstraintReason

Represents the reasons for constraints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_reason** | **str** |  | 
**end_reason** | **str** |  | 

## Example

```python
from across.sdk.v1.models.constraint_reason import ConstraintReason

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintReason from a JSON string
constraint_reason_instance = ConstraintReason.from_json(json)
# print the JSON string representation of the object
print(ConstraintReason.to_json())

# convert the object into a dict
constraint_reason_dict = constraint_reason_instance.to_dict()
# create an instance of ConstraintReason from a dict
constraint_reason_from_dict = ConstraintReason.from_dict(constraint_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


