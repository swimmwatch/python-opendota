# python_opendota.PublicMatchesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_matches_get**](PublicMatchesApi.md#public_matches_get) | **GET** /publicMatches | GET /publicMatches


# **public_matches_get**
> [PublicMatchesResponse] public_matches_get()

GET /publicMatches

Get list of randomly sampled public matches

### Example


```python
import time
import python_opendota
from python_opendota.api import public_matches_api
from python_opendota.model.public_matches_response import PublicMatchesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_matches_api.PublicMatchesApi(api_client)
    mmr_ascending = 1 # int | Order by MMR ascending (optional)
    mmr_descending = 1 # int | Order by MMR descending (optional)
    less_than_match_id = 1 # int | Get matches with a match ID lower than this value (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /publicMatches
        api_response = api_instance.public_matches_get(mmr_ascending=mmr_ascending, mmr_descending=mmr_descending, less_than_match_id=less_than_match_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PublicMatchesApi->public_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mmr_ascending** | **int**| Order by MMR ascending | [optional]
 **mmr_descending** | **int**| Order by MMR descending | [optional]
 **less_than_match_id** | **int**| Get matches with a match ID lower than this value | [optional]

### Return type

[**[PublicMatchesResponse]**](PublicMatchesResponse.md)

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

