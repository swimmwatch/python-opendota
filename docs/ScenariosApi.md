# python_opendota.ScenariosApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scenarios_item_timings_get**](ScenariosApi.md#scenarios_item_timings_get) | **GET** /scenarios/itemTimings | GET /scenarios/itemTimings
[**scenarios_lane_roles_get**](ScenariosApi.md#scenarios_lane_roles_get) | **GET** /scenarios/laneRoles | GET /scenarios/laneRoles
[**scenarios_misc_get**](ScenariosApi.md#scenarios_misc_get) | **GET** /scenarios/misc | GET /scenarios/misc


# **scenarios_item_timings_get**
> [ScenarioItemTimingsResponse] scenarios_item_timings_get()

GET /scenarios/itemTimings

Win rates for certain item timings on a hero for items that cost at least 1400 gold

### Example


```python
import time
import python_opendota
from python_opendota.api import scenarios_api
from python_opendota.model.scenario_item_timings_response import ScenarioItemTimingsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scenarios_api.ScenariosApi(api_client)
    item = "item_example" # str | Filter by item name e.g. \"spirit_vessel\" (optional)
    hero_id = 1 # int | Hero ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /scenarios/itemTimings
        api_response = api_instance.scenarios_item_timings_get(item=item, hero_id=hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ScenariosApi->scenarios_item_timings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | **str**| Filter by item name e.g. \&quot;spirit_vessel\&quot; | [optional]
 **hero_id** | **int**| Hero ID | [optional]

### Return type

[**[ScenarioItemTimingsResponse]**](ScenarioItemTimingsResponse.md)

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

# **scenarios_lane_roles_get**
> [ScenarioLaneRolesResponse] scenarios_lane_roles_get()

GET /scenarios/laneRoles

Win rates for heroes in certain lane roles

### Example


```python
import time
import python_opendota
from python_opendota.api import scenarios_api
from python_opendota.model.scenario_lane_roles_response import ScenarioLaneRolesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scenarios_api.ScenariosApi(api_client)
    lane_role = "lane_role_example" # str | Filter by lane role 1-4 (Safe, Mid, Off, Jungle) (optional)
    hero_id = 1 # int | Hero ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /scenarios/laneRoles
        api_response = api_instance.scenarios_lane_roles_get(lane_role=lane_role, hero_id=hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ScenariosApi->scenarios_lane_roles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lane_role** | **str**| Filter by lane role 1-4 (Safe, Mid, Off, Jungle) | [optional]
 **hero_id** | **int**| Hero ID | [optional]

### Return type

[**[ScenarioLaneRolesResponse]**](ScenarioLaneRolesResponse.md)

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

# **scenarios_misc_get**
> [ScenarioMiscResponse] scenarios_misc_get()

GET /scenarios/misc

Miscellaneous team scenarios

### Example


```python
import time
import python_opendota
from python_opendota.api import scenarios_api
from python_opendota.model.scenario_misc_response import ScenarioMiscResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = scenarios_api.ScenariosApi(api_client)
    scenario = "scenario_example" # str | pos_chat_1min,neg_chat_1min,courier_kill,first_blood (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /scenarios/misc
        api_response = api_instance.scenarios_misc_get(scenario=scenario)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling ScenariosApi->scenarios_misc_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario** | **str**| pos_chat_1min,neg_chat_1min,courier_kill,first_blood | [optional]

### Return type

[**[ScenarioMiscResponse]**](ScenarioMiscResponse.md)

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

