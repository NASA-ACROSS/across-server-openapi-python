# across.sdk.v1.ToolsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_joint_windows_tools_visibility_calculator_windows_get**](ToolsApi.md#calculate_joint_windows_tools_visibility_calculator_windows_get) | **GET** /tools/visibility-calculator/windows/ | Calculated Joint Visibility Windows
[**calculate_joint_windows_tools_visibility_calculator_windows_get_0**](ToolsApi.md#calculate_joint_windows_tools_visibility_calculator_windows_get_0) | **GET** /tools/visibility-calculator/windows/ | Calculated Joint Visibility Windows
[**calculate_windows_tools_visibility_calculator_windows_instrument_id_get**](ToolsApi.md#calculate_windows_tools_visibility_calculator_windows_instrument_id_get) | **GET** /tools/visibility-calculator/windows/{instrument_id} | Calculated Visibility Windows
[**calculate_windows_tools_visibility_calculator_windows_instrument_id_get_0**](ToolsApi.md#calculate_windows_tools_visibility_calculator_windows_instrument_id_get_0) | **GET** /tools/visibility-calculator/windows/{instrument_id} | Calculated Visibility Windows


# **calculate_joint_windows_tools_visibility_calculator_windows_get**
> JointVisibilityResult calculate_joint_windows_tools_visibility_calculator_windows_get(ra, dec, date_range_begin, date_range_end, instrument_ids, hi_res=hi_res, min_visibility_duration=min_visibility_duration)

Calculated Joint Visibility Windows

Calculate joint visibility windows between instruments for a given observation coordinate 

 Use GET /telescope/ to retrieve a list of telescopes and their associated instruments 

 WARNING: This is a long running process and is liable to timeout after a strict 60 second execution limit 

 If you experience issues retrieving results, please scope your date range to be a smaller window or set `hi_res` to `false`

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.joint_visibility_result import JointVisibilityResult
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
    api_instance = across.sdk.v1.ToolsApi(api_client)
    ra = 3.4 # float | 
    dec = 3.4 # float | 
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime | 
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime | 
    instrument_ids = ['instrument_ids_example'] # List[Optional[str]] | 
    hi_res = True # bool |  (optional) (default to True)
    min_visibility_duration = 0 # int |  (optional) (default to 0)

    try:
        # Calculated Joint Visibility Windows
        api_response = api_instance.calculate_joint_windows_tools_visibility_calculator_windows_get(ra, dec, date_range_begin, date_range_end, instrument_ids, hi_res=hi_res, min_visibility_duration=min_visibility_duration)
        print("The response of ToolsApi->calculate_joint_windows_tools_visibility_calculator_windows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->calculate_joint_windows_tools_visibility_calculator_windows_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ra** | **float**|  | 
 **dec** | **float**|  | 
 **date_range_begin** | **datetime**|  | 
 **date_range_end** | **datetime**|  | 
 **instrument_ids** | [**List[Optional[str]]**](str.md)|  | 
 **hi_res** | **bool**|  | [optional] [default to True]
 **min_visibility_duration** | **int**|  | [optional] [default to 0]

### Return type

[**JointVisibilityResult**](JointVisibilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return joint visibility window calculation results. |  -  |
**404** | The visibility calculator does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_joint_windows_tools_visibility_calculator_windows_get_0**
> JointVisibilityResult calculate_joint_windows_tools_visibility_calculator_windows_get_0(ra, dec, date_range_begin, date_range_end, instrument_ids, hi_res=hi_res, min_visibility_duration=min_visibility_duration)

Calculated Joint Visibility Windows

Calculate joint visibility windows between instruments for a given observation coordinate 

 Use GET /telescope/ to retrieve a list of telescopes and their associated instruments 

 WARNING: This is a long running process and is liable to timeout after a strict 60 second execution limit 

 If you experience issues retrieving results, please scope your date range to be a smaller window or set `hi_res` to `false`

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.joint_visibility_result import JointVisibilityResult
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
    api_instance = across.sdk.v1.ToolsApi(api_client)
    ra = 3.4 # float | 
    dec = 3.4 # float | 
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime | 
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime | 
    instrument_ids = ['instrument_ids_example'] # List[Optional[str]] | 
    hi_res = True # bool |  (optional) (default to True)
    min_visibility_duration = 0 # int |  (optional) (default to 0)

    try:
        # Calculated Joint Visibility Windows
        api_response = api_instance.calculate_joint_windows_tools_visibility_calculator_windows_get_0(ra, dec, date_range_begin, date_range_end, instrument_ids, hi_res=hi_res, min_visibility_duration=min_visibility_duration)
        print("The response of ToolsApi->calculate_joint_windows_tools_visibility_calculator_windows_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->calculate_joint_windows_tools_visibility_calculator_windows_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ra** | **float**|  | 
 **dec** | **float**|  | 
 **date_range_begin** | **datetime**|  | 
 **date_range_end** | **datetime**|  | 
 **instrument_ids** | [**List[Optional[str]]**](str.md)|  | 
 **hi_res** | **bool**|  | [optional] [default to True]
 **min_visibility_duration** | **int**|  | [optional] [default to 0]

### Return type

[**JointVisibilityResult**](JointVisibilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return joint visibility window calculation results. |  -  |
**404** | The visibility calculator does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_windows_tools_visibility_calculator_windows_instrument_id_get**
> VisibilityResult calculate_windows_tools_visibility_calculator_windows_instrument_id_get(instrument_id, ra, dec, date_range_begin, date_range_end, hi_res=hi_res, min_visibility_duration=min_visibility_duration)

Calculated Visibility Windows

Calculate visibility windows of an instrument for a given observation coordinate 

 Use GET /telescope/ to retrieve a list of telescopes and their associated instruments 

 WARNING: This is a long running process and is liable to timeout after a strict 60 second execution limit 

 If you experience issues retrieving results, please scope your date range to be a smaller window or set `hi_res` to `false`

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.visibility_result import VisibilityResult
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
    api_instance = across.sdk.v1.ToolsApi(api_client)
    instrument_id = 'instrument_id_example' # str | 
    ra = 3.4 # float | 
    dec = 3.4 # float | 
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime | 
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime | 
    hi_res = True # bool |  (optional) (default to True)
    min_visibility_duration = 0 # int |  (optional) (default to 0)

    try:
        # Calculated Visibility Windows
        api_response = api_instance.calculate_windows_tools_visibility_calculator_windows_instrument_id_get(instrument_id, ra, dec, date_range_begin, date_range_end, hi_res=hi_res, min_visibility_duration=min_visibility_duration)
        print("The response of ToolsApi->calculate_windows_tools_visibility_calculator_windows_instrument_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->calculate_windows_tools_visibility_calculator_windows_instrument_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **str**|  | 
 **ra** | **float**|  | 
 **dec** | **float**|  | 
 **date_range_begin** | **datetime**|  | 
 **date_range_end** | **datetime**|  | 
 **hi_res** | **bool**|  | [optional] [default to True]
 **min_visibility_duration** | **int**|  | [optional] [default to 0]

### Return type

[**VisibilityResult**](VisibilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return visibility window calculation results. |  -  |
**404** | The visibility calculator does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_windows_tools_visibility_calculator_windows_instrument_id_get_0**
> VisibilityResult calculate_windows_tools_visibility_calculator_windows_instrument_id_get_0(instrument_id, ra, dec, date_range_begin, date_range_end, hi_res=hi_res, min_visibility_duration=min_visibility_duration)

Calculated Visibility Windows

Calculate visibility windows of an instrument for a given observation coordinate 

 Use GET /telescope/ to retrieve a list of telescopes and their associated instruments 

 WARNING: This is a long running process and is liable to timeout after a strict 60 second execution limit 

 If you experience issues retrieving results, please scope your date range to be a smaller window or set `hi_res` to `false`

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.visibility_result import VisibilityResult
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
    api_instance = across.sdk.v1.ToolsApi(api_client)
    instrument_id = 'instrument_id_example' # str | 
    ra = 3.4 # float | 
    dec = 3.4 # float | 
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime | 
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime | 
    hi_res = True # bool |  (optional) (default to True)
    min_visibility_duration = 0 # int |  (optional) (default to 0)

    try:
        # Calculated Visibility Windows
        api_response = api_instance.calculate_windows_tools_visibility_calculator_windows_instrument_id_get_0(instrument_id, ra, dec, date_range_begin, date_range_end, hi_res=hi_res, min_visibility_duration=min_visibility_duration)
        print("The response of ToolsApi->calculate_windows_tools_visibility_calculator_windows_instrument_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->calculate_windows_tools_visibility_calculator_windows_instrument_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_id** | **str**|  | 
 **ra** | **float**|  | 
 **dec** | **float**|  | 
 **date_range_begin** | **datetime**|  | 
 **date_range_end** | **datetime**|  | 
 **hi_res** | **bool**|  | [optional] [default to True]
 **min_visibility_duration** | **int**|  | [optional] [default to 0]

### Return type

[**VisibilityResult**](VisibilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return visibility window calculation results. |  -  |
**404** | The visibility calculator does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

