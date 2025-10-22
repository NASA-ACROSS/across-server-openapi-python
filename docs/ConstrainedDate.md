# ConstrainedDate

Represents a constrained date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **datetime** |  | 
**constraint** | [**ConstraintType**](ConstraintType.md) |  | 
**observatory_id** | **str** |  | 

## Example

```python
from across.sdk.v1.models.constrained_date import ConstrainedDate

# TODO update the JSON string below
json = "{}"
# create an instance of ConstrainedDate from a JSON string
constrained_date_instance = ConstrainedDate.from_json(json)
# print the JSON string representation of the object
print(ConstrainedDate.to_json())

# convert the object into a dict
constrained_date_dict = constrained_date_instance.to_dict()
# create an instance of ConstrainedDate from a dict
constrained_date_from_dict = ConstrainedDate.from_dict(constrained_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


