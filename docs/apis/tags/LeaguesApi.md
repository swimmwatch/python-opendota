<a name="__pageTop"></a>
# python_opendota.apis.tags.leagues_api.LeaguesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leagues_get**](#leagues_get) | **get** /leagues | GET /leagues
[**leagues_league_id_get**](#leagues_league_id_get) | **get** /leagues/{league_id} | GET /leagues/{league_id}
[**leagues_league_id_matches_get**](#leagues_league_id_matches_get) | **get** /leagues/{league_id}/matches | GET /leagues/{league_id}/matches
[**leagues_league_id_teams_get**](#leagues_league_id_teams_get) | **get** /leagues/{league_id}/teams | GET /leagues/{league_id}/teams

# **leagues_get**
<a name="leagues_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] leagues_get()

GET /leagues

Get league data

### Example

```python
import python_opendota
from python_opendota.apis.tags import leagues_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#leagues_get.ApiResponseFor200) | Success

#### leagues_get.ApiResponseFor200
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
**leagueid** | decimal.Decimal, int,  | decimal.Decimal,  | leagueid | [optional] 
**ticket** | str,  | str,  | ticket | [optional] 
**banner** | str,  | str,  | banner | [optional] 
**tier** | str,  | str,  | tier | [optional] 
**name** | str,  | str,  | name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_league_id_get**
<a name="leagues_league_id_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] leagues_league_id_get(league_id)

GET /leagues/{league_id}

Get data for a league

### Example

```python
import python_opendota
from python_opendota.apis.tags import leagues_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leagues_api.LeaguesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'league_id': 1,
    }
    try:
        # GET /leagues/{league_id}
        api_response = api_instance.leagues_league_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LeaguesApi->leagues_league_id_get: %s\n" % e)
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
league_id | LeagueIdSchema | | 

# LeagueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#leagues_league_id_get.ApiResponseFor200) | Success

#### leagues_league_id_get.ApiResponseFor200
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
**leagueid** | decimal.Decimal, int,  | decimal.Decimal,  | leagueid | [optional] 
**ticket** | str,  | str,  | ticket | [optional] 
**banner** | str,  | str,  | banner | [optional] 
**tier** | str,  | str,  | tier | [optional] 
**name** | str,  | str,  | name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_league_id_matches_get**
<a name="leagues_league_id_matches_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leagues_league_id_matches_get(league_id)

GET /leagues/{league_id}/matches

Get matches for a team

### Example

```python
import python_opendota
from python_opendota.apis.tags import leagues_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leagues_api.LeaguesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'league_id': 1,
    }
    try:
        # GET /leagues/{league_id}/matches
        api_response = api_instance.leagues_league_id_matches_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LeaguesApi->leagues_league_id_matches_get: %s\n" % e)
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
league_id | LeagueIdSchema | | 

# LeagueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#leagues_league_id_matches_get.ApiResponseFor200) | Success

#### leagues_league_id_matches_get.ApiResponseFor200
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
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Length of the match | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Unix timestamp of when the match began | [optional] 
**radiant_team_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Radiant&#x27;s team_id | [optional] 
**radiant_name** | str,  | str,  | The Radiant&#x27;s team name | [optional] 
**dire_team_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Dire&#x27;s team_id | [optional] 
**dire_name** | str,  | str,  | The Dire&#x27;s team name | [optional] 
**leagueid** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier for the league the match took place in | [optional] 
**league_name** | str,  | str,  | Name of league the match took place in | [optional] 
**series_id** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier for the series of the match | [optional] 
**series_type** | decimal.Decimal, int,  | decimal.Decimal,  | Type of series the match was | [optional] 
**radiant_score** | decimal.Decimal, int,  | decimal.Decimal,  | Number of kills the Radiant team had when the match ended | [optional] 
**dire_score** | decimal.Decimal, int,  | decimal.Decimal,  | Number of kills the Dire team had when the match ended | [optional] 
**radiant_win** | bool,  | BoolClass,  | Whether or not the Radiant won the match | [optional] 
**radiant** | bool,  | BoolClass,  | Whether the team/player/hero was on Radiant | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_league_id_teams_get**
<a name="leagues_league_id_teams_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} leagues_league_id_teams_get(league_id)

GET /leagues/{league_id}/teams

Get teams for a league

### Example

```python
import python_opendota
from python_opendota.apis.tags import leagues_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leagues_api.LeaguesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'league_id': 1,
    }
    try:
        # GET /leagues/{league_id}/teams
        api_response = api_instance.leagues_league_id_teams_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LeaguesApi->leagues_league_id_teams_get: %s\n" % e)
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
league_id | LeagueIdSchema | | 

# LeagueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#leagues_league_id_teams_get.ApiResponseFor200) | Success

#### leagues_league_id_teams_get.ApiResponseFor200
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

