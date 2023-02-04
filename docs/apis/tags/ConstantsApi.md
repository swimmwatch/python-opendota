<a name="__pageTop"></a>
# python_opendota.apis.tags.constants_api.ConstantsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**constants_get**](#constants_get) | **get** /constants | GET /constants
[**constants_resource_get**](#constants_resource_get) | **get** /constants/{resource} | GET /constants

# **constants_get**
<a name="constants_get"></a>
> [str] constants_get()

GET /constants

Gets an array of available resources.

### Example

```python
import python_opendota
from python_opendota.apis.tags import constants_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = constants_api.ConstantsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /constants
        api_response = api_instance.constants_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ConstantsApi->constants_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#constants_get.ApiResponseFor200) | Success

#### constants_get.ApiResponseFor200
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
items | str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **constants_resource_get**
<a name="constants_resource_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] constants_resource_get(resource)

GET /constants

Get static game data mirrored from the dotaconstants repository.

### Example

```python
import python_opendota
from python_opendota.apis.tags import constants_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = constants_api.ConstantsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'resource': "resource_example",
    }
    try:
        # GET /constants
        api_response = api_instance.constants_resource_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ConstantsApi->constants_resource_get: %s\n" % e)
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
resource | ResourceSchema | | 

# ResourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#constants_resource_get.ApiResponseFor200) | Success

#### constants_resource_get.ApiResponseFor200
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

