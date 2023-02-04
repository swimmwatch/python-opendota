<a name="__pageTop"></a>
# python_opendota.apis.tags.players_by_rank_api.PlayersByRankApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_by_rank_get**](#players_by_rank_get) | **get** /playersByRank | GET /playersByRank

# **players_by_rank_get**
<a name="players_by_rank_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} players_by_rank_get()

GET /playersByRank

Players ordered by rank/medal tier

### Example

```python
import python_opendota
from python_opendota.apis.tags import players_by_rank_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = players_by_rank_api.PlayersByRankApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /playersByRank
        api_response = api_instance.players_by_rank_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersByRankApi->players_by_rank_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#players_by_rank_get.ApiResponseFor200) | Success

#### players_by_rank_get.ApiResponseFor200
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
**account_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | account_id | [optional] 
**rank_tier** | decimal.Decimal, int, float,  | decimal.Decimal,  | Integer indicating the rank/medal of the player | [optional] 
**fh_unavailable** | bool,  | BoolClass,  | Indicates if we were unable to fetch full history for this player due to privacy settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

