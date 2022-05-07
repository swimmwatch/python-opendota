# python_opendota.LeaguesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leagues_get**](LeaguesApi.md#leagues_get) | **GET** /leagues | GET /leagues
[**leagues_league_id_get**](LeaguesApi.md#leagues_league_id_get) | **GET** /leagues/{league_id} | GET /leagues/{league_id}
[**leagues_league_id_matches_get**](LeaguesApi.md#leagues_league_id_matches_get) | **GET** /leagues/{league_id}/matches | GET /leagues/{league_id}/matches
[**leagues_league_id_teams_get**](LeaguesApi.md#leagues_league_id_teams_get) | **GET** /leagues/{league_id}/teams | GET /leagues/{league_id}/teams


# **leagues_get**
> [LeagueObjectResponse] leagues_get()

GET /leagues

Get league data

### Example


```python
import time
import python_opendota
from python_opendota.api import leagues_api
from python_opendota.model.league_object_response import LeagueObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = leagues_api.LeaguesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /leagues
        api_response = api_instance.leagues_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LeaguesApi->leagues_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LeagueObjectResponse]**](LeagueObjectResponse.md)

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

# **leagues_league_id_get**
> [LeagueObjectResponse] leagues_league_id_get(league_id)

GET /leagues/{league_id}

Get data for a league

### Example


```python
import time
import python_opendota
from python_opendota.api import leagues_api
from python_opendota.model.league_object_response import LeagueObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = leagues_api.LeaguesApi(api_client)
    league_id = 1 # int | League ID

    # example passing only required values which don't have defaults set
    try:
        # GET /leagues/{league_id}
        api_response = api_instance.leagues_league_id_get(league_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LeaguesApi->leagues_league_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| League ID |

### Return type

[**[LeagueObjectResponse]**](LeagueObjectResponse.md)

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

# **leagues_league_id_matches_get**
> MatchObjectResponse leagues_league_id_matches_get(league_id)

GET /leagues/{league_id}/matches

Get matches for a team

### Example


```python
import time
import python_opendota
from python_opendota.api import leagues_api
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
    api_instance = leagues_api.LeaguesApi(api_client)
    league_id = 1 # int | League ID

    # example passing only required values which don't have defaults set
    try:
        # GET /leagues/{league_id}/matches
        api_response = api_instance.leagues_league_id_matches_get(league_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LeaguesApi->leagues_league_id_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| League ID |

### Return type

[**MatchObjectResponse**](MatchObjectResponse.md)

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

# **leagues_league_id_teams_get**
> TeamObjectResponse leagues_league_id_teams_get(league_id)

GET /leagues/{league_id}/teams

Get teams for a league

### Example


```python
import time
import python_opendota
from python_opendota.api import leagues_api
from python_opendota.model.team_object_response import TeamObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = leagues_api.LeaguesApi(api_client)
    league_id = 1 # int | League ID

    # example passing only required values which don't have defaults set
    try:
        # GET /leagues/{league_id}/teams
        api_response = api_instance.leagues_league_id_teams_get(league_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LeaguesApi->leagues_league_id_teams_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| League ID |

### Return type

[**TeamObjectResponse**](TeamObjectResponse.md)

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

