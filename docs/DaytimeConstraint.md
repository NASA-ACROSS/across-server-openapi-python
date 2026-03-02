# DaytimeConstraint

Constraint that avoids daytime observations based on twilight definitions.  For ground-based telescopes, daytime is defined by the Sun's position relative to the horizon. Different twilight types provide different levels of darkness.  For space-based telescopes, daytime refers to periods when the spacecraft is in direct sunlight (requires appropriate ephemeris data).  The telescope type (ground vs space) is automatically detected based on the ephemeris type: GroundEphemeris for ground-based, all others for space-based.  Parameters ---------- twilight_type : TwilightType     The type of twilight to use for defining daytime boundaries.     - 'astronomical': Sun 12-18° below horizon (default)     - 'nautical': Sun 6-12° below horizon     - 'civil': Sun 0-6° below horizon     - 'day': Sun above horizon  Methods ------- __call__(time, ephemeris, coordinate)     Checks if the observation time qualifies as daytime for the given constraints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] [default to 'Daytime']
**name** | **str** |  | [optional] [default to 'Daytime Avoidance']
**twilight_type** | [**TwilightType**](TwilightType.md) | Type of twilight defining daytime boundaries | [optional] 

## Example

```python
from across.sdk.v1.models.daytime_constraint import DaytimeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of DaytimeConstraint from a JSON string
daytime_constraint_instance = DaytimeConstraint.from_json(json)
# print the JSON string representation of the object
print(DaytimeConstraint.to_json())

# convert the object into a dict
daytime_constraint_dict = daytime_constraint_instance.to_dict()
# create an instance of DaytimeConstraint from a dict
daytime_constraint_from_dict = DaytimeConstraint.from_dict(daytime_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


