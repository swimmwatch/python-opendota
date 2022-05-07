# python_opendota.BenchmarksApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**benchmarks_get**](BenchmarksApi.md#benchmarks_get) | **GET** /benchmarks | GET /benchmarks


# **benchmarks_get**
> BenchmarksResponse benchmarks_get(hero_id)

GET /benchmarks

Benchmarks of average stat values for a hero

### Example


```python
import time
import python_opendota
from python_opendota.api import benchmarks_api
from python_opendota.model.benchmarks_response import BenchmarksResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = benchmarks_api.BenchmarksApi(api_client)
    hero_id = "hero_id_example" # str | Hero ID

    # example passing only required values which don't have defaults set
    try:
        # GET /benchmarks
        api_response = api_instance.benchmarks_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling BenchmarksApi->benchmarks_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **str**| Hero ID |

### Return type

[**BenchmarksResponse**](BenchmarksResponse.md)

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

