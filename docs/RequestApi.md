# python_opendota.RequestApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_job_id_get**](RequestApi.md#request_job_id_get) | **GET** /request/{jobId} | GET /request/{jobId}
[**request_match_id_post**](RequestApi.md#request_match_id_post) | **POST** /request/{match_id} | POST /request/{match_id}


# **request_job_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type request_job_id_get(job_id)

GET /request/{jobId}

Get parse request state

### Example


```python
import time
import python_opendota
from python_opendota.api import request_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_api.RequestApi(api_client)
    job_id = "jobId_example" # str | The job ID to query.

    # example passing only required values which don't have defaults set
    try:
        # GET /request/{jobId}
        api_response = api_instance.request_job_id_get(job_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling RequestApi->request_job_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID to query. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_match_id_post**
> bool, date, datetime, dict, float, int, list, str, none_type request_match_id_post(match_id)

POST /request/{match_id}

Submit a new parse request

### Example


```python
import time
import python_opendota
from python_opendota.api import request_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = request_api.RequestApi(api_client)
    match_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # POST /request/{match_id}
        api_response = api_instance.request_match_id_post(match_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling RequestApi->request_match_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

