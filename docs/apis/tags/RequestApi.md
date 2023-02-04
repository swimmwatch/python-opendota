<a name="__pageTop"></a>
# python_opendota.apis.tags.request_api.RequestApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_job_id_get**](#request_job_id_get) | **get** /request/{jobId} | GET /request/{jobId}
[**request_match_id_post**](#request_match_id_post) | **post** /request/{match_id} | POST /request/{match_id}

# **request_job_id_get**
<a name="request_job_id_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} request_job_id_get(job_id)

GET /request/{jobId}

Get parse request state

### Example

```python
import python_opendota
from python_opendota.apis.tags import request_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = request_api.RequestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'jobId': "jobId_example",
    }
    try:
        # GET /request/{jobId}
        api_response = api_instance.request_job_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling RequestApi->request_job_id_get: %s\n" % e)
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
jobId | JobIdSchema | | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#request_job_id_get.ApiResponseFor200) | Success

#### request_job_id_get.ApiResponseFor200
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

# **request_match_id_post**
<a name="request_match_id_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} request_match_id_post(match_id)

POST /request/{match_id}

Submit a new parse request

### Example

```python
import python_opendota
from python_opendota.apis.tags import request_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)

# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = request_api.RequestApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'match_id': 1,
    }
    try:
        # POST /request/{match_id}
        api_response = api_instance.request_match_id_post(
            path_params=path_params,
        )
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling RequestApi->request_match_id_post: %s\n" % e)
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
200 | [ApiResponseFor200](#request_match_id_post.ApiResponseFor200) | Success

#### request_match_id_post.ApiResponseFor200
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

