# ConstraintABC

Base class for constraints. Constraints represent conditions that make a target NOT visible (blocked from observation). A constraint returns True when the target is constrained (NOT visible) and False when the target is visible.  When combining multiple constraints, the typical approach in visibility calculations is to use OR logic: the target is not visible if ANY constraint blocks it. AND and NOT logic are provided but are rarely used in practice.  Constraints can be combined using logical operators: - | (OR): Combined constraint violated if ANY sub-constraint is violated (typical usage) - & (AND): Combined constraint violated only if ALL sub-constraints are violated (rarely used) - ~ (NOT): Inverts the constraint's logic (rarely used) - ^ (XOR): Combined constraint violated when an odd number of sub-constraints are violated (rarely used)  Methods ------- __call__(time, ephemeris, coord)     Evaluates if a given coordinate is constrained at the given time. __or__(other)     Combines two constraints with OR logic using the | operator (typical usage). __and__(other)     Combines two constraints with AND logic using the & operator. __invert__()     Negates a constraint using the ~ operator. __xor__(other)     Combines two constraints with XOR logic using the ^ operator.  Examples -------- Typical usage: combine constraints with OR (if any constraint blocks, target not visible):  >>> from across.tools.visibility.constraints import ( ...     SunAngleConstraint, MoonAngleConstraint, EarthLimbConstraint ... ) >>> sun = SunAngleConstraint(min_angle=45)      # Not visible if <45° from Sun >>> moon = MoonAngleConstraint(min_angle=10)    # Not visible if <10° from Moon >>> earth = EarthLimbConstraint(min_angle=33)   # Not visible if <33° above limb >>> # Target not visible if ANY constraint blocks it >>> all_constraints = sun | moon | earth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | 
**name** | [**ConstraintType**](ConstraintType.md) |  | 

## Example

```python
from across.sdk.v1.models.constraint_abc import ConstraintABC

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintABC from a JSON string
constraint_abc_instance = ConstraintABC.from_json(json)
# print the JSON string representation of the object
print(ConstraintABC.to_json())

# convert the object into a dict
constraint_abc_dict = constraint_abc_instance.to_dict()
# create an instance of ConstraintABC from a dict
constraint_abc_from_dict = ConstraintABC.from_dict(constraint_abc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


