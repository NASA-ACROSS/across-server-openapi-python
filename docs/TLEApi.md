# across.sdk.v1.TLEApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tle**](TLEApi.md#create_tle) | **POST** /tle/ | Create a TLE


# **create_tle**
> TLE create_tle(tle_create)

Create a TLE

Create a new TLE for ACROSS.

### Example

* Bearer Authentication (Authorization):

```python
import across.sdk.v1
from across.sdk.v1.models.tle import TLE
from across.sdk.v1.models.tle_create import TLECreate
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
    api_instance = across.sdk.v1.TLEApi(api_client)
    tle_create = across.sdk.v1.TLECreate() # TLECreate | 

    try:
        # Create a TLE
        api_response = api_instance.create_tle(tle_create)
        print("The response of TLEApi->create_tle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLEApi->create_tle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tle_create** | [**TLECreate**](TLECreate.md)|  | 

### Return type

[**TLE**](TLE.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**404** | The TLE does not exist. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

