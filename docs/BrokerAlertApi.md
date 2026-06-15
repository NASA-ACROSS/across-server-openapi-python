# across.sdk.v1.BrokerAlertApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_broker_alert**](BrokerAlertApi.md#create_broker_alert) | **POST** /broker-alert/ | Create a BrokerAlert
[**get_broker_alert**](BrokerAlertApi.md#get_broker_alert) | **GET** /broker-alert/{broker_alert_id} | Read a broker alert
[**get_broker_alerts**](BrokerAlertApi.md#get_broker_alerts) | **GET** /broker-alert/ | Read broker alert(s)


# **create_broker_alert**
> str create_broker_alert(broker_alert_create)

Create a BrokerAlert

Create a new BrokerAlert and any new associated BrokerEvent or Localization records.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.broker_alert_create import BrokerAlertCreate
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = across.sdk.v1.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with across.sdk.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = across.sdk.v1.BrokerAlertApi(api_client)
    broker_alert_create = across.sdk.v1.BrokerAlertCreate() # BrokerAlertCreate | 

    try:
        # Create a BrokerAlert
        api_response = api_instance.create_broker_alert(broker_alert_create)
        print("The response of BrokerAlertApi->create_broker_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokerAlertApi->create_broker_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_alert_create** | [**BrokerAlertCreate**](BrokerAlertCreate.md)|  | 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created broker alert id |  -  |
**404** | The BrokerAlert does not exist. |  -  |
**409** | Duplicate broker alert |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_broker_alert**
> BrokerAlert get_broker_alert(broker_alert_id)

Read a broker alert

Read a broker alert by ID.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.broker_alert import BrokerAlert
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
    api_instance = across.sdk.v1.BrokerAlertApi(api_client)
    broker_alert_id = 'broker_alert_id_example' # str | 

    try:
        # Read a broker alert
        api_response = api_instance.get_broker_alert(broker_alert_id)
        print("The response of BrokerAlertApi->get_broker_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokerAlertApi->get_broker_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broker_alert_id** | **str**|  | 

### Return type

[**BrokerAlert**](BrokerAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a BrokerAlert |  -  |
**404** | BrokerAlert not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_broker_alerts**
> PageBrokerAlert get_broker_alerts(page=page, page_limit=page_limit, status=status, broker_name=broker_name, data_source=data_source, external_event_id=external_event_id, broker_event_id=broker_event_id, broker_received_before=broker_received_before, broker_received_after=broker_received_after)

Read broker alert(s)

Read many broker alerts based on query params

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.broker_alert_data_source import BrokerAlertDataSource
from across.sdk.v1.models.broker_alert_status import BrokerAlertStatus
from across.sdk.v1.models.page_broker_alert import PageBrokerAlert
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
    api_instance = across.sdk.v1.BrokerAlertApi(api_client)
    page = 56 # int | Page number (optional)
    page_limit = 56 # int | Records per page (optional)
    status = [across.sdk.v1.BrokerAlertStatus()] # List[BrokerAlertStatus] |  (optional)
    broker_name = 'broker_name_example' # str |  (optional)
    data_source = [across.sdk.v1.BrokerAlertDataSource()] # List[BrokerAlertDataSource] |  (optional)
    external_event_id = 'external_event_id_example' # str |  (optional)
    broker_event_id = 'broker_event_id_example' # str |  (optional)
    broker_received_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    broker_received_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Read broker alert(s)
        api_response = api_instance.get_broker_alerts(page=page, page_limit=page_limit, status=status, broker_name=broker_name, data_source=data_source, external_event_id=external_event_id, broker_event_id=broker_event_id, broker_received_before=broker_received_before, broker_received_after=broker_received_after)
        print("The response of BrokerAlertApi->get_broker_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrokerAlertApi->get_broker_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **page_limit** | **int**| Records per page | [optional] 
 **status** | [**List[BrokerAlertStatus]**](BrokerAlertStatus.md)|  | [optional] 
 **broker_name** | **str**|  | [optional] 
 **data_source** | [**List[BrokerAlertDataSource]**](BrokerAlertDataSource.md)|  | [optional] 
 **external_event_id** | **str**|  | [optional] 
 **broker_event_id** | **str**|  | [optional] 
 **broker_received_before** | **datetime**|  | [optional] 
 **broker_received_after** | **datetime**|  | [optional] 

### Return type

[**PageBrokerAlert**](PageBrokerAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return broker alerts |  -  |
**404** | The BrokerAlert does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

