<a name="__pageTop"></a>
# python_opendota.apis.tags.players_api.PlayersApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_account_id_counts_get**](#players_account_id_counts_get) | **get** /players/{account_id}/counts | GET /players/{account_id}/counts
[**players_account_id_get**](#players_account_id_get) | **get** /players/{account_id} | GET /players/{account_id}
[**players_account_id_heroes_get**](#players_account_id_heroes_get) | **get** /players/{account_id}/heroes | GET /players/{account_id}/heroes
[**players_account_id_histograms_field_get**](#players_account_id_histograms_field_get) | **get** /players/{account_id}/histograms/{field} | GET /players/{account_id}/histograms
[**players_account_id_matches_get**](#players_account_id_matches_get) | **get** /players/{account_id}/matches | GET /players/{account_id}/matches
[**players_account_id_peers_get**](#players_account_id_peers_get) | **get** /players/{account_id}/peers | GET /players/{account_id}/peers
[**players_account_id_pros_get**](#players_account_id_pros_get) | **get** /players/{account_id}/pros | GET /players/{account_id}/pros
[**players_account_id_rankings_get**](#players_account_id_rankings_get) | **get** /players/{account_id}/rankings | GET /players/{account_id}/rankings
[**players_account_id_ratings_get**](#players_account_id_ratings_get) | **get** /players/{account_id}/ratings | GET /players/{account_id}/ratings
[**players_account_id_recent_matches_get**](#players_account_id_recent_matches_get) | **get** /players/{account_id}/recentMatches | GET /players/{account_id}/recentMatches
[**players_account_id_refresh_post**](#players_account_id_refresh_post) | **post** /players/{account_id}/refresh | POST /players/{account_id}/refresh
[**players_account_id_totals_get**](#players_account_id_totals_get) | **get** /players/{account_id}/totals | GET /players/{account_id}/totals
[**players_account_id_wardmap_get**](#players_account_id_wardmap_get) | **get** /players/{account_id}/wardmap | GET /players/{account_id}/wardmap
[**players_account_id_wl_get**](#players_account_id_wl_get) | **get** /players/{account_id}/wl | GET /players/{account_id}/wl
[**players_account_id_wordcloud_get**](#players_account_id_wordcloud_get) | **get** /players/{account_id}/wordcloud | GET /players/{account_id}/wordcloud

# **players_account_id_counts_get**
<a name="players_account_id_counts_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} players_account_id_counts_get(account_id)

GET /players/{account_id}/counts

Counts in categories

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/counts
        api_response = api_instance.players_account_id_counts_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_counts_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/counts
        api_response = api_instance.players_account_id_counts_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_counts_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_counts_get.ApiResponseFor200) | Success

#### players_account_id_counts_get.ApiResponseFor200
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
**[leaver_status](#leaver_status)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer describing whether or not the player left the game. 0: didn&#x27;t leave. 1: left safely. 2+: Abandoned | [optional] 
**[game_mode](#game_mode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | [optional] 
**[lobby_type](#lobby_type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | [optional] 
**[lane_role](#lane_role)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | lane_role | [optional] 
**[region](#region)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer corresponding to the region the game was played on | [optional] 
**[patch](#patch)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | patch | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# leaver_status

Integer describing whether or not the player left the game. 0: didn't leave. 1: left safely. 2+: Abandoned

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer describing whether or not the player left the game. 0: didn&#x27;t leave. 1: left safely. 2+: Abandoned | 

# game_mode

Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | 

# lobby_type

Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | 

# lane_role

lane_role

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | lane_role | 

# region

Integer corresponding to the region the game was played on

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Integer corresponding to the region the game was played on | 

# patch

patch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | patch | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_get**
<a name="players_account_id_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} players_account_id_get(account_id)

GET /players/{account_id}

Player data

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    try:
        # GET /players/{account_id}
        api_response = api_instance.players_account_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_get: %s\n" % e)
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
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_get.ApiResponseFor200) | Success

#### players_account_id_get.ApiResponseFor200
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
**solo_competitive_rank** | decimal.Decimal, int,  | decimal.Decimal,  | solo_competitive_rank | [optional] 
**competitive_rank** | decimal.Decimal, int,  | decimal.Decimal,  | competitive_rank | [optional] 
**rank_tier** | decimal.Decimal, int, float,  | decimal.Decimal,  | rank_tier | [optional] 
**leaderboard_rank** | decimal.Decimal, int, float,  | decimal.Decimal,  | leaderboard_rank | [optional] 
**[mmr_estimate](#mmr_estimate)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | mmr_estimate | [optional] 
**[profile](#profile)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | profile | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mmr_estimate

mmr_estimate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | mmr_estimate | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**estimate** | decimal.Decimal, int, float,  | decimal.Decimal,  | estimate | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# profile

profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_id** | decimal.Decimal, int,  | decimal.Decimal,  | account_id | [optional] 
**personaname** | str,  | str,  | personaname | [optional] 
**name** | str,  | str,  | name | [optional] 
**plus** | bool,  | BoolClass,  | Boolean indicating status of current Dota Plus subscription | [optional] 
**cheese** | decimal.Decimal, int,  | decimal.Decimal,  | cheese | [optional] 
**steamid** | str,  | str,  | steamid | [optional] 
**avatar** | str,  | str,  | avatar | [optional] 
**avatarmedium** | str,  | str,  | avatarmedium | [optional] 
**avatarfull** | str,  | str,  | avatarfull | [optional] 
**profileurl** | str,  | str,  | profileurl | [optional] 
**last_login** | str,  | str,  | last_login | [optional] 
**loccountrycode** | str,  | str,  | loccountrycode | [optional] 
**is_contributor** | bool,  | BoolClass,  | Boolean indicating if the user contributed to the development of OpenDota | [optional] if omitted the server will use the default value of False
**is_subscriber** | bool,  | BoolClass,  | Boolean indicating if the user subscribed to OpenDota | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_heroes_get**
<a name="players_account_id_heroes_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_heroes_get(account_id)

GET /players/{account_id}/heroes

Heroes played

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/heroes
        api_response = api_instance.players_account_id_heroes_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_heroes_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/heroes
        api_response = api_instance.players_account_id_heroes_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_heroes_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_heroes_get.ApiResponseFor200) | Success

#### players_account_id_heroes_get.ApiResponseFor200
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
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | hero | 

# items

hero

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | hero | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hero_id** | str,  | str,  | The ID value of the hero played | [optional] 
**last_played** | decimal.Decimal, int,  | decimal.Decimal,  | last_played | [optional] 
**games** | decimal.Decimal, int,  | decimal.Decimal,  | games | [optional] 
**win** | decimal.Decimal, int,  | decimal.Decimal,  | win | [optional] 
**with_games** | decimal.Decimal, int,  | decimal.Decimal,  | with_games | [optional] 
**with_win** | decimal.Decimal, int,  | decimal.Decimal,  | with_win | [optional] 
**against_games** | decimal.Decimal, int,  | decimal.Decimal,  | against_games | [optional] 
**against_win** | decimal.Decimal, int,  | decimal.Decimal,  | against_win | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_histograms_field_get**
<a name="players_account_id_histograms_field_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_histograms_field_get(account_idfield)

GET /players/{account_id}/histograms

Distribution of matches in a single stat

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
        'field': "field_example",
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/histograms
        api_response = api_instance.players_account_id_histograms_field_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_histograms_field_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
        'field': "field_example",
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/histograms
        api_response = api_instance.players_account_id_histograms_field_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_histograms_field_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 
field | FieldSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FieldSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_histograms_field_get.ApiResponseFor200) | Success

#### players_account_id_histograms_field_get.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_matches_get**
<a name="players_account_id_matches_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_matches_get(account_id)

GET /players/{account_id}/matches

Matches played

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/matches
        api_response = api_instance.players_account_id_matches_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_matches_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
        'project': "project_example",
    }
    try:
        # GET /players/{account_id}/matches
        api_response = api_instance.players_account_id_matches_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_matches_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional
project | ProjectSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_matches_get.ApiResponseFor200) | Success

#### players_account_id_matches_get.ApiResponseFor200
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
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the match | 

# items

Object containing information on the match

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the match | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**match_id** | decimal.Decimal, int,  | decimal.Decimal,  | Match ID | [optional] 
**player_slot** | decimal.Decimal, int,  | decimal.Decimal,  | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**radiant_win** | bool,  | BoolClass,  | Boolean indicating whether Radiant won the match | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Duration of the game in seconds | [optional] 
**game_mode** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | [optional] 
**lobby_type** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | [optional] 
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID value of the hero played | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time the game started in seconds since 1970 | [optional] 
**version** | decimal.Decimal, int,  | decimal.Decimal,  | version | [optional] 
**kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total kills the player had at the end of the game | [optional] 
**deaths** | decimal.Decimal, int,  | decimal.Decimal,  | Total deaths the player had at the end of the game | [optional] 
**assists** | decimal.Decimal, int,  | decimal.Decimal,  | Total assists the player had at the end of the game | [optional] 
**skill** | decimal.Decimal, int,  | decimal.Decimal,  | Skill bracket assigned by Valve (Normal, High, Very High) | [optional] 
**average_rank** | decimal.Decimal, int,  | decimal.Decimal,  | Average rank of players with public match data | [optional] 
**leaver_status** | decimal.Decimal, int,  | decimal.Decimal,  | Integer describing whether or not the player left the game. 0: didn&#x27;t leave. 1: left safely. 2+: Abandoned | [optional] 
**party_size** | decimal.Decimal, int,  | decimal.Decimal,  | Size of the player&#x27;s party | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_peers_get**
<a name="players_account_id_peers_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_peers_get(account_id)

GET /players/{account_id}/peers

Players played with

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/peers
        api_response = api_instance.players_account_id_peers_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_peers_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/peers
        api_response = api_instance.players_account_id_peers_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_peers_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_peers_get.ApiResponseFor200) | Success

#### players_account_id_peers_get.ApiResponseFor200
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
**account_id** | decimal.Decimal, int,  | decimal.Decimal,  | account_id | [optional] 
**last_played** | decimal.Decimal, int,  | decimal.Decimal,  | last_played | [optional] 
**win** | decimal.Decimal, int,  | decimal.Decimal,  | win | [optional] 
**games** | decimal.Decimal, int,  | decimal.Decimal,  | games | [optional] 
**with_win** | decimal.Decimal, int,  | decimal.Decimal,  | with_win | [optional] 
**with_games** | decimal.Decimal, int,  | decimal.Decimal,  | with_games | [optional] 
**against_win** | decimal.Decimal, int,  | decimal.Decimal,  | against_win | [optional] 
**against_games** | decimal.Decimal, int,  | decimal.Decimal,  | against_games | [optional] 
**with_gpm_sum** | decimal.Decimal, int,  | decimal.Decimal,  | with_gpm_sum | [optional] 
**with_xpm_sum** | decimal.Decimal, int,  | decimal.Decimal,  | with_xpm_sum | [optional] 
**personaname** | str,  | str,  | personaname | [optional] 
**name** | str,  | str,  | name | [optional] 
**is_contributor** | bool,  | BoolClass,  | is_contributor | [optional] 
**is_subscriber** | bool,  | BoolClass,  | is_subscriber | [optional] 
**last_login** | str,  | str,  | last_login | [optional] 
**avatar** | str,  | str,  | avatar | [optional] 
**avatarfull** | str,  | str,  | avatarfull | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_pros_get**
<a name="players_account_id_pros_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_pros_get(account_id)

GET /players/{account_id}/pros

Pro players played with

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/pros
        api_response = api_instance.players_account_id_pros_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_pros_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/pros
        api_response = api_instance.players_account_id_pros_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_pros_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_pros_get.ApiResponseFor200) | Success

#### players_account_id_pros_get.ApiResponseFor200
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
**account_id** | decimal.Decimal, int,  | decimal.Decimal,  | account_id | [optional] 
**name** | str,  | str,  | name | [optional] 
**country_code** | str,  | str,  | country_code | [optional] 
**fantasy_role** | decimal.Decimal, int,  | decimal.Decimal,  | fantasy_role | [optional] 
**team_id** | decimal.Decimal, int,  | decimal.Decimal,  | team_id | [optional] 
**team_name** | str,  | str,  | team_name | [optional] 
**team_tag** | str,  | str,  | team_tag | [optional] 
**is_locked** | bool,  | BoolClass,  | is_locked | [optional] 
**is_pro** | bool,  | BoolClass,  | is_pro | [optional] 
**locked_until** | decimal.Decimal, int,  | decimal.Decimal,  | locked_until | [optional] 
**steamid** | str,  | str,  | steamid | [optional] 
**avatar** | str,  | str,  | avatar | [optional] 
**avatarmedium** | str,  | str,  | avatarmedium | [optional] 
**avatarfull** | str,  | str,  | avatarfull | [optional] 
**profileurl** | str,  | str,  | profileurl | [optional] 
**last_login** | str, datetime,  | str,  | last_login | [optional] value must conform to RFC-3339 date-time
**full_history_time** | str, datetime,  | str,  | full_history_time | [optional] value must conform to RFC-3339 date-time
**cheese** | decimal.Decimal, int,  | decimal.Decimal,  | cheese | [optional] 
**fh_unavailable** | bool,  | BoolClass,  | fh_unavailable | [optional] 
**loccountrycode** | str,  | str,  | loccountrycode | [optional] 
**last_played** | decimal.Decimal, int,  | decimal.Decimal,  | last_played | [optional] 
**win** | decimal.Decimal, int,  | decimal.Decimal,  | win | [optional] 
**games** | decimal.Decimal, int,  | decimal.Decimal,  | games | [optional] 
**with_win** | decimal.Decimal, int,  | decimal.Decimal,  | with_win | [optional] 
**with_games** | decimal.Decimal, int,  | decimal.Decimal,  | with_games | [optional] 
**against_win** | decimal.Decimal, int,  | decimal.Decimal,  | against_win | [optional] 
**against_games** | decimal.Decimal, int,  | decimal.Decimal,  | against_games | [optional] 
**with_gpm_sum** | decimal.Decimal, int,  | decimal.Decimal,  | with_gpm_sum | [optional] 
**with_xpm_sum** | decimal.Decimal, int,  | decimal.Decimal,  | with_xpm_sum | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_rankings_get**
<a name="players_account_id_rankings_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_rankings_get(account_id)

GET /players/{account_id}/rankings

Player hero rankings

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    try:
        # GET /players/{account_id}/rankings
        api_response = api_instance.players_account_id_rankings_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_rankings_get: %s\n" % e)
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
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_rankings_get.ApiResponseFor200) | Success

#### players_account_id_rankings_get.ApiResponseFor200
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
**hero_id** | str,  | str,  | The ID value of the hero played | [optional] 
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | hero_score | [optional] 
**percent_rank** | decimal.Decimal, int, float,  | decimal.Decimal,  | percent_rank | [optional] 
**card** | decimal.Decimal, int,  | decimal.Decimal,  | numeric_rank | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_ratings_get**
<a name="players_account_id_ratings_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_ratings_get(account_id)

GET /players/{account_id}/ratings

Player rating history

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    try:
        # GET /players/{account_id}/ratings
        api_response = api_instance.players_account_id_ratings_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_ratings_get: %s\n" % e)
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
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_ratings_get.ApiResponseFor200) | Success

#### players_account_id_ratings_get.ApiResponseFor200
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
**account_id** | decimal.Decimal, int,  | decimal.Decimal,  | account_id | [optional] 
**match_id** | decimal.Decimal, int,  | decimal.Decimal,  | match_id | [optional] 
**solo_competitive_rank** | decimal.Decimal, int,  | decimal.Decimal,  | solo_competitive_rank | [optional] 
**competitive_rank** | decimal.Decimal, int,  | decimal.Decimal,  | competitive_rank | [optional] 
**time** | decimal.Decimal, int,  | decimal.Decimal,  | time | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_recent_matches_get**
<a name="players_account_id_recent_matches_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_recent_matches_get(account_id)

GET /players/{account_id}/recentMatches

Recent matches played

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    try:
        # GET /players/{account_id}/recentMatches
        api_response = api_instance.players_account_id_recent_matches_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_recent_matches_get: %s\n" % e)
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
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_recent_matches_get.ApiResponseFor200) | Success

#### players_account_id_recent_matches_get.ApiResponseFor200
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
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | match | 

# items

match

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | match | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**match_id** | decimal.Decimal, int,  | decimal.Decimal,  | Match ID | [optional] 
**player_slot** | decimal.Decimal, int,  | decimal.Decimal,  | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**radiant_win** | bool,  | BoolClass,  | Boolean indicating whether Radiant won the match | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Duration of the game in seconds | [optional] 
**game_mode** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | [optional] 
**lobby_type** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | [optional] 
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID value of the hero played | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Start time of the match in seconds elapsed since 1970 | [optional] 
**version** | decimal.Decimal, int,  | decimal.Decimal,  | version | [optional] 
**kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total kills the player had at the end of the match | [optional] 
**deaths** | decimal.Decimal, int,  | decimal.Decimal,  | Total deaths the player had at the end of the match | [optional] 
**assists** | decimal.Decimal, int,  | decimal.Decimal,  | Total assists the player had at the end of the match | [optional] 
**skill** | decimal.Decimal, int,  | decimal.Decimal,  | Skill bracket assigned by Valve (Normal, High, Very High). If the skill is unknown, will return null. | [optional] 
**average_rank** | decimal.Decimal, int,  | decimal.Decimal,  | Average rank of players with public match data | [optional] 
**xp_per_min** | decimal.Decimal, int,  | decimal.Decimal,  | Experience Per Minute obtained by the player | [optional] 
**gold_per_min** | decimal.Decimal, int,  | decimal.Decimal,  | Average gold per minute of the player | [optional] 
**hero_damage** | decimal.Decimal, int,  | decimal.Decimal,  | Total hero damage to enemy heroes | [optional] 
**hero_healing** | decimal.Decimal, int,  | decimal.Decimal,  | Total healing of ally heroes | [optional] 
**last_hits** | decimal.Decimal, int,  | decimal.Decimal,  | Total last hits the player had at the end of the match | [optional] 
**lane** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to which lane the player laned in for the match | [optional] 
**lane_role** | decimal.Decimal, int,  | decimal.Decimal,  | lane_role | [optional] 
**is_roaming** | bool,  | BoolClass,  | Boolean describing whether or not the player roamed | [optional] 
**cluster** | decimal.Decimal, int,  | decimal.Decimal,  | cluster | [optional] 
**leaver_status** | decimal.Decimal, int,  | decimal.Decimal,  | Integer describing whether or not the player left the game. 0: didn&#x27;t leave. 1: left safely. 2+: Abandoned | [optional] 
**party_size** | decimal.Decimal, int,  | decimal.Decimal,  | Size of the players party. If not in a party, will return 1. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_refresh_post**
<a name="players_account_id_refresh_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} players_account_id_refresh_post(account_id)

POST /players/{account_id}/refresh

Refresh player match history

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    try:
        # POST /players/{account_id}/refresh
        api_response = api_instance.players_account_id_refresh_post(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_refresh_post: %s\n" % e)
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
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_refresh_post.ApiResponseFor200) | Success

#### players_account_id_refresh_post.ApiResponseFor200
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

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_totals_get**
<a name="players_account_id_totals_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] players_account_id_totals_get(account_id)

GET /players/{account_id}/totals

Totals in stats

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/totals
        api_response = api_instance.players_account_id_totals_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_totals_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/totals
        api_response = api_instance.players_account_id_totals_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_totals_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_totals_get.ApiResponseFor200) | Success

#### players_account_id_totals_get.ApiResponseFor200
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
**field** | str,  | str,  | field | [optional] 
**n** | decimal.Decimal, int,  | decimal.Decimal,  | number | [optional] 
**sum** | decimal.Decimal, int,  | decimal.Decimal,  | sum | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_wardmap_get**
<a name="players_account_id_wardmap_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} players_account_id_wardmap_get(account_id)

GET /players/{account_id}/wardmap

Wards placed in matches played

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/wardmap
        api_response = api_instance.players_account_id_wardmap_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wardmap_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/wardmap
        api_response = api_instance.players_account_id_wardmap_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wardmap_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_wardmap_get.ApiResponseFor200) | Success

#### players_account_id_wardmap_get.ApiResponseFor200
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
**[obs](#obs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | obs | [optional] 
**[sen](#sen)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | sen | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# obs

obs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | obs | 

# sen

sen

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | sen | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_wl_get**
<a name="players_account_id_wl_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} players_account_id_wl_get(account_id)

GET /players/{account_id}/wl

Win/Loss count

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/wl
        api_response = api_instance.players_account_id_wl_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wl_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/wl
        api_response = api_instance.players_account_id_wl_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wl_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_wl_get.ApiResponseFor200) | Success

#### players_account_id_wl_get.ApiResponseFor200
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
**win** | decimal.Decimal, int,  | decimal.Decimal,  | Number of wins | [optional] 
**lose** | decimal.Decimal, int,  | decimal.Decimal,  | Number of loses | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_account_id_wordcloud_get**
<a name="players_account_id_wordcloud_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} players_account_id_wordcloud_get(account_id)

GET /players/{account_id}/wordcloud

Words said/read in matches played

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_id': 1,
    }
    query_params = {
    }
    try:
        # GET /players/{account_id}/wordcloud
        api_response = api_instance.players_account_id_wordcloud_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wordcloud_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_id': 1,
    }
    query_params = {
        'limit': 1,
        'offset': 1,
        'win': 1,
        'patch': 1,
        'game_mode': 1,
        'lobby_type': 1,
        'region': 1,
        'date': 1,
        'lane_role': 1,
        'hero_id': 1,
        'is_radiant': 1,
        'included_account_id': 1,
        'excluded_account_id': 1,
        'with_hero_id': 1,
        'against_hero_id': 1,
        'significant': 1,
        'having': 1,
        'sort': "sort_example",
    }
    try:
        # GET /players/{account_id}/wordcloud
        api_response = api_instance.players_account_id_wordcloud_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wordcloud_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
win | WinSchema | | optional
patch | PatchSchema | | optional
game_mode | GameModeSchema | | optional
lobby_type | LobbyTypeSchema | | optional
region | RegionSchema | | optional
date | DateSchema | | optional
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional
is_radiant | IsRadiantSchema | | optional
included_account_id | IncludedAccountIdSchema | | optional
excluded_account_id | ExcludedAccountIdSchema | | optional
with_hero_id | WithHeroIdSchema | | optional
against_hero_id | AgainstHeroIdSchema | | optional
significant | SignificantSchema | | optional
having | HavingSchema | | optional
sort | SortSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LobbyTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IsRadiantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExcludedAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WithHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# AgainstHeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SignificantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# HavingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_id | AccountIdSchema | | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_account_id_wordcloud_get.ApiResponseFor200) | Success

#### players_account_id_wordcloud_get.ApiResponseFor200
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
**[my_word_counts](#my_word_counts)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | my_word_counts | [optional] 
**[all_word_counts](#all_word_counts)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | all_word_counts | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# my_word_counts

my_word_counts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | my_word_counts | 

# all_word_counts

all_word_counts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | all_word_counts | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

