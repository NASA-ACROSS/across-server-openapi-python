# across.sdk.v1.InstrumentApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_instrument**](InstrumentApi.md#get_instrument) | **GET** /instrument/{instrument_id} | Read an instrument
[**get_instruments**](InstrumentApi.md#get_instruments) | **GET** /instrument/ | Read instruments(s)


# **get_instrument**
> Instrument get_instrument(instrument_id)

Read an instrument

Read an instrument by a instrument ID.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.instrument import Instrument
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
    api_instance = across.sdk.v1.InstrumentApi(api_client)
    instrument_id = 'instrument_id_example' # str | 

    try:
        # Read an instrument
        api_response = api_instance.get_instrument(instrument_id)
        print("The response of InstrumentApi->get_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->get_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **str**|  | 

### Return type

[**Instrument**](Instrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return an Instrument |  -  |
**404** | Instrument not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instruments**
> List[Instrument] get_instruments(name=name, telescope_id=telescope_id, telescope_name=telescope_name, created_on=created_on)

Read instruments(s)

Read many instruments based on query params

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.instrument import Instrument
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
    api_instance = across.sdk.v1.InstrumentApi(api_client)
    name = 'name_example' # str |  (optional)
    telescope_id = 'telescope_id_example' # str |  (optional)
    telescope_name = 'telescope_name_example' # str |  (optional)
    created_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Read instruments(s)
        api_response = api_instance.get_instruments(name=name, telescope_id=telescope_id, telescope_name=telescope_name, created_on=created_on)
        print("The response of InstrumentApi->get_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->get_instruments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **telescope_id** | **str**|  | [optional] 
 **telescope_name** | **str**|  | [optional] 
 **created_on** | **datetime**|  | [optional] 

### Return type

[**List[Instrument]**](Instrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return an instrument |  -  |
**404** | The instrument does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

