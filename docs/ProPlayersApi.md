# python_opendota.ProPlayersApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pro_players_get**](ProPlayersApi.md#pro_players_get) | **GET** /proPlayers | GET /proPlayers


# **pro_players_get**
> [PlayerObjectResponse] pro_players_get()

GET /proPlayers

Get list of pro players

### Example


```python
import time
import python_opendota
from python_opendota.api import pro_players_api
from python_opendota.model.player_object_response import PlayerObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pro_players_api.ProPlayersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /proPlayers
        api_response = api_instance.pro_players_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ProPlayersApi->pro_players_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[PlayerObjectResponse]**](PlayerObjectResponse.md)

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

