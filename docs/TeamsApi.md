# python_opendota.TeamsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_get**](TeamsApi.md#teams_get) | **GET** /teams | GET /teams
[**teams_team_id_get**](TeamsApi.md#teams_team_id_get) | **GET** /teams/{team_id} | GET /teams/{team_id}
[**teams_team_id_heroes_get**](TeamsApi.md#teams_team_id_heroes_get) | **GET** /teams/{team_id}/heroes | GET /teams/{team_id}/heroes
[**teams_team_id_matches_get**](TeamsApi.md#teams_team_id_matches_get) | **GET** /teams/{team_id}/matches | GET /teams/{team_id}/matches
[**teams_team_id_players_get**](TeamsApi.md#teams_team_id_players_get) | **GET** /teams/{team_id}/players | GET /teams/{team_id}/players


# **teams_get**
> [TeamObjectResponse] teams_get()

GET /teams

Get team data

### Example


```python
import time
import python_opendota
from python_opendota.api import teams_api
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
    api_instance = teams_api.TeamsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /teams
        api_response = api_instance.teams_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[TeamObjectResponse]**](TeamObjectResponse.md)

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

# **teams_team_id_get**
> TeamObjectResponse teams_team_id_get(team_id)

GET /teams/{team_id}

Get data for a team

### Example


```python
import time
import python_opendota
from python_opendota.api import teams_api
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
    api_instance = teams_api.TeamsApi(api_client)
    team_id = 1 # int | Team ID

    # example passing only required values which don't have defaults set
    try:
        # GET /teams/{team_id}
        api_response = api_instance.teams_team_id_get(team_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID |

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

# **teams_team_id_heroes_get**
> TeamHeroesResponse teams_team_id_heroes_get(team_id)

GET /teams/{team_id}/heroes

Get heroes for a team

### Example


```python
import time
import python_opendota
from python_opendota.api import teams_api
from python_opendota.model.team_heroes_response import TeamHeroesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)
    team_id = 1 # int | Team ID

    # example passing only required values which don't have defaults set
    try:
        # GET /teams/{team_id}/heroes
        api_response = api_instance.teams_team_id_heroes_get(team_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_heroes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID |

### Return type

[**TeamHeroesResponse**](TeamHeroesResponse.md)

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

# **teams_team_id_matches_get**
> MatchObjectResponse teams_team_id_matches_get(team_id)

GET /teams/{team_id}/matches

Get matches for a team

### Example


```python
import time
import python_opendota
from python_opendota.api import teams_api
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
    api_instance = teams_api.TeamsApi(api_client)
    team_id = 1 # int | Team ID

    # example passing only required values which don't have defaults set
    try:
        # GET /teams/{team_id}/matches
        api_response = api_instance.teams_team_id_matches_get(team_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID |

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

# **teams_team_id_players_get**
> TeamPlayersResponse teams_team_id_players_get(team_id)

GET /teams/{team_id}/players

Get players who have played for a team

### Example


```python
import time
import python_opendota
from python_opendota.api import teams_api
from python_opendota.model.team_players_response import TeamPlayersResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)
    team_id = 1 # int | Team ID

    # example passing only required values which don't have defaults set
    try:
        # GET /teams/{team_id}/players
        api_response = api_instance.teams_team_id_players_get(team_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_players_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID |

### Return type

[**TeamPlayersResponse**](TeamPlayersResponse.md)

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

