<a name="__pageTop"></a>
# python_opendota.apis.tags.matches_api.MatchesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matches_match_id_get**](#matches_match_id_get) | **get** /matches/{match_id} | GET /matches/{match_id}

# **matches_match_id_get**
<a name="matches_match_id_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} matches_match_id_get(match_id)

GET /matches/{match_id}

Match data

### Example

```python
import python_opendota
from python_opendota.apis.tags import matches_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = matches_api.MatchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'match_id': 1,
    }
    try:
        # GET /matches/{match_id}
        api_response = api_instance.matches_match_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling MatchesApi->matches_match_id_get: %s\n" % e)
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
match_id | MatchIdSchema | | 

# MatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#matches_match_id_get.ApiResponseFor200) | Success

#### matches_match_id_get.ApiResponseFor200
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
**match_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID number of the match assigned by Valve | [optional] 
**barracks_status_dire** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmask. An integer that represents a binary of which barracks are still standing. 63 would mean all barracks still stand at the end of the game. | [optional] 
**barracks_status_radiant** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmask. An integer that represents a binary of which barracks are still standing. 63 would mean all barracks still stand at the end of the game. | [optional] 
**[chat](#chat)** | list, tuple,  | tuple,  | Array containing information on the chat of the game | [optional] 
**cluster** | decimal.Decimal, int,  | decimal.Decimal,  | cluster | [optional] 
**[cosmetics](#cosmetics)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | cosmetics | [optional] 
**dire_score** | decimal.Decimal, int,  | decimal.Decimal,  | Final score for Dire (number of kills on Radiant) | [optional] 
**[draft_timings](#draft_timings)** | list, tuple,  | tuple,  | draft_timings | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Duration of the game in seconds | [optional] 
**engine** | decimal.Decimal, int,  | decimal.Decimal,  | engine | [optional] 
**first_blood_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds at which first blood occurred | [optional] 
**game_mode** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | [optional] 
**human_players** | decimal.Decimal, int,  | decimal.Decimal,  | Number of human players in the game | [optional] 
**leagueid** | decimal.Decimal, int,  | decimal.Decimal,  | leagueid | [optional] 
**lobby_type** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | [optional] 
**match_seq_num** | decimal.Decimal, int,  | decimal.Decimal,  | match_seq_num | [optional] 
**negative_votes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of negative votes the replay received in the in-game client | [optional] 
**[objectives](#objectives)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | objectives | [optional] 
**[picks_bans](#picks_bans)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the draft. Each pick/ban contains a boolean relating to whether the choice is a pick or a ban, the hero ID, the team the picked or banned it, and the order. | [optional] 
**positive_votes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of positive votes the replay received in the in-game client | [optional] 
**[radiant_gold_adv](#radiant_gold_adv)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Array of the Radiant gold advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their gold disadvantage.  | [optional] 
**radiant_score** | decimal.Decimal, int,  | decimal.Decimal,  | Final score for Radiant (number of kills on Radiant) | [optional] 
**radiant_win** | bool,  | BoolClass,  | Boolean indicating whether Radiant won the match | [optional] 
**[radiant_xp_adv](#radiant_xp_adv)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Array of the Radiant experience advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their experience disadvantage.  | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | The Unix timestamp at which the game started | [optional] 
**[teamfights](#teamfights)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | teamfights | [optional] 
**tower_status_dire** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmask. An integer that represents a binary of which Dire towers are still standing. | [optional] 
**tower_status_radiant** | decimal.Decimal, int,  | decimal.Decimal,  | Bitmask. An integer that represents a binary of which Radiant towers are still standing. | [optional] 
**version** | decimal.Decimal, int,  | decimal.Decimal,  | Parse version, used internally by OpenDota | [optional] 
**replay_salt** | decimal.Decimal, int,  | decimal.Decimal,  | replay_salt | [optional] 
**series_id** | decimal.Decimal, int,  | decimal.Decimal,  | series_id | [optional] 
**series_type** | decimal.Decimal, int,  | decimal.Decimal,  | series_type | [optional] 
**[radiant_team](#radiant_team)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | radiant_team | [optional] 
**[dire_team](#dire_team)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | dire_team | [optional] 
**[league](#league)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | league | [optional] 
**skill** | decimal.Decimal, int,  | decimal.Decimal,  | Skill bracket assigned by Valve (Normal, High, Very High) | [optional] 
**[players](#players)** | list, tuple,  | tuple,  | Array of information on individual players | [optional] 
**patch** | decimal.Decimal, int,  | decimal.Decimal,  | Information on the patch version the game is played on | [optional] 
**region** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to the region the game was played on | [optional] 
**[all_word_counts](#all_word_counts)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Word counts of the all chat messages in the player&#x27;s games | [optional] 
**[my_word_counts](#my_word_counts)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Word counts of the player&#x27;s all chat messages | [optional] 
**throw** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum gold advantage of the player&#x27;s team if they lost the match | [optional] 
**comeback** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum gold disadvantage of the player&#x27;s team if they won the match | [optional] 
**loss** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum gold disadvantage of the player&#x27;s team if they lost the match | [optional] 
**win** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum gold advantage of the player&#x27;s team if they won the match | [optional] 
**replay_url** | str,  | str,  | replay_url | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# chat

Array containing information on the chat of the game

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing information on the chat of the game | 

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
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds at which the message was said | [optional] 
**unit** | str,  | str,  | Name of the player who sent the message | [optional] 
**key** | str,  | str,  | The message the player sent | [optional] 
**slot** | decimal.Decimal, int,  | decimal.Decimal,  | slot | [optional] 
**player_slot** | decimal.Decimal, int,  | decimal.Decimal,  | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cosmetics

cosmetics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | cosmetics | 

# draft_timings

draft_timings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | draft_timings | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | draft_stage | 

# items

draft_stage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | draft_stage | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**order** | decimal.Decimal, int,  | decimal.Decimal,  | order | [optional] 
**pick** | bool,  | BoolClass,  | pick | [optional] 
**active_team** | decimal.Decimal, int,  | decimal.Decimal,  | active_team | [optional] 
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID value of the hero played | [optional] 
**player_slot** | decimal.Decimal, int,  | decimal.Decimal,  | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**extra_time** | decimal.Decimal, int,  | decimal.Decimal,  | extra_time | [optional] 
**total_time_taken** | decimal.Decimal, int,  | decimal.Decimal,  | total_time_taken | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# objectives

objectives

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | objectives | 

# picks_bans

Object containing information on the draft. Each pick/ban contains a boolean relating to whether the choice is a pick or a ban, the hero ID, the team the picked or banned it, and the order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the draft. Each pick/ban contains a boolean relating to whether the choice is a pick or a ban, the hero ID, the team the picked or banned it, and the order. | 

# radiant_gold_adv

Array of the Radiant gold advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their gold disadvantage. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Array of the Radiant gold advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their gold disadvantage.  | 

# radiant_xp_adv

Array of the Radiant experience advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their experience disadvantage. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Array of the Radiant experience advantage at each minute in the game. A negative number means that Radiant is behind, and thus it is their experience disadvantage.  | 

# teamfights

teamfights

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | teamfights | 

# radiant_team

radiant_team

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | radiant_team | 

# dire_team

dire_team

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | dire_team | 

# league

league

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | league | 

# players

Array of information on individual players

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of information on individual players | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | player | 

# items

player

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | player | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**match_id** | decimal.Decimal, int,  | decimal.Decimal,  | Match ID | [optional] 
**player_slot** | decimal.Decimal, int,  | decimal.Decimal,  | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**[ability_upgrades_arr](#ability_upgrades_arr)** | list, tuple,  | tuple,  | An array describing how abilities were upgraded | [optional] 
**[ability_uses](#ability_uses)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how many times the played used their abilities | [optional] 
**[ability_targets](#ability_targets)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on who the player used their abilities on | [optional] 
**[damage_targets](#damage_targets)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how and how much damage the player dealt to other heroes | [optional] 
**account_id** | decimal.Decimal, int,  | decimal.Decimal,  | account_id | [optional] 
**[actions](#actions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how many and what type of actions the player issued to their hero | [optional] 
**[additional_units](#additional_units)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on additional units the player had under their control | [optional] 
**assists** | decimal.Decimal, int,  | decimal.Decimal,  | Number of assists the player had | [optional] 
**backpack_0** | decimal.Decimal, int,  | decimal.Decimal,  | Item in backpack slot 0 | [optional] 
**backpack_1** | decimal.Decimal, int,  | decimal.Decimal,  | Item in backpack slot 1 | [optional] 
**backpack_2** | decimal.Decimal, int,  | decimal.Decimal,  | Item in backpack slot 2 | [optional] 
**[buyback_log](#buyback_log)** | list, tuple,  | tuple,  | Array containing information about buybacks | [optional] 
**camps_stacked** | decimal.Decimal, int,  | decimal.Decimal,  | Number of camps stacked | [optional] 
**[connection_log](#connection_log)** | list, tuple,  | tuple,  | Array containing information about the player&#x27;s disconnections and reconnections | [optional] 
**creeps_stacked** | decimal.Decimal, int,  | decimal.Decimal,  | Number of creeps stacked | [optional] 
**[damage](#damage)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about damage dealt by the player to different units | [optional] 
**[damage_inflictor](#damage_inflictor)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about about the sources of this player&#x27;s damage to heroes | [optional] 
**[damage_inflictor_received](#damage_inflictor_received)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about the sources of damage received by this player from heroes | [optional] 
**[damage_taken](#damage_taken)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about from whom the player took damage | [optional] 
**deaths** | decimal.Decimal, int,  | decimal.Decimal,  | Number of deaths | [optional] 
**denies** | decimal.Decimal, int,  | decimal.Decimal,  | Number of denies | [optional] 
**[dn_t](#dn_t)** | list, tuple,  | tuple,  | Array containing number of denies at different times of the match | [optional] 
**gold** | decimal.Decimal, int,  | decimal.Decimal,  | Gold at the end of the game | [optional] 
**gold_per_min** | decimal.Decimal, int,  | decimal.Decimal,  | Gold Per Minute obtained by this player | [optional] 
**[gold_reasons](#gold_reasons)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how the player gainined gold over the course of the match | [optional] 
**gold_spent** | decimal.Decimal, int,  | decimal.Decimal,  | How much gold the player spent | [optional] 
**[gold_t](#gold_t)** | list, tuple,  | tuple,  | Array containing total gold at different times of the match | [optional] 
**hero_damage** | decimal.Decimal, int,  | decimal.Decimal,  | Hero Damage Dealt | [optional] 
**hero_healing** | decimal.Decimal, int,  | decimal.Decimal,  | Hero Healing Done | [optional] 
**[hero_hits](#hero_hits)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how many ticks of damages the hero inflicted with different spells and damage inflictors | [optional] 
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID value of the hero played | [optional] 
**item_0** | decimal.Decimal, int,  | decimal.Decimal,  | Item in the player&#x27;s first slot | [optional] 
**item_1** | decimal.Decimal, int,  | decimal.Decimal,  | Item in the player&#x27;s second slot | [optional] 
**item_2** | decimal.Decimal, int,  | decimal.Decimal,  | Item in the player&#x27;s third slot | [optional] 
**item_3** | decimal.Decimal, int,  | decimal.Decimal,  | Item in the player&#x27;s fourth slot | [optional] 
**item_4** | decimal.Decimal, int,  | decimal.Decimal,  | Item in the player&#x27;s fifth slot | [optional] 
**item_5** | decimal.Decimal, int,  | decimal.Decimal,  | Item in the player&#x27;s sixth slot | [optional] 
**[item_uses](#item_uses)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about how many times a player used items | [optional] 
**[kill_streaks](#kill_streaks)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about the player&#x27;s killstreaks | [optional] 
**[killed](#killed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about what units the player killed | [optional] 
**[killed_by](#killed_by)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about who killed the player | [optional] 
**kills** | decimal.Decimal, int,  | decimal.Decimal,  | Number of kills | [optional] 
**[kills_log](#kills_log)** | list, tuple,  | tuple,  | Array containing information on which hero the player killed at what time | [optional] 
**[lane_pos](#lane_pos)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on lane position | [optional] 
**last_hits** | decimal.Decimal, int,  | decimal.Decimal,  | Number of last hits | [optional] 
**leaver_status** | decimal.Decimal, int,  | decimal.Decimal,  | Integer describing whether or not the player left the game. 0: didn&#x27;t leave. 1: left safely. 2+: Abandoned | [optional] 
**level** | decimal.Decimal, int,  | decimal.Decimal,  | Level at the end of the game | [optional] 
**[lh_t](#lh_t)** | list, tuple,  | tuple,  | Array describing last hits at each minute in the game | [optional] 
**[life_state](#life_state)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | life_state | [optional] 
**[max_hero_hit](#max_hero_hit)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on the highest damage instance the player inflicted | [optional] 
**[multi_kills](#multi_kills)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on the number of the number of multikills the player had | [optional] 
**[obs](#obs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on where the player placed observer wards. The location takes the form (outer number, inner number) and are from ~64-192. | [optional] 
**[obs_left_log](#obs_left_log)** | list, tuple,  | tuple,  | obs_left_log | [optional] 
**[obs_log](#obs_log)** | list, tuple,  | tuple,  | Object containing information on when and where the player placed observer wards | [optional] 
**obs_placed** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of observer wards placed | [optional] 
**party_id** | decimal.Decimal, int,  | decimal.Decimal,  | party_id | [optional] 
**[permanent_buffs](#permanent_buffs)** | list, tuple,  | tuple,  | Array describing permanent buffs the player had at the end of the game. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/permanent_buffs.json | [optional] 
**pings** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of pings | [optional] 
**[purchase](#purchase)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the items the player purchased | [optional] 
**[purchase_log](#purchase_log)** | list, tuple,  | tuple,  | Object containing information on when items were purchased | [optional] 
**rune_pickups** | decimal.Decimal, int,  | decimal.Decimal,  | Number of runes picked up | [optional] 
**[runes](#runes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information about which runes the player picked up | [optional] 
**[runes_log](#runes_log)** | list, tuple,  | tuple,  | Array with information on when runes were picked up | [optional] 
**[sen](#sen)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on where sentries were placed. The location takes the form (outer number, inner number) and are from ~64-192. | [optional] 
**[sen_left_log](#sen_left_log)** | list, tuple,  | tuple,  | Array containing information on when and where the player placed sentries | [optional] 
**[sen_log](#sen_log)** | list, tuple,  | tuple,  | Array with information on when and where sentries were placed by the player | [optional] 
**sen_placed** | decimal.Decimal, int,  | decimal.Decimal,  | How many sentries were placed by the player | [optional] 
**stuns** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total stun duration of all stuns by the player | [optional] 
**[times](#times)** | list, tuple,  | tuple,  | Time in seconds corresponding to the time of entries of other arrays in the match. | [optional] 
**tower_damage** | decimal.Decimal, int,  | decimal.Decimal,  | Total tower damage done by the player | [optional] 
**xp_per_min** | decimal.Decimal, int,  | decimal.Decimal,  | Experience Per Minute obtained by the player | [optional] 
**[xp_reasons](#xp_reasons)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the sources of this player&#x27;s experience | [optional] 
**[xp_t](#xp_t)** | list, tuple,  | tuple,  | Experience at each minute of the game | [optional] 
**personaname** | str,  | str,  | personaname | [optional] 
**name** | str,  | str,  | name | [optional] 
**last_login** | str, datetime,  | str,  | Time of player&#x27;s last login | [optional] value must conform to RFC-3339 date-time
**radiant_win** | bool,  | BoolClass,  | Boolean indicating whether Radiant won the match | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Start time of the match in seconds since 1970 | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Duration of the game in seconds | [optional] 
**cluster** | decimal.Decimal, int,  | decimal.Decimal,  | cluster | [optional] 
**lobby_type** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to lobby type of match. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json | [optional] 
**game_mode** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to game mode played. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json | [optional] 
**patch** | decimal.Decimal, int,  | decimal.Decimal,  | Integer representing the patch the game was played on | [optional] 
**region** | decimal.Decimal, int,  | decimal.Decimal,  | Integer corresponding to the region the game was played on | [optional] 
**isRadiant** | bool,  | BoolClass,  | Boolean for whether or not the player is on Radiant | [optional] 
**win** | decimal.Decimal, int,  | decimal.Decimal,  | Binary integer representing whether or not the player won | [optional] 
**lose** | decimal.Decimal, int,  | decimal.Decimal,  | Binary integer representing whether or not the player lost | [optional] 
**total_gold** | decimal.Decimal, int,  | decimal.Decimal,  | Total gold at the end of the game | [optional] 
**total_xp** | decimal.Decimal, int,  | decimal.Decimal,  | Total experience at the end of the game | [optional] 
**kills_per_min** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of kills per minute | [optional] 
**kda** | decimal.Decimal, int, float,  | decimal.Decimal,  | kda | [optional] 
**abandons** | decimal.Decimal, int,  | decimal.Decimal,  | abandons | [optional] 
**neutral_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of neutral creeps killed | [optional] 
**tower_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of tower kills the player had | [optional] 
**courier_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of courier kills the player had | [optional] 
**lane_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of lane creeps killed by the player | [optional] 
**hero_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of heroes killed by the player | [optional] 
**observer_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of observer wards killed by the player | [optional] 
**sentry_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of sentry wards killed by the player | [optional] 
**roshan_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of roshan kills (last hit on roshan) the player had | [optional] 
**necronomicon_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of Necronomicon creeps killed by the player | [optional] 
**ancient_kills** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of Ancient creeps killed by the player | [optional] 
**buyback_count** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of buyback the player used | [optional] 
**observer_uses** | decimal.Decimal, int,  | decimal.Decimal,  | Number of observer wards used | [optional] 
**sentry_uses** | decimal.Decimal, int,  | decimal.Decimal,  | Number of sentry wards used | [optional] 
**lane_efficiency** | decimal.Decimal, int, float,  | decimal.Decimal,  | lane_efficiency | [optional] 
**lane_efficiency_pct** | decimal.Decimal, int, float,  | decimal.Decimal,  | lane_efficiency_pct | [optional] 
**lane** | decimal.Decimal, int,  | decimal.Decimal,  | Integer referring to which lane the hero laned in | [optional] 
**lane_role** | decimal.Decimal, int,  | decimal.Decimal,  | lane_role | [optional] 
**is_roaming** | bool,  | BoolClass,  | Boolean referring to whether or not the player roamed | [optional] 
**[purchase_time](#purchase_time)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on when the player last purchased an item | [optional] 
**[first_purchase_time](#first_purchase_time)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on when the player first puchased an item | [optional] 
**[item_win](#item_win)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on whether or not the item won | [optional] 
**[item_usage](#item_usage)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing binary integers the tell whether the item was purchased by the player (note: this is always 1) | [optional] 
**[purchase_tpscroll](#purchase_tpscroll)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Total number of TP scrolls purchased by the player | [optional] 
**actions_per_min** | decimal.Decimal, int,  | decimal.Decimal,  | Actions per minute | [optional] 
**life_state_dead** | decimal.Decimal, int,  | decimal.Decimal,  | life_state_dead | [optional] 
**rank_tier** | decimal.Decimal, int,  | decimal.Decimal,  | The rank tier of the player. Tens place indicates rank, ones place indicates stars. | [optional] 
**[cosmetics](#cosmetics)** | list, tuple,  | tuple,  | cosmetics | [optional] 
**[benchmarks](#benchmarks)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on certain benchmarks like GPM, XPM, KDA, tower damage, etc | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ability_upgrades_arr

An array describing how abilities were upgraded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array describing how abilities were upgraded | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ability_uses

Object containing information on how many times the played used their abilities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how many times the played used their abilities | 

# ability_targets

Object containing information on who the player used their abilities on

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on who the player used their abilities on | 

# damage_targets

Object containing information on how and how much damage the player dealt to other heroes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how and how much damage the player dealt to other heroes | 

# actions

Object containing information on how many and what type of actions the player issued to their hero

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how many and what type of actions the player issued to their hero | 

# additional_units

Object containing information on additional units the player had under their control

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on additional units the player had under their control | 

# buyback_log

Array containing information about buybacks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing information about buybacks | 

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
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds the buyback occurred | [optional] 
**slot** | decimal.Decimal, int,  | decimal.Decimal,  | slot | [optional] 
**player_slot** | decimal.Decimal, int,  | decimal.Decimal,  | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# connection_log

Array containing information about the player's disconnections and reconnections

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing information about the player&#x27;s disconnections and reconnections | 

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
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Game time in seconds the event ocurred | [optional] 
**event** | str,  | str,  | Event that occurred | [optional] 
**player_slot** | decimal.Decimal, int,  | decimal.Decimal,  | Which slot the player is in. 0-127 are Radiant, 128-255 are Dire | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# damage

Object containing information about damage dealt by the player to different units

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about damage dealt by the player to different units | 

# damage_inflictor

Object containing information about about the sources of this player's damage to heroes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about about the sources of this player&#x27;s damage to heroes | 

# damage_inflictor_received

Object containing information about the sources of damage received by this player from heroes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about the sources of damage received by this player from heroes | 

# damage_taken

Object containing information about from whom the player took damage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about from whom the player took damage | 

# dn_t

Array containing number of denies at different times of the match

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing number of denies at different times of the match | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# gold_reasons

Object containing information on how the player gainined gold over the course of the match

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how the player gainined gold over the course of the match | 

# gold_t

Array containing total gold at different times of the match

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing total gold at different times of the match | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# hero_hits

Object containing information on how many ticks of damages the hero inflicted with different spells and damage inflictors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on how many ticks of damages the hero inflicted with different spells and damage inflictors | 

# item_uses

Object containing information about how many times a player used items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about how many times a player used items | 

# kill_streaks

Object containing information about the player's killstreaks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about the player&#x27;s killstreaks | 

# killed

Object containing information about what units the player killed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about what units the player killed | 

# killed_by

Object containing information about who killed the player

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information about who killed the player | 

# kills_log

Array containing information on which hero the player killed at what time

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing information on which hero the player killed at what time | 

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
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds the player killed the hero | [optional] 
**key** | str,  | str,  | Hero killed | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lane_pos

Object containing information on lane position

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on lane position | 

# lh_t

Array describing last hits at each minute in the game

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array describing last hits at each minute in the game | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# life_state

life_state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | life_state | 

# max_hero_hit

Object with information on the highest damage instance the player inflicted

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on the highest damage instance the player inflicted | 

# multi_kills

Object with information on the number of the number of multikills the player had

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on the number of the number of multikills the player had | 

# obs

Object with information on where the player placed observer wards. The location takes the form (outer number, inner number) and are from ~64-192.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on where the player placed observer wards. The location takes the form (outer number, inner number) and are from ~64-192. | 

# obs_left_log

obs_left_log

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | obs_left_log | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# obs_log

Object containing information on when and where the player placed observer wards

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Object containing information on when and where the player placed observer wards | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# permanent_buffs

Array describing permanent buffs the player had at the end of the game. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/permanent_buffs.json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array describing permanent buffs the player had at the end of the game. List of constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/permanent_buffs.json | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# purchase

Object containing information on the items the player purchased

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the items the player purchased | 

# purchase_log

Object containing information on when items were purchased

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Object containing information on when items were purchased | 

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
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds the item was bought | [optional] 
**key** | str,  | str,  | String item ID | [optional] 
**charges** | decimal.Decimal, int,  | decimal.Decimal,  | Integer amount of charges | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# runes

Object with information about which runes the player picked up

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information about which runes the player picked up | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] 

# runes_log

Array with information on when runes were picked up

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array with information on when runes were picked up | 

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
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds rune picked up | [optional] 
**key** | decimal.Decimal, int,  | decimal.Decimal,  | key | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sen

Object with information on where sentries were placed. The location takes the form (outer number, inner number) and are from ~64-192.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on where sentries were placed. The location takes the form (outer number, inner number) and are from ~64-192. | 

# sen_left_log

Array containing information on when and where the player placed sentries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing information on when and where the player placed sentries | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# sen_log

Array with information on when and where sentries were placed by the player

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array with information on when and where sentries were placed by the player | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# times

Time in seconds corresponding to the time of entries of other arrays in the match.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Time in seconds corresponding to the time of entries of other arrays in the match. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# xp_reasons

Object containing information on the sources of this player's experience

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on the sources of this player&#x27;s experience | 

# xp_t

Experience at each minute of the game

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Experience at each minute of the game | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# purchase_time

Object with information on when the player last purchased an item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on when the player last purchased an item | 

# first_purchase_time

Object with information on when the player first puchased an item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on when the player first puchased an item | 

# item_win

Object with information on whether or not the item won

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with information on whether or not the item won | 

# item_usage

Object containing binary integers the tell whether the item was purchased by the player (note: this is always 1)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing binary integers the tell whether the item was purchased by the player (note: this is always 1) | 

# purchase_tpscroll

Total number of TP scrolls purchased by the player

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Total number of TP scrolls purchased by the player | 

# cosmetics

cosmetics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | cosmetics | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# benchmarks

Object containing information on certain benchmarks like GPM, XPM, KDA, tower damage, etc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object containing information on certain benchmarks like GPM, XPM, KDA, tower damage, etc | 

# all_word_counts

Word counts of the all chat messages in the player's games

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Word counts of the all chat messages in the player&#x27;s games | 

# my_word_counts

Word counts of the player's all chat messages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Word counts of the player&#x27;s all chat messages | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

