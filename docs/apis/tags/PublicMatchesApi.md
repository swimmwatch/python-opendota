<a name="__pageTop"></a>
# python_opendota.apis.tags.public_matches_api.PublicMatchesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_matches_get**](#public_matches_get) | **get** /publicMatches | GET /publicMatches

# **public_matches_get**
<a name="public_matches_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] public_matches_get()

GET /publicMatches

Get list of randomly sampled public matches

### Example

```python
import python_opendota
from python_opendota.apis.tags import public_matches_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_matches_api.PublicMatchesApi(api_client)

    # example passing only optional values
    query_params = {
        'mmr_ascending': 1,
        'mmr_descending': 1,
        'less_than_match_id': 1,
    }
    try:
        # GET /publicMatches
        api_response = api_instance.public_matches_get(
            query_params=query_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PublicMatchesApi->public_matches_get: %s\n" % e)
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
mmr_ascending | MmrAscendingSchema | | optional
mmr_descending | MmrDescendingSchema | | optional
less_than_match_id | LessThanMatchIdSchema | | optional


# MmrAscendingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MmrDescendingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LessThanMatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#public_matches_get.ApiResponseFor200) | Success

#### public_matches_get.ApiResponseFor200
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
**match_id** | decimal.Decimal, int,  | decimal.Decimal,  | match_id | [optional] 
**match_seq_num** | decimal.Decimal, int,  | decimal.Decimal,  | match_seq_num | [optional] 
**radiant_win** | bool,  | BoolClass,  | Boolean indicating whether Radiant won the match | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | start_time | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Duration of the game in seconds | [optional] 
**radiant_team** | str,  | str,  | radiant_team | [optional] 
**dire_team** | str,  | str,  | dire_team | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

