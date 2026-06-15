# across.sdk.v1.BrokerEventApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_broker_event**](BrokerEventApi.md#get_broker_event) | **GET** /broker-event/{broker_event_id} | Read a broker event
[**get_broker_events**](BrokerEventApi.md#get_broker_events) | **GET** /broker-event/ | Read broker event(s)


# **get_broker_event**
> BrokerEvent get_broker_event(broker_event_id)

Read a broker event

Read a broker event by ID.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.broker_event import BrokerEvent
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.BrokerEventApi(api_client)
    broker_event_id = 'broker_event_id_example' # str | 

    try:
        # Read a broker event
        api_response = api_instance.get_broker_event(broker_event_id)
        print("The response of BrokerEventApi->get_broker_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokerEventApi->get_broker_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_event_id** | **str**|  | 

### Return type

[**BrokerEvent**](BrokerEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a BrokerEvent |  -  |
**404** | BrokerEvent not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_broker_events**
> PageBrokerEvent get_broker_events(page=page, page_limit=page_limit, type=type, name=name, date_range_begin=date_range_begin, date_range_end=date_range_end, include_localizations=include_localizations)

Read broker event(s)

Read many broker events based on query params

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.broker_event_type import BrokerEventType
from across.sdk.v1.models.page_broker_event import PageBrokerEvent
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.BrokerEventApi(api_client)
    page = 56 # int | Page number (optional)
    page_limit = 56 # int | Records per page (optional)
    type = [across.sdk.v1.BrokerEventType()] # List[BrokerEventType] |  (optional)
    name = 'name_example' # str |  (optional)
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    include_localizations = False # bool |  (optional) (default to False)

    try:
        # Read broker event(s)
        api_response = api_instance.get_broker_events(page=page, page_limit=page_limit, type=type, name=name, date_range_begin=date_range_begin, date_range_end=date_range_end, include_localizations=include_localizations)
        print("The response of BrokerEventApi->get_broker_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokerEventApi->get_broker_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **page_limit** | **int**| Records per page | [optional] 
 **type** | [**List[BrokerEventType]**](BrokerEventType.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **date_range_begin** | **datetime**|  | [optional] 
 **date_range_end** | **datetime**|  | [optional] 
 **include_localizations** | **bool**|  | [optional] [default to False]

### Return type

[**PageBrokerEvent**](PageBrokerEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return broker events |  -  |
**404** | The BrokerEvent does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

