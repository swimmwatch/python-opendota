# python_opendota.LiveApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**live_get**](LiveApi.md#live_get) | **GET** /live | GET /live


# **live_get**
> [bool, date, datetime, dict, float, int, list, str, none_type] live_get()

GET /live

Get top currently ongoing live games

### Example


```python
import time
import python_opendota
from python_opendota.api import live_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = live_api.LiveApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /live
        api_response = api_instance.live_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LiveApi->live_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

