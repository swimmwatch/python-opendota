# python_opendota.HeroStatsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_stats_get**](HeroStatsApi.md#hero_stats_get) | **GET** /heroStats | GET /heroStats


# **hero_stats_get**
> [HeroStatsResponse] hero_stats_get()

GET /heroStats

Get stats about hero performance in recent matches

### Example


```python
import time
import python_opendota
from python_opendota.api import hero_stats_api
from python_opendota.model.hero_stats_response import HeroStatsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hero_stats_api.HeroStatsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /heroStats
        api_response = api_instance.hero_stats_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroStatsApi->hero_stats_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[HeroStatsResponse]**](HeroStatsResponse.md)

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

