# python_opendota.ProMatchesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pro_matches_get**](ProMatchesApi.md#pro_matches_get) | **GET** /proMatches | GET /proMatches


# **pro_matches_get**
> [MatchObjectResponse] pro_matches_get()

GET /proMatches

Get list of pro matches

### Example


```python
import time
import python_opendota
from python_opendota.api import pro_matches_api
from python_opendota.model.match_object_response import MatchObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pro_matches_api.ProMatchesApi(api_client)
    less_than_match_id = 1 # int | Get matches with a match ID lower than this value (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /proMatches
        api_response = api_instance.pro_matches_get(less_than_match_id=less_than_match_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ProMatchesApi->pro_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **less_than_match_id** | **int**| Get matches with a match ID lower than this value | [optional]

### Return type

[**[MatchObjectResponse]**](MatchObjectResponse.md)

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

