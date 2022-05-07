# python_opendota.PlayersByRankApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_by_rank_get**](PlayersByRankApi.md#players_by_rank_get) | **GET** /playersByRank | GET /playersByRank


# **players_by_rank_get**
> PlayersByRankResponse players_by_rank_get()

GET /playersByRank

Players ordered by rank/medal tier

### Example


```python
import time
import python_opendota
from python_opendota.api import players_by_rank_api
from python_opendota.model.players_by_rank_response import PlayersByRankResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_by_rank_api.PlayersByRankApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /playersByRank
        api_response = api_instance.players_by_rank_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersByRankApi->players_by_rank_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PlayersByRankResponse**](PlayersByRankResponse.md)

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

