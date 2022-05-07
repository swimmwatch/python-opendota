# python_opendota.MatchesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_match_id_get**](MatchesApi.md#matches_match_id_get) | **GET** /matches/{match_id} | GET /matches/{match_id}


# **matches_match_id_get**
> MatchResponse matches_match_id_get(match_id)

GET /matches/{match_id}

Match data

### Example


```python
import time
import python_opendota
from python_opendota.api import matches_api
from python_opendota.model.match_response import MatchResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = matches_api.MatchesApi(api_client)
    match_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # GET /matches/{match_id}
        api_response = api_instance.matches_match_id_get(match_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling MatchesApi->matches_match_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  |

### Return type

[**MatchResponse**](MatchResponse.md)

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

