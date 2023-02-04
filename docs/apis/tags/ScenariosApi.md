<a name="__pageTop"></a>
# python_opendota.apis.tags.scenarios_api.ScenariosApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scenarios_item_timings_get**](#scenarios_item_timings_get) | **get** /scenarios/itemTimings | GET /scenarios/itemTimings
[**scenarios_lane_roles_get**](#scenarios_lane_roles_get) | **get** /scenarios/laneRoles | GET /scenarios/laneRoles
[**scenarios_misc_get**](#scenarios_misc_get) | **get** /scenarios/misc | GET /scenarios/misc

# **scenarios_item_timings_get**
<a name="scenarios_item_timings_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] scenarios_item_timings_get()

GET /scenarios/itemTimings

Win rates for certain item timings on a hero for items that cost at least 1400 gold

### Example

```python
import python_opendota
from python_opendota.apis.tags import scenarios_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenarios_api.ScenariosApi(api_client)

    # example passing only optional values
    query_params = {
        'item': "item_example",
        'hero_id': 1,
    }
    try:
        # GET /scenarios/itemTimings
        api_response = api_instance.scenarios_item_timings_get(
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ScenariosApi->scenarios_item_timings_get: %s\n" % e)
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
item | ItemSchema | | optional
hero_id | HeroIdSchema | | optional


# ItemSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#scenarios_item_timings_get.ApiResponseFor200) | Success

#### scenarios_item_timings_get.ApiResponseFor200
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
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | Hero ID | [optional] 
**item** | str,  | str,  | Purchased item | [optional] 
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Ingame time in seconds before the item was purchased | [optional] 
**games** | str,  | str,  | The number of games where the hero bought this item before this time | [optional] 
**wins** | str,  | str,  | The number of games won where the hero bought this item before this time | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **scenarios_lane_roles_get**
<a name="scenarios_lane_roles_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] scenarios_lane_roles_get()

GET /scenarios/laneRoles

Win rates for heroes in certain lane roles

### Example

```python
import python_opendota
from python_opendota.apis.tags import scenarios_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenarios_api.ScenariosApi(api_client)

    # example passing only optional values
    query_params = {
        'lane_role': "lane_role_example",
        'hero_id': 1,
    }
    try:
        # GET /scenarios/laneRoles
        api_response = api_instance.scenarios_lane_roles_get(
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ScenariosApi->scenarios_lane_roles_get: %s\n" % e)
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
lane_role | LaneRoleSchema | | optional
hero_id | HeroIdSchema | | optional


# LaneRoleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeroIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#scenarios_lane_roles_get.ApiResponseFor200) | Success

#### scenarios_lane_roles_get.ApiResponseFor200
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
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | Hero ID | [optional] 
**lane_role** | decimal.Decimal, int,  | decimal.Decimal,  | The hero&#x27;s lane role | [optional] 
**time** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum game length in seconds | [optional] 
**games** | str,  | str,  | The number of games where the hero played in this lane role | [optional] 
**wins** | str,  | str,  | The number of games won where the hero played in this lane role | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **scenarios_misc_get**
<a name="scenarios_misc_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] scenarios_misc_get()

GET /scenarios/misc

Miscellaneous team scenarios

### Example

```python
import python_opendota
from python_opendota.apis.tags import scenarios_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scenarios_api.ScenariosApi(api_client)

    # example passing only optional values
    query_params = {
        'scenario': "scenario_example",
    }
    try:
        # GET /scenarios/misc
        api_response = api_instance.scenarios_misc_get(
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ScenariosApi->scenarios_misc_get: %s\n" % e)
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
scenario | ScenarioSchema | | optional


# ScenarioSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#scenarios_misc_get.ApiResponseFor200) | Success

#### scenarios_misc_get.ApiResponseFor200
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
**scenario** | str,  | str,  | The scenario&#x27;s name or description | [optional] 
**is_radiant** | bool,  | BoolClass,  | Boolean indicating whether Radiant executed this scenario | [optional] 
**region** | decimal.Decimal, int,  | decimal.Decimal,  | Region the game was played in | [optional] 
**games** | str,  | str,  | The number of games where this scenario occurred | [optional] 
**wins** | str,  | str,  | The number of games won where this scenario occured | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

