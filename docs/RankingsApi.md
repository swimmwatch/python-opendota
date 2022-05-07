# python_opendota.RankingsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rankings_get**](RankingsApi.md#rankings_get) | **GET** /rankings | GET /rankings


# **rankings_get**
> RankingsResponse rankings_get(hero_id)

GET /rankings

Top players by hero

### Example


```python
import time
import python_opendota
from python_opendota.api import rankings_api
from python_opendota.model.rankings_response import RankingsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rankings_api.RankingsApi(api_client)
    hero_id = "hero_id_example" # str | Hero ID

    # example passing only required values which don't have defaults set
    try:
        # GET /rankings
        api_response = api_instance.rankings_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling RankingsApi->rankings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **str**| Hero ID |

### Return type

[**RankingsResponse**](RankingsResponse.md)

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

