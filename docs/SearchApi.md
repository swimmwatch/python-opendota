# python_opendota.SearchApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](SearchApi.md#search_get) | **GET** /search | GET /search


# **search_get**
> [SearchResponse] search_get(q)

GET /search

Search players by personaname.

### Example


```python
import time
import python_opendota
from python_opendota.api import search_api
from python_opendota.model.search_response import SearchResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    q = "q_example" # str | Search string

    # example passing only required values which don't have defaults set
    try:
        # GET /search
        api_response = api_instance.search_get(q)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling SearchApi->search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search string |

### Return type

[**[SearchResponse]**](SearchResponse.md)

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

