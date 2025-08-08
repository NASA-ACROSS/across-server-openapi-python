# across/sdk.FilterApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filter_filter_id_get**](FilterApi.md#get_filter_filter_id_get) | **GET** /filter/{filter_id} | Read a filter
[**get_many_filter_get**](FilterApi.md#get_many_filter_get) | **GET** /filter/ | Read filters(s)


# **get_filter_filter_id_get**
> Filter get_filter_filter_id_get(filter_id)

Read a filter

Read a filter by a filter ID.

### Example


```python
import across/sdk
from across/sdk.models.filter import Filter
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
    api_instance = across/sdk.FilterApi(api_client)
    filter_id = 'filter_id_example' # str | 

    try:
        # Read a filter
        api_response = api_instance.get_filter_filter_id_get(filter_id)
        print("The response of FilterApi->get_filter_filter_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->get_filter_filter_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**|  | 

### Return type

[**Filter**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a filter |  -  |
**404** | filter not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_many_filter_get**
> List[Filter] get_many_filter_get(name=name, instrument_id=instrument_id, instrument_name=instrument_name, covers_wavelength=covers_wavelength)

Read filters(s)

Read many filters based on query params

### Example


```python
import across/sdk
from across/sdk.models.filter import Filter
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
    api_instance = across/sdk.FilterApi(api_client)
    name = 'name_example' # str |  (optional)
    instrument_id = 'instrument_id_example' # str |  (optional)
    instrument_name = 'instrument_name_example' # str |  (optional)
    covers_wavelength = 3.4 # float |  (optional)

    try:
        # Read filters(s)
        api_response = api_instance.get_many_filter_get(name=name, instrument_id=instrument_id, instrument_name=instrument_name, covers_wavelength=covers_wavelength)
        print("The response of FilterApi->get_many_filter_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterApi->get_many_filter_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **instrument_id** | **str**|  | [optional] 
 **instrument_name** | **str**|  | [optional] 
 **covers_wavelength** | **float**|  | [optional] 

### Return type

[**List[Filter]**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a filter |  -  |
**404** | The filter does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

