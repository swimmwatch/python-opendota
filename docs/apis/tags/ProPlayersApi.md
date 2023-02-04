<a name="__pageTop"></a>
# python_opendota.apis.tags.pro_players_api.ProPlayersApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pro_players_get**](#pro_players_get) | **get** /proPlayers | GET /proPlayers

# **pro_players_get**
<a name="pro_players_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] pro_players_get()

GET /proPlayers

Get list of pro players

### Example

```python
import python_opendota
from python_opendota.apis.tags import pro_players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#pro_players_get.ApiResponseFor200) | Success

#### pro_players_get.ApiResponseFor200
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

