# python_opendota.FindMatchesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_matches_get**](FindMatchesApi.md#find_matches_get) | **GET** /findMatches | GET /


# **find_matches_get**
> bool, date, datetime, dict, float, int, list, str, none_type find_matches_get()

GET /

Finds recent matches by heroes played

### Example


```python
import time
import python_opendota
from python_opendota.api import find_matches_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = find_matches_api.FindMatchesApi(api_client)
    team_a = 1 # int | Hero IDs on first team (array) (optional)
    team_b = 1 # int | Hero IDs on second team (array) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /
        api_response = api_instance.find_matches_get(team_a=team_a, team_b=team_b)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling FindMatchesApi->find_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_a** | **int**| Hero IDs on first team (array) | [optional]
 **team_b** | **int**| Hero IDs on second team (array) | [optional]

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

