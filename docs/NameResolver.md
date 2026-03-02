# NameResolver

Pydantic model class representing a resolved object name  Parameters ---------- ra: float     Right ascension coordinate, in degrees. dec: float     Declination coordinate, in degrees. resolver: str     Resolver used for resolving the coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra** | **float** |  | 
**dec** | **float** |  | 
**resolver** | **str** |  | 

## Example

```python
from across.sdk.v1.models.name_resolver import NameResolver

# TODO update the JSON string below
json = "{}"
# create an instance of NameResolver from a JSON string
name_resolver_instance = NameResolver.from_json(json)
# print the JSON string representation of the object
print(NameResolver.to_json())

# convert the object into a dict
name_resolver_dict = name_resolver_instance.to_dict()
# create an instance of NameResolver from a dict
name_resolver_from_dict = NameResolver.from_dict(name_resolver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


