# python_opendota.ParsedMatchesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parsed_matches_get**](ParsedMatchesApi.md#parsed_matches_get) | **GET** /parsedMatches | GET /parsedMatches


# **parsed_matches_get**
> [ParsedMatchesResponse] parsed_matches_get()

GET /parsedMatches

Get list of parsed match IDs

### Example


```python
import time
import python_opendota
from python_opendota.api import parsed_matches_api
from python_opendota.model.parsed_matches_response import ParsedMatchesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = parsed_matches_api.ParsedMatchesApi(api_client)
    less_than_match_id = 1 # int | Get matches with a match ID lower than this value (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /parsedMatches
        api_response = api_instance.parsed_matches_get(less_than_match_id=less_than_match_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ParsedMatchesApi->parsed_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **less_than_match_id** | **int**| Get matches with a match ID lower than this value | [optional]

### Return type

[**[ParsedMatchesResponse]**](ParsedMatchesResponse.md)

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

