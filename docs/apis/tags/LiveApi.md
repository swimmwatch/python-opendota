<a name="__pageTop"></a>
# python_opendota.apis.tags.live_api.LiveApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**live_get**](#live_get) | **get** /live | GET /live

# **live_get**
<a name="live_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] live_get()

GET /live

Get top currently ongoing live games

### Example

```python
import python_opendota
from python_opendota.apis.tags import live_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = live_api.LiveApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /live
        api_response = api_instance.live_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling LiveApi->live_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#live_get.ApiResponseFor200) | Success

#### live_get.ApiResponseFor200
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

