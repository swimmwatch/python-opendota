# python_opendota.DistributionsApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributions_get**](DistributionsApi.md#distributions_get) | **GET** /distributions | GET /distributions


# **distributions_get**
> DistributionsResponse distributions_get()

GET /distributions

Distributions of MMR data by bracket and country

### Example


```python
import time
import python_opendota
from python_opendota.api import distributions_api
from python_opendota.model.distributions_response import DistributionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = distributions_api.DistributionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /distributions
        api_response = api_instance.distributions_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling DistributionsApi->distributions_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DistributionsResponse**](DistributionsResponse.md)

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

