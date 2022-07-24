# python_opendota.HeroesApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heroes_get**](HeroesApi.md#heroes_get) | **GET** /heroes | GET /heroes
[**heroes_hero_id_durations_get**](HeroesApi.md#heroes_hero_id_durations_get) | **GET** /heroes/{hero_id}/durations | GET /heroes/{hero_id}/durations
[**heroes_hero_id_item_popularity_get**](HeroesApi.md#heroes_hero_id_item_popularity_get) | **GET** /heroes/{hero_id}/itemPopularity | GET /heroes/{hero_id}/itemPopularity
[**heroes_hero_id_matches_get**](HeroesApi.md#heroes_hero_id_matches_get) | **GET** /heroes/{hero_id}/matches | GET /heroes/{hero_id}/matches
[**heroes_hero_id_matchups_get**](HeroesApi.md#heroes_hero_id_matchups_get) | **GET** /heroes/{hero_id}/matchups | GET /heroes/{hero_id}/matchups
[**heroes_hero_id_players_get**](HeroesApi.md#heroes_hero_id_players_get) | **GET** /heroes/{hero_id}/players | GET /heroes/{hero_id}/players


# **heroes_get**
> [HeroObjectResponse] heroes_get()

GET /heroes

Get hero data

### Example


```python
import time
import python_opendota
from python_opendota.api import heroes_api
from python_opendota.model.hero_object_response import HeroObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET /heroes
        api_response = api_instance.heroes_get()
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[HeroObjectResponse]**](HeroObjectResponse.md)

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

# **heroes_hero_id_durations_get**
> [HeroDurationsResponse] heroes_hero_id_durations_get(hero_id)

GET /heroes/{hero_id}/durations

Get hero performance over a range of match durations

### Example


```python
import time
import python_opendota
from python_opendota.api import heroes_api
from python_opendota.model.hero_durations_response import HeroDurationsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)
    hero_id = 1 # int | Hero ID

    # example passing only required values which don't have defaults set
    try:
        # GET /heroes/{hero_id}/durations
        api_response = api_instance.heroes_hero_id_durations_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_durations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID |

### Return type

[**[HeroDurationsResponse]**](HeroDurationsResponse.md)

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

# **heroes_hero_id_item_popularity_get**
> HeroItemPopularityResponse heroes_hero_id_item_popularity_get(hero_id)

GET /heroes/{hero_id}/itemPopularity

Get item popularity of hero categoried by start, early, mid and late game, analyzed from professional games

### Example


```python
import time
import python_opendota
from python_opendota.api import heroes_api
from python_opendota.model.hero_item_popularity_response import HeroItemPopularityResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)
    hero_id = 1 # int | Hero ID

    # example passing only required values which don't have defaults set
    try:
        # GET /heroes/{hero_id}/itemPopularity
        api_response = api_instance.heroes_hero_id_item_popularity_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_item_popularity_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID |

### Return type

[**HeroItemPopularityResponse**](HeroItemPopularityResponse.md)

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

# **heroes_hero_id_matches_get**
> [MatchObjectResponse] heroes_hero_id_matches_get(hero_id)

GET /heroes/{hero_id}/matches

Get recent matches with a hero

### Example


```python
import time
import python_opendota
from python_opendota.api import heroes_api
from python_opendota.model.match_object_response import MatchObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)
    hero_id = 1 # int | Hero ID

    # example passing only required values which don't have defaults set
    try:
        # GET /heroes/{hero_id}/matches
        api_response = api_instance.heroes_hero_id_matches_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID |

### Return type

[**[MatchObjectResponse]**](MatchObjectResponse.md)

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

# **heroes_hero_id_matchups_get**
> [HeroMatchupsResponse] heroes_hero_id_matchups_get(hero_id)

GET /heroes/{hero_id}/matchups

Get results against other heroes for a hero

### Example


```python
import time
import python_opendota
from python_opendota.api import heroes_api
from python_opendota.model.hero_matchups_response import HeroMatchupsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)
    hero_id = 1 # int | Hero ID

    # example passing only required values which don't have defaults set
    try:
        # GET /heroes/{hero_id}/matchups
        api_response = api_instance.heroes_hero_id_matchups_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_matchups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID |

### Return type

[**[HeroMatchupsResponse]**](HeroMatchupsResponse.md)

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

# **heroes_hero_id_players_get**
> [[PlayerObjectResponse]] heroes_hero_id_players_get(hero_id)

GET /heroes/{hero_id}/players

Get players who have played this hero

### Example


```python
import time
import python_opendota
from python_opendota.api import heroes_api
from python_opendota.model.player_object_response import PlayerObjectResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = heroes_api.HeroesApi(api_client)
    hero_id = 1 # int | Hero ID

    # example passing only required values which don't have defaults set
    try:
        # GET /heroes/{hero_id}/players
        api_response = api_instance.heroes_hero_id_players_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling HeroesApi->heroes_hero_id_players_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hero_id** | **int**| Hero ID |

### Return type

**[[PlayerObjectResponse]]**

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

