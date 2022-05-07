# python_opendota.ConstantsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**constants_get**](ConstantsApi.md#constants_get) | **GET** /constants | GET /constants
[**constants_resource_get**](ConstantsApi.md#constants_resource_get) | **GET** /constants/{resource} | GET /constants


# **constants_get**
> [str] constants_get()

GET /constants

Gets an array of available resources.

### Example


```python
import time
import python_opendota
from python_opendota.api import constants_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
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

### Return type

**[str]**

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

# **constants_resource_get**
> [bool, date, datetime, dict, float, int, list, str, none_type] constants_resource_get(resource)

GET /constants

Get static game data mirrored from the dotaconstants repository.

### Example


```python
import time
import python_opendota
from python_opendota.api import constants_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = constants_api.ConstantsApi(api_client)
    resource = "resource_example" # str | Resource name e.g. `heroes`. [List of resources](https://github.com/odota/dotaconstants/tree/master/build)

    # example passing only required values which don't have defaults set
    try:
        # GET /constants
        api_response = api_instance.constants_resource_get(resource)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ConstantsApi->constants_resource_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource name e.g. &#x60;heroes&#x60;. [List of resources](https://github.com/odota/dotaconstants/tree/master/build) |

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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

