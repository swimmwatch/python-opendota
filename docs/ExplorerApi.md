# python_opendota.ExplorerApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explorer_get**](ExplorerApi.md#explorer_get) | **GET** /explorer | GET /explorer


# **explorer_get**
> bool, date, datetime, dict, float, int, list, str, none_type explorer_get()

GET /explorer

Submit arbitrary SQL queries to the database

### Example


```python
import time
import python_opendota
from python_opendota.api import explorer_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = explorer_api.ExplorerApi(api_client)
    sql = "sql_example" # str | The PostgreSQL query as percent-encoded string. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /explorer
        api_response = api_instance.explorer_get(sql=sql)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ExplorerApi->explorer_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql** | **str**| The PostgreSQL query as percent-encoded string. | [optional]

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

