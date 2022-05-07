# python_opendota.MetadataApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_get**](MetadataApi.md#metadata_get) | **GET** /metadata | GET /metadata


# **metadata_get**
> MetadataResponse metadata_get()

GET /metadata

Site metadata

### Example


```python
import time
import python_opendota
from python_opendota.api import metadata_api
from python_opendota.model.metadata_response import MetadataResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_api.MetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /metadata
        api_response = api_instance.metadata_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling MetadataApi->metadata_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataResponse**](MetadataResponse.md)

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

