# SPICEParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**naif_id** | **int** |  | 
**spice_kernel_url** | **str** |  | 

## Example

```python
from across/sdk.models.spice_parameters import SPICEParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SPICEParameters from a JSON string
spice_parameters_instance = SPICEParameters.from_json(json)
# print the JSON string representation of the object
print(SPICEParameters.to_json())

# convert the object into a dict
spice_parameters_dict = spice_parameters_instance.to_dict()
# create an instance of SPICEParameters from a dict
spice_parameters_from_dict = SPICEParameters.from_dict(spice_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


