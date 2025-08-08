# across.sdk.v1.ScheduleApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_many_schedules**](ScheduleApi.md#create_many_schedules) | **POST** /schedule/bulk | Create many Schedules
[**create_schedule**](ScheduleApi.md#create_schedule) | **POST** /schedule/ | Create a Schedule
[**get_schedule**](ScheduleApi.md#get_schedule) | **GET** /schedule/{schedule_id} | Read a schedule
[**get_schedules**](ScheduleApi.md#get_schedules) | **GET** /schedule/ | Read schedule(s)
[**get_schedules_history**](ScheduleApi.md#get_schedules_history) | **GET** /schedule/history | Read schedule(s)


# **create_many_schedules**
> List[str] create_many_schedules(schedule_create_many)

Create many Schedules

Create many new observing schedules for ACROSS.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.schedule_create_many import ScheduleCreateMany
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/api/v1"
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
    api_instance = across.sdk.v1.ScheduleApi(api_client)
    schedule_create_many = across.sdk.v1.ScheduleCreateMany() # ScheduleCreateMany | 

    try:
        # Create many Schedules
        api_response = api_instance.create_many_schedules(schedule_create_many)
        print("The response of ScheduleApi->create_many_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->create_many_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_create_many** | [**ScheduleCreateMany**](ScheduleCreateMany.md)|  | 

### Return type

**List[str]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created schedule ids |  -  |
**404** | The schedule does not exist. |  -  |
**422** | Incorrect schedule parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_schedule**
> str create_schedule(schedule_create)

Create a Schedule

Create a new observing schedule for ACROSS.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.schedule_create import ScheduleCreate
from across.sdk.v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = across.sdk.v1.Configuration(
    host = "/api/v1"
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
    api_instance = across.sdk.v1.ScheduleApi(api_client)
    schedule_create = across.sdk.v1.ScheduleCreate() # ScheduleCreate | 

    try:
        # Create a Schedule
        api_response = api_instance.create_schedule(schedule_create)
        print("The response of ScheduleApi->create_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->create_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_create** | [**ScheduleCreate**](ScheduleCreate.md)|  | 

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
**201** | Created schedule id |  -  |
**404** | The schedule does not exist. |  -  |
**409** | Duplicate schedule |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule**
> Schedule get_schedule(schedule_id)

Read a schedule

Read a schedule by a schedule ID.

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.schedule import Schedule
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
    api_instance = across.sdk.v1.ScheduleApi(api_client)
    schedule_id = 'schedule_id_example' # str | 

    try:
        # Read a schedule
        api_response = api_instance.get_schedule(schedule_id)
        print("The response of ScheduleApi->get_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->get_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **str**|  | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a schedule |  -  |
**404** | Schedule not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedules**
> PageSchedule get_schedules(page=page, page_limit=page_limit, date_range_begin=date_range_begin, date_range_end=date_range_end, status=status, external_id=external_id, fidelity=fidelity, created_on=created_on, observatory_ids=observatory_ids, observatory_names=observatory_names, telescope_ids=telescope_ids, telescope_names=telescope_names, name=name)

Read schedule(s)

Read most recent schedules based on query params

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.page_schedule import PageSchedule
from across.sdk.v1.models.schedule_fidelity import ScheduleFidelity
from across.sdk.v1.models.schedule_status import ScheduleStatus
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
    api_instance = across.sdk.v1.ScheduleApi(api_client)
    page = 56 # int | Page number (optional)
    page_limit = 56 # int | Records per page (optional)
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    status = across.sdk.v1.ScheduleStatus() # ScheduleStatus |  (optional)
    external_id = 'external_id_example' # str |  (optional)
    fidelity = across.sdk.v1.ScheduleFidelity() # ScheduleFidelity |  (optional)
    created_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    observatory_ids = [] # List[Optional[str]] |  (optional) (default to [])
    observatory_names = [] # List[Optional[str]] |  (optional) (default to [])
    telescope_ids = [] # List[Optional[str]] |  (optional) (default to [])
    telescope_names = [] # List[Optional[str]] |  (optional) (default to [])
    name = 'name_example' # str |  (optional)

    try:
        # Read schedule(s)
        api_response = api_instance.get_schedules(page=page, page_limit=page_limit, date_range_begin=date_range_begin, date_range_end=date_range_end, status=status, external_id=external_id, fidelity=fidelity, created_on=created_on, observatory_ids=observatory_ids, observatory_names=observatory_names, telescope_ids=telescope_ids, telescope_names=telescope_names, name=name)
        print("The response of ScheduleApi->get_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->get_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **page_limit** | **int**| Records per page | [optional] 
 **date_range_begin** | **datetime**|  | [optional] 
 **date_range_end** | **datetime**|  | [optional] 
 **status** | [**ScheduleStatus**](.md)|  | [optional] 
 **external_id** | **str**|  | [optional] 
 **fidelity** | [**ScheduleFidelity**](.md)|  | [optional] 
 **created_on** | **datetime**|  | [optional] 
 **observatory_ids** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **observatory_names** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **telescope_ids** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **telescope_names** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **name** | **str**|  | [optional] 

### Return type

[**PageSchedule**](PageSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a schedule |  -  |
**404** | The schedule does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedules_history**
> PageSchedule get_schedules_history(page=page, page_limit=page_limit, date_range_begin=date_range_begin, date_range_end=date_range_end, status=status, external_id=external_id, fidelity=fidelity, created_on=created_on, observatory_ids=observatory_ids, observatory_names=observatory_names, telescope_ids=telescope_ids, telescope_names=telescope_names, name=name)

Read schedule(s)

Read many recent schedules based on query params

### Example


```python
import across.sdk.v1
from across.sdk.v1.models.page_schedule import PageSchedule
from across.sdk.v1.models.schedule_fidelity import ScheduleFidelity
from across.sdk.v1.models.schedule_status import ScheduleStatus
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
    api_instance = across.sdk.v1.ScheduleApi(api_client)
    page = 56 # int | Page number (optional)
    page_limit = 56 # int | Records per page (optional)
    date_range_begin = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    date_range_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    status = across.sdk.v1.ScheduleStatus() # ScheduleStatus |  (optional)
    external_id = 'external_id_example' # str |  (optional)
    fidelity = across.sdk.v1.ScheduleFidelity() # ScheduleFidelity |  (optional)
    created_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    observatory_ids = [] # List[Optional[str]] |  (optional) (default to [])
    observatory_names = [] # List[Optional[str]] |  (optional) (default to [])
    telescope_ids = [] # List[Optional[str]] |  (optional) (default to [])
    telescope_names = [] # List[Optional[str]] |  (optional) (default to [])
    name = 'name_example' # str |  (optional)

    try:
        # Read schedule(s)
        api_response = api_instance.get_schedules_history(page=page, page_limit=page_limit, date_range_begin=date_range_begin, date_range_end=date_range_end, status=status, external_id=external_id, fidelity=fidelity, created_on=created_on, observatory_ids=observatory_ids, observatory_names=observatory_names, telescope_ids=telescope_ids, telescope_names=telescope_names, name=name)
        print("The response of ScheduleApi->get_schedules_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->get_schedules_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **page_limit** | **int**| Records per page | [optional] 
 **date_range_begin** | **datetime**|  | [optional] 
 **date_range_end** | **datetime**|  | [optional] 
 **status** | [**ScheduleStatus**](.md)|  | [optional] 
 **external_id** | **str**|  | [optional] 
 **fidelity** | [**ScheduleFidelity**](.md)|  | [optional] 
 **created_on** | **datetime**|  | [optional] 
 **observatory_ids** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **observatory_names** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **telescope_ids** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **telescope_names** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **name** | **str**|  | [optional] 

### Return type

[**PageSchedule**](PageSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | The schedule does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

