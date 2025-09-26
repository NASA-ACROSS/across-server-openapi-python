# PageObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_number** | **int** |  | 
**page** | **int** |  | 
**page_limit** | **int** |  | 
**items** | [**List[Observation]**](Observation.md) |  | 

## Example

```python
from across.sdk.v1.models.page_observation import PageObservation

# TODO update the JSON string below
json = "{}"
# create an instance of PageObservation from a JSON string
page_observation_instance = PageObservation.from_json(json)
# print the JSON string representation of the object
print(PageObservation.to_json())

# convert the object into a dict
page_observation_dict = page_observation_instance.to_dict()
# create an instance of PageObservation from a dict
page_observation_from_dict = PageObservation.from_dict(page_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


