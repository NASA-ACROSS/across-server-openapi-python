# JointVisibilityResult

A Pydantic model class representing the joint visibility calculation parameters.  This class is used for joint visibility calculations in the ACROSS SSA system.  Parameters ---------- instrument_ids: list[UUID]     List of instrument IDs to check visibility against visibility_windows: list[VisibilityWindow]     List of joint visibility windows for all the instruments observatory_visibility_windows: dict[UUID, list[VisibilityWindow]]     Dictionary mapping instrument IDs to their respective visibility windows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_ids** | **List[str]** |  | 
**visibility_windows** | [**List[VisibilityWindow]**](VisibilityWindow.md) |  | 
**observatory_visibility_windows** | **Dict[str, List[VisibilityWindow]]** |  | 

## Example

```python
from across.sdk.v1.models.joint_visibility_result import JointVisibilityResult

# TODO update the JSON string below
json = "{}"
# create an instance of JointVisibilityResult from a JSON string
joint_visibility_result_instance = JointVisibilityResult.from_json(json)
# print the JSON string representation of the object
print(JointVisibilityResult.to_json())

# convert the object into a dict
joint_visibility_result_dict = joint_visibility_result_instance.to_dict()
# create an instance of JointVisibilityResult from a dict
joint_visibility_result_from_dict = JointVisibilityResult.from_dict(joint_visibility_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


