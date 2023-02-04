<a name="__pageTop"></a>
# python_opendota.apis.tags.heroes_api.HeroesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heroes_get**](#heroes_get) | **get** /heroes | GET /heroes
[**heroes_hero_id_durations_get**](#heroes_hero_id_durations_get) | **get** /heroes/{hero_id}/durations | GET /heroes/{hero_id}/durations
[**heroes_hero_id_item_popularity_get**](#heroes_hero_id_item_popularity_get) | **get** /heroes/{hero_id}/itemPopularity | GET /heroes/{hero_id}/itemPopularity
[**heroes_hero_id_matches_get**](#heroes_hero_id_matches_get) | **get** /heroes/{hero_id}/matches | GET /heroes/{hero_id}/matches
[**heroes_hero_id_matchups_get**](#heroes_hero_id_matchups_get) | **get** /heroes/{hero_id}/matchups | GET /heroes/{hero_id}/matchups
[**heroes_hero_id_players_get**](#heroes_hero_id_players_get) | **get** /heroes/{hero_id}/players | GET /heroes/{hero_id}/players

# **heroes_get**
<a name="heroes_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] heroes_get()

GET /heroes

Get hero data

### Example

```python
import python_opendota
from python_opendota.apis.tags import heroes_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /heroes
        api_response = api_instance.heroes_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#heroes_get.ApiResponseFor200) | Success

#### heroes_get.ApiResponseFor200
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
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Numeric identifier for the hero object | [optional] 
**name** | str,  | str,  | Dota hero command name, e.g. &#x27;npc_dota_hero_antimage&#x27; | [optional] 
**localized_name** | str,  | str,  | Hero name, e.g. &#x27;Anti-Mage&#x27; | [optional] 
**primary_attr** | str,  | str,  | Hero primary shorthand attribute name, e.g. &#x27;agi&#x27; | [optional] 
**attack_type** | str,  | str,  | Hero attack type, either &#x27;Melee&#x27; or &#x27;Ranged&#x27; | [optional] 
**[roles](#roles)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# roles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | A hero&#x27;s role in the game | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **heroes_hero_id_durations_get**
<a name="heroes_hero_id_durations_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] heroes_hero_id_durations_get(hero_id)

GET /heroes/{hero_id}/durations

Get hero performance over a range of match durations

### Example

```python
import python_opendota
from python_opendota.apis.tags import heroes_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'hero_id': 1,
    }
    try:
        # GET /heroes/{hero_id}/durations
        api_response = api_instance.heroes_hero_id_durations_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_durations_get: %s\n" % e)
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
hero_id | HeroIdSchema | | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#heroes_hero_id_durations_get.ApiResponseFor200) | Success

#### heroes_hero_id_durations_get.ApiResponseFor200
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
**duration_bin** | str,  | str,  | Lower bound of number of seconds the match lasted | [optional] 
**games_played** | decimal.Decimal, int,  | decimal.Decimal,  | Number of games played | [optional] 
**wins** | decimal.Decimal, int,  | decimal.Decimal,  | Number of wins | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **heroes_hero_id_item_popularity_get**
<a name="heroes_hero_id_item_popularity_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} heroes_hero_id_item_popularity_get(hero_id)

GET /heroes/{hero_id}/itemPopularity

Get item popularity of hero categoried by start, early, mid and late game, analyzed from professional games

### Example

```python
import python_opendota
from python_opendota.apis.tags import heroes_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'hero_id': 1,
    }
    try:
        # GET /heroes/{hero_id}/itemPopularity
        api_response = api_instance.heroes_hero_id_item_popularity_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_item_popularity_get: %s\n" % e)
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
hero_id | HeroIdSchema | | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#heroes_hero_id_item_popularity_get.ApiResponseFor200) | Success

#### heroes_hero_id_item_popularity_get.ApiResponseFor200
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
**[start_game_items](#start_game_items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought before game started | [optional] 
**[early_game_items](#early_game_items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought in the first 10 min of the game, with cost at least 700 | [optional] 
**[mid_game_items](#mid_game_items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought between 10 and 25 min of the game, with cost at least 2000 | [optional] 
**[late_game_items](#late_game_items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought at least 25 min after game started, with cost at least 4000 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# start_game_items

Items bought before game started

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought before game started | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | decimal.Decimal, int,  | decimal.Decimal,  | Number of item bought | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# early_game_items

Items bought in the first 10 min of the game, with cost at least 700

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought in the first 10 min of the game, with cost at least 700 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | decimal.Decimal, int,  | decimal.Decimal,  | Number of item bought | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mid_game_items

Items bought between 10 and 25 min of the game, with cost at least 2000

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought between 10 and 25 min of the game, with cost at least 2000 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | decimal.Decimal, int,  | decimal.Decimal,  | Number of item bought | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# late_game_items

Items bought at least 25 min after game started, with cost at least 4000

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Items bought at least 25 min after game started, with cost at least 4000 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**item** | decimal.Decimal, int,  | decimal.Decimal,  | Number of item bought | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **heroes_hero_id_matches_get**
<a name="heroes_hero_id_matches_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] heroes_hero_id_matches_get(hero_id)

GET /heroes/{hero_id}/matches

Get recent matches with a hero

### Example

```python
import python_opendota
from python_opendota.apis.tags import heroes_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'hero_id': 1,
    }
    try:
        # GET /heroes/{hero_id}/matches
        api_response = api_instance.heroes_hero_id_matches_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_matches_get: %s\n" % e)
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
hero_id | HeroIdSchema | | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#heroes_hero_id_matches_get.ApiResponseFor200) | Success

#### heroes_hero_id_matches_get.ApiResponseFor200
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

# **heroes_hero_id_matchups_get**
<a name="heroes_hero_id_matchups_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] heroes_hero_id_matchups_get(hero_id)

GET /heroes/{hero_id}/matchups

Get results against other heroes for a hero

### Example

```python
import python_opendota
from python_opendota.apis.tags import heroes_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'hero_id': 1,
    }
    try:
        # GET /heroes/{hero_id}/matchups
        api_response = api_instance.heroes_hero_id_matchups_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_matchups_get: %s\n" % e)
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
hero_id | HeroIdSchema | | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#heroes_hero_id_matchups_get.ApiResponseFor200) | Success

#### heroes_hero_id_matchups_get.ApiResponseFor200
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
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | Numeric identifier for the hero object | [optional] 
**games_played** | decimal.Decimal, int,  | decimal.Decimal,  | Number of games played | [optional] 
**wins** | decimal.Decimal, int,  | decimal.Decimal,  | Number of games won | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **heroes_hero_id_players_get**
<a name="heroes_hero_id_players_get"></a>
> [[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]] heroes_hero_id_players_get(hero_id)

GET /heroes/{hero_id}/players

Get players who have played this hero

### Example

```python
import python_opendota
from python_opendota.apis.tags import heroes_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'hero_id': 1,
    }
    try:
        # GET /heroes/{hero_id}/players
        api_response = api_instance.heroes_hero_id_players_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_players_get: %s\n" % e)
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
hero_id | HeroIdSchema | | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#heroes_hero_id_players_get.ApiResponseFor200) | Success

#### heroes_hero_id_players_get.ApiResponseFor200
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
[items](#items) | list, tuple,  | tuple,  |  | 

# items

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
**account_id** | decimal.Decimal, int,  | decimal.Decimal,  | Player&#x27;s account identifier | [optional] 
**steamid** | str,  | str,  | Player&#x27;s steam identifier | [optional] 
**avatar** | str,  | str,  | Steam picture URL (small picture) | [optional] 
**avatarmedium** | str,  | str,  | Steam picture URL (medium picture) | [optional] 
**avatarfull** | str,  | str,  | Steam picture URL (full picture) | [optional] 
**profileurl** | str,  | str,  | Steam profile URL | [optional] 
**personaname** | str,  | str,  | Player&#x27;s Steam name | [optional] 
**last_login** | str, datetime,  | str,  | Date and time of last login to OpenDota | [optional] value must conform to RFC-3339 date-time
**full_history_time** | str, datetime,  | str,  | Date and time of last request to refresh player&#x27;s match history | [optional] value must conform to RFC-3339 date-time
**cheese** | decimal.Decimal, int,  | decimal.Decimal,  | Amount of dollars the player has donated to OpenDota | [optional] 
**fh_unavailable** | bool,  | BoolClass,  | Whether the refresh of player&#x27; match history failed | [optional] 
**loccountrycode** | str,  | str,  | Player&#x27;s country identifier, e.g. US | [optional] 
**name** | str,  | str,  | Verified player name, e.g. &#x27;Miracle-&#x27; | [optional] 
**country_code** | str,  | str,  | Player&#x27;s country code | [optional] 
**fantasy_role** | decimal.Decimal, int,  | decimal.Decimal,  | Player&#x27;s ingame role (core: 1 or support: 2) | [optional] 
**team_id** | decimal.Decimal, int,  | decimal.Decimal,  | Player&#x27;s team identifier | [optional] 
**team_name** | str,  | str,  | Player&#x27;s team name, e.g. &#x27;Evil Geniuses&#x27; | [optional] 
**team_tag** | str,  | str,  | Player&#x27;s team shorthand tag, e.g. &#x27;EG&#x27; | [optional] 
**is_locked** | bool,  | BoolClass,  | Whether the roster lock is active | [optional] 
**is_pro** | bool,  | BoolClass,  | Whether the player is professional or not | [optional] 
**locked_until** | decimal.Decimal, int,  | decimal.Decimal,  | When the roster lock will end | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

