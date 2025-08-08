# across/sdk.ObservationApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_observation**](ObservationApi.md#get_observation) | **GET** /observation/{observation_id} | Read an observation
[**get_observations**](ObservationApi.md#get_observations) | **GET** /observation/ | Read observations(s)


# **get_observation**
> Observation get_observation(observation_id)

Read an observation

Read an observation by an observation ID.

### Example


```python
import across/sdk
from across/sdk.models.observation import Observation
from across/sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across/sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with across/sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across/sdk.ObservationApi(api_client)
    observation_id = 'observation_id_example' # str | 

    try:
        # Read an observation
        api_response = api_instance.get_observation(observation_id)
        print("The response of ObservationApi->get_observation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationApi->get_observation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_id** | **str**|  | 

### Return type

[**Observation**](Observation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return an observation |  -  |
**404** | Observation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observations**
> List[Observation] get_observations(external_id=external_id, schedule_ids=schedule_ids, observatory_ids=observatory_ids, telescope_ids=telescope_ids, instrument_ids=instrument_ids, status=status, proposal=proposal, object_name=object_name, date_range_begin=date_range_begin, date_range_end=date_range_end, bandpass_min=bandpass_min, bandpass_max=bandpass_max, bandpass_type=bandpass_type, cone_search_ra=cone_search_ra, cone_search_dec=cone_search_dec, cone_search_radius=cone_search_radius, type=type, depth_value=depth_value, depth_unit=depth_unit)

Read observations(s)

Read the observations based on query params

### Example


```python
import across/sdk
from across/sdk.models.depth_unit import DepthUnit
from across/sdk.models.observation import Observation
from across/sdk.models.observation_status import ObservationStatus
from across/sdk.models.observation_type import ObservationType
from across/sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across/sdk.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with across/sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across/sdk.ObservationApi(api_client)
    external_id = 'external_id_example' # str |  (optional)
    schedule_ids = ['schedule_ids_example'] # List[Optional[str]] |  (optional)
    observatory_ids = ['observatory_ids_example'] # List[str] |  (optional)
    telescope_ids = ['telescope_ids_example'] # List[str] |  (optional)
    instrument_ids = ['instrument_ids_example'] # List[str] |  (optional)
    status = across/sdk.ObservationStatus() # ObservationStatus |  (optional)
    proposal = 'proposal_example' # str |  (optional)
    object_name = 'object_name_example' # str |  (optional)
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    bandpass_min = 3.4 # float |  (optional)
    bandpass_max = 3.4 # float |  (optional)
    bandpass_type = across/sdk.BandpassType() # BandpassType |  (optional)
    cone_search_ra = 3.4 # float |  (optional)
    cone_search_dec = 3.4 # float |  (optional)
    cone_search_radius = 3.4 # float |  (optional)
    type = across/sdk.ObservationType() # ObservationType |  (optional)
    depth_value = 3.4 # float |  (optional)
    depth_unit = across/sdk.DepthUnit() # DepthUnit |  (optional)

    try:
        # Read observations(s)
        api_response = api_instance.get_observations(external_id=external_id, schedule_ids=schedule_ids, observatory_ids=observatory_ids, telescope_ids=telescope_ids, instrument_ids=instrument_ids, status=status, proposal=proposal, object_name=object_name, date_range_begin=date_range_begin, date_range_end=date_range_end, bandpass_min=bandpass_min, bandpass_max=bandpass_max, bandpass_type=bandpass_type, cone_search_ra=cone_search_ra, cone_search_dec=cone_search_dec, cone_search_radius=cone_search_radius, type=type, depth_value=depth_value, depth_unit=depth_unit)
        print("The response of ObservationApi->get_observations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationApi->get_observations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | [optional] 
 **schedule_ids** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **observatory_ids** | [**List[str]**](str.md)|  | [optional] 
 **telescope_ids** | [**List[str]**](str.md)|  | [optional] 
 **instrument_ids** | [**List[str]**](str.md)|  | [optional] 
 **status** | [**ObservationStatus**](.md)|  | [optional] 
 **proposal** | **str**|  | [optional] 
 **object_name** | **str**|  | [optional] 
 **date_range_begin** | **datetime**|  | [optional] 
 **date_range_end** | **datetime**|  | [optional] 
 **bandpass_min** | **float**|  | [optional] 
 **bandpass_max** | **float**|  | [optional] 
 **bandpass_type** | [**BandpassType**](.md)|  | [optional] 
 **cone_search_ra** | **float**|  | [optional] 
 **cone_search_dec** | **float**|  | [optional] 
 **cone_search_radius** | **float**|  | [optional] 
 **type** | [**ObservationType**](.md)|  | [optional] 
 **depth_value** | **float**|  | [optional] 
 **depth_unit** | [**DepthUnit**](.md)|  | [optional] 

### Return type

[**List[Observation]**](Observation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a list of observations |  -  |
**404** | The observation does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

