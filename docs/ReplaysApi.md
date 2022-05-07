# python_opendota.ReplaysApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replays_get**](ReplaysApi.md#replays_get) | **GET** /replays | GET /replays


# **replays_get**
> [ReplaysResponse] replays_get(match_id)

GET /replays

Get data to construct a replay URL with

### Example


```python
import time
import python_opendota
from python_opendota.api import replays_api
from python_opendota.model.replays_response import ReplaysResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = replays_api.ReplaysApi(api_client)
    match_id = 1 # int | Match IDs (array)

    # example passing only required values which don't have defaults set
    try:
        # GET /replays
        api_response = api_instance.replays_get(match_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ReplaysApi->replays_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**| Match IDs (array) |

### Return type

[**[ReplaysResponse]**](ReplaysResponse.md)

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

