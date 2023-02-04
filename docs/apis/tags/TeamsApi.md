<a name="__pageTop"></a>
# python_opendota.apis.tags.teams_api.TeamsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_get**](#teams_get) | **get** /teams | GET /teams
[**teams_team_id_get**](#teams_team_id_get) | **get** /teams/{team_id} | GET /teams/{team_id}
[**teams_team_id_heroes_get**](#teams_team_id_heroes_get) | **get** /teams/{team_id}/heroes | GET /teams/{team_id}/heroes
[**teams_team_id_matches_get**](#teams_team_id_matches_get) | **get** /teams/{team_id}/matches | GET /teams/{team_id}/matches
[**teams_team_id_players_get**](#teams_team_id_players_get) | **get** /teams/{team_id}/players | GET /teams/{team_id}/players

# **teams_get**
<a name="teams_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] teams_get()

GET /teams

Get team data

### Example

```python
import python_opendota
from python_opendota.apis.tags import teams_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
    }
    try:
        # GET /teams
        api_response = api_instance.teams_get(
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#teams_get.ApiResponseFor200) | Success

#### teams_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**team_id** | decimal.Decimal, int,  | decimal.Decimal,  | Team&#x27;s identifier | [optional] 
**rating** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Elo rating of the team | [optional] 
**wins** | decimal.Decimal, int,  | decimal.Decimal,  | The number of games won by this team | [optional] 
**losses** | decimal.Decimal, int,  | decimal.Decimal,  | The number of losses by this team | [optional] 
**last_match_time** | decimal.Decimal, int,  | decimal.Decimal,  | The Unix timestamp of the last match played by this team | [optional] 
**name** | str,  | str,  | Team name, eg. &#x27;Newbee&#x27; | [optional] 
**tag** | str,  | str,  | The team tag/abbreviation | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_team_id_get**
<a name="teams_team_id_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} teams_team_id_get(team_id)

GET /teams/{team_id}

Get data for a team

### Example

```python
import python_opendota
from python_opendota.apis.tags import teams_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'team_id': 1,
    }
    try:
        # GET /teams/{team_id}
        api_response = api_instance.teams_team_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
team_id | TeamIdSchema | | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#teams_team_id_get.ApiResponseFor200) | Success

#### teams_team_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**team_id** | decimal.Decimal, int,  | decimal.Decimal,  | Team&#x27;s identifier | [optional] 
**rating** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Elo rating of the team | [optional] 
**wins** | decimal.Decimal, int,  | decimal.Decimal,  | The number of games won by this team | [optional] 
**losses** | decimal.Decimal, int,  | decimal.Decimal,  | The number of losses by this team | [optional] 
**last_match_time** | decimal.Decimal, int,  | decimal.Decimal,  | The Unix timestamp of the last match played by this team | [optional] 
**name** | str,  | str,  | Team name, eg. &#x27;Newbee&#x27; | [optional] 
**tag** | str,  | str,  | The team tag/abbreviation | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_team_id_heroes_get**
<a name="teams_team_id_heroes_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} teams_team_id_heroes_get(team_id)

GET /teams/{team_id}/heroes

Get heroes for a team

### Example

```python
import python_opendota
from python_opendota.apis.tags import teams_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'team_id': 1,
    }
    try:
        # GET /teams/{team_id}/heroes
        api_response = api_instance.teams_team_id_heroes_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_heroes_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
team_id | TeamIdSchema | | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#teams_team_id_heroes_get.ApiResponseFor200) | Success

#### teams_team_id_heroes_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | The hero ID | [optional] 
**name** | str,  | str,  | The hero name | [optional] 
**games_played** | decimal.Decimal, int,  | decimal.Decimal,  | Number of games played | [optional] 
**wins** | decimal.Decimal, int,  | decimal.Decimal,  | Number of wins | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_team_id_matches_get**
<a name="teams_team_id_matches_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} teams_team_id_matches_get(team_id)

GET /teams/{team_id}/matches

Get matches for a team

### Example

```python
import python_opendota
from python_opendota.apis.tags import teams_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'team_id': 1,
    }
    try:
        # GET /teams/{team_id}/matches
        api_response = api_instance.teams_team_id_matches_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_matches_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
team_id | TeamIdSchema | | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#teams_team_id_matches_get.ApiResponseFor200) | Success

#### teams_team_id_matches_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**match_id** | decimal.Decimal, int,  | decimal.Decimal,  | Used to identify individual matches, e.g. 3703866531 | [optional] 
**radiant** | bool,  | BoolClass,  | Whether the team/player/hero was on Radiant | [optional] 
**radiant_win** | bool,  | BoolClass,  | Whether or not the Radiant won the match | [optional] 
**radiant_score** | decimal.Decimal, int,  | decimal.Decimal,  | Number of kills the Radiant team had when the match ended | [optional] 
**dire_score** | decimal.Decimal, int,  | decimal.Decimal,  | Number of kills the Dire team had when the match ended | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Length of the match | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Unix timestamp of when the match began | [optional] 
**leagueid** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier for the league the match took place in | [optional] 
**league_name** | str,  | str,  | Name of league the match took place in | [optional] 
**cluster** | decimal.Decimal, int,  | decimal.Decimal,  | cluster | [optional] 
**opposing_team_id** | decimal.Decimal, int,  | decimal.Decimal,  | Opposing team identifier | [optional] 
**opposing_team_name** | str,  | str,  | Opposing team name, e.g. &#x27;Evil Geniuses&#x27; | [optional] 
**opposing_team_logo** | str,  | str,  | Opposing team logo url | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_team_id_players_get**
<a name="teams_team_id_players_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} teams_team_id_players_get(team_id)

GET /teams/{team_id}/players

Get players who have played for a team

### Example

```python
import python_opendota
from python_opendota.apis.tags import teams_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = teams_api.TeamsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'team_id': 1,
    }
    try:
        # GET /teams/{team_id}/players
        api_response = api_instance.teams_team_id_players_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling TeamsApi->teams_team_id_players_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
team_id | TeamIdSchema | | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#teams_team_id_players_get.ApiResponseFor200) | Success

#### teams_team_id_players_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | str,  | str,  | The player account ID | [optional] 
**name** | str,  | str,  | The player name | [optional] 
**games_played** | decimal.Decimal, int,  | decimal.Decimal,  | Number of games played | [optional] 
**wins** | decimal.Decimal, int,  | decimal.Decimal,  | Number of wins | [optional] 
**is_current_team_member** | bool,  | BoolClass,  | If this player is on the current roster | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

