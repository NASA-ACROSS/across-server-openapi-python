# AirmassConstraint

Constraint based on airmass (zenith angle) for ground-based telescopes.  Airmass affects the quality of astronomical observations. Higher airmass means more atmospheric absorption and poorer image quality. This constraint ensures observations are conducted at acceptable airmass values.  Parameters ---------- max_air_mass : float     Maximum allowed airmass. Observations with higher airmass will be constrained.     Typical values: 1.5-2.0 for good quality, up to 3.0 for some surveys.  Methods ------- __call__(time, ephemeris, coordinate)     Checks if the airmass is too high for the given coordinate and time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Airmass']
**name** | **str** |  | [optional] [default to 'Airmass Limit']
**max_air_mass** | **float** | Maximum allowed airmass for observations | [optional] [default to 2.0]

## Example

```python
from across.sdk.v1.models.airmass_constraint import AirmassConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of AirmassConstraint from a JSON string
airmass_constraint_instance = AirmassConstraint.from_json(json)
# print the JSON string representation of the object
print(AirmassConstraint.to_json())

# convert the object into a dict
airmass_constraint_dict = airmass_constraint_instance.to_dict()
# create an instance of AirmassConstraint from a dict
airmass_constraint_from_dict = AirmassConstraint.from_dict(airmass_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


