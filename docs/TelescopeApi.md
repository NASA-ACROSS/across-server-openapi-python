# across.sdk.v1.TelescopeApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_telescope**](TelescopeApi.md#get_telescope) | **GET** /telescope/{telescope_id} | Read an telescope
[**get_telescopes**](TelescopeApi.md#get_telescopes) | **GET** /telescope/ | Read telescopes(s)


# **get_telescope**
> Telescope get_telescope(telescope_id)

Read an telescope

Read a telescope by a telescope ID.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.telescope import Telescope
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.TelescopeApi(api_client)
    telescope_id = 'telescope_id_example' # str | 

    try:
        # Read an telescope
        api_response = api_instance.get_telescope(telescope_id)
        print("The response of TelescopeApi->get_telescope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelescopeApi->get_telescope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telescope_id** | **str**|  | 

### Return type

[**Telescope**](Telescope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a Telescope |  -  |
**404** | Telescope not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telescopes**
> List[Telescope] get_telescopes(name=name, instrument_id=instrument_id, instrument_name=instrument_name, created_on=created_on, include_filters=include_filters, include_footprints=include_footprints)

Read telescopes(s)

Read most recent telescopes based on query params

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.telescope import Telescope
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.TelescopeApi(api_client)
    name = 'name_example' # str |  (optional)
    instrument_id = 'instrument_id_example' # str |  (optional)
    instrument_name = 'instrument_name_example' # str |  (optional)
    created_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    include_filters = False # bool |  (optional) (default to False)
    include_footprints = False # bool |  (optional) (default to False)

    try:
        # Read telescopes(s)
        api_response = api_instance.get_telescopes(name=name, instrument_id=instrument_id, instrument_name=instrument_name, created_on=created_on, include_filters=include_filters, include_footprints=include_footprints)
        print("The response of TelescopeApi->get_telescopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TelescopeApi->get_telescopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **instrument_id** | **str**|  | [optional] 
 **instrument_name** | **str**|  | [optional] 
 **created_on** | **datetime**|  | [optional] 
 **include_filters** | **bool**|  | [optional] [default to False]
 **include_footprints** | **bool**|  | [optional] [default to False]

### Return type

[**List[Telescope]**](Telescope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a telescope |  -  |
**404** | The telescope does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

