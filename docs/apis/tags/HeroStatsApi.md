<a name="__pageTop"></a>
# python_opendota.apis.tags.hero_stats_api.HeroStatsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hero_stats_get**](#hero_stats_get) | **get** /heroStats | GET /heroStats

# **hero_stats_get**
<a name="hero_stats_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] hero_stats_get()

GET /heroStats

Get stats about hero performance in recent matches

### Example

```python
import python_opendota
from python_opendota.apis.tags import hero_stats_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hero_stats_api.HeroStatsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /heroStats
        api_response = api_instance.hero_stats_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroStatsApi->hero_stats_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#hero_stats_get.ApiResponseFor200) | Success

#### hero_stats_get.ApiResponseFor200
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
**id** | decimal.Decimal, int,  | decimal.Decimal,  | id | [optional] 
**name** | str,  | str,  | name | [optional] 
**localized_name** | str,  | str,  | localized_name | [optional] 
**img** | str,  | str,  | img | [optional] 
**icon** | str,  | str,  | icon | [optional] 
**pro_win** | decimal.Decimal, int,  | decimal.Decimal,  | pro_win | [optional] 
**pro_pick** | decimal.Decimal, int,  | decimal.Decimal,  | pro_pick | [optional] 
**hero_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID value of the hero played | [optional] 
**pro_ban** | decimal.Decimal, int,  | decimal.Decimal,  | pro_ban | [optional] 
**1_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Herald picks | [optional] 
**1_win** | decimal.Decimal, int,  | decimal.Decimal,  | Herald wins | [optional] 
**2_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Guardian picks | [optional] 
**2_win** | decimal.Decimal, int,  | decimal.Decimal,  | Guardian wins | [optional] 
**3_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Crusader picks | [optional] 
**3_win** | decimal.Decimal, int,  | decimal.Decimal,  | Crusader wins | [optional] 
**4_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Archon picks | [optional] 
**4_win** | decimal.Decimal, int,  | decimal.Decimal,  | Archon wins | [optional] 
**5_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Legend picks | [optional] 
**5_win** | decimal.Decimal, int,  | decimal.Decimal,  | Legend wins | [optional] 
**6_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Ancient picks | [optional] 
**6_win** | decimal.Decimal, int,  | decimal.Decimal,  | Ancient wins | [optional] 
**7_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Divine picks | [optional] 
**7_win** | decimal.Decimal, int,  | decimal.Decimal,  | Divine wins | [optional] 
**8_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Immortal picks | [optional] 
**8_win** | decimal.Decimal, int,  | decimal.Decimal,  | Immortal wins | [optional] 
**turbo_pick** | decimal.Decimal, int,  | decimal.Decimal,  | Picks in Turbo mode this month | [optional] 
**turbo_win** | decimal.Decimal, int,  | decimal.Decimal,  | Wins in Turbo mode this month | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

