# python_opendota.RecordsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**records_field_get**](RecordsApi.md#records_field_get) | **GET** /records/{field} | GET /records/{field}


# **records_field_get**
> [RecordsResponse] records_field_get(field)

GET /records/{field}

Get top performances in a stat

### Example


```python
import time
import python_opendota
from python_opendota.api import records_api
from python_opendota.model.records_response import RecordsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)
    field = "field_example" # str | Field name to query

    # example passing only required values which don't have defaults set
    try:
        # GET /records/{field}
        api_response = api_instance.records_field_get(field)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling RecordsApi->records_field_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Field name to query |

### Return type

[**[RecordsResponse]**](RecordsResponse.md)

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

