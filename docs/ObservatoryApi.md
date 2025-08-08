# across/sdk.ObservatoryApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_observatories**](ObservatoryApi.md#get_observatories) | **GET** /observatory/ | Read observatory(s)
[**get_observatory**](ObservatoryApi.md#get_observatory) | **GET** /observatory/{observatory_id} | Read an observatory


# **get_observatories**
> List[Observatory] get_observatories(name=name, type=type, telescope_name=telescope_name, telescope_id=telescope_id, ephemeris_type=ephemeris_type, created_on=created_on)

Read observatory(s)

Read many observatories based on query params

### Example


```python
import across/sdk
from across/sdk.models.ephemeris_type import EphemerisType
from across/sdk.models.observatory import Observatory
from across/sdk.models.observatory_type import ObservatoryType
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
    api_instance = across/sdk.ObservatoryApi(api_client)
    name = 'name_example' # str |  (optional)
    type = across/sdk.ObservatoryType() # ObservatoryType |  (optional)
    telescope_name = 'telescope_name_example' # str |  (optional)
    telescope_id = 'telescope_id_example' # str |  (optional)
    ephemeris_type = [across/sdk.EphemerisType()] # List[EphemerisType] |  (optional)
    created_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Read observatory(s)
        api_response = api_instance.get_observatories(name=name, type=type, telescope_name=telescope_name, telescope_id=telescope_id, ephemeris_type=ephemeris_type, created_on=created_on)
        print("The response of ObservatoryApi->get_observatories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservatoryApi->get_observatories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **type** | [**ObservatoryType**](.md)|  | [optional] 
 **telescope_name** | **str**|  | [optional] 
 **telescope_id** | **str**|  | [optional] 
 **ephemeris_type** | [**List[EphemerisType]**](EphemerisType.md)|  | [optional] 
 **created_on** | **datetime**|  | [optional] 

### Return type

[**List[Observatory]**](Observatory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a observatory |  -  |
**404** | The observatory does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observatory**
> Observatory get_observatory(observatory_id)

Read an observatory

Read a observatory by a observatory ID.

### Example


```python
import across/sdk
from across/sdk.models.observatory import Observatory
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
    api_instance = across/sdk.ObservatoryApi(api_client)
    observatory_id = 'observatory_id_example' # str | 

    try:
        # Read an observatory
        api_response = api_instance.get_observatory(observatory_id)
        print("The response of ObservatoryApi->get_observatory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservatoryApi->get_observatory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observatory_id** | **str**|  | 

### Return type

[**Observatory**](Observatory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a Observatory |  -  |
**404** | Observatory not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

