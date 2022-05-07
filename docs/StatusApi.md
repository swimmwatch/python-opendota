# python_opendota.StatusApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](StatusApi.md#status_get) | **GET** /status | GET /status


# **status_get**
> bool, date, datetime, dict, float, int, list, str, none_type status_get()

GET /status

Get current service statistics

### Example


```python
import time
import python_opendota
from python_opendota.api import status_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /status
        api_response = api_instance.status_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling StatusApi->status_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

