# python_opendota.PlayersApi

All URIs are relative to *http://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_account_id_counts_get**](PlayersApi.md#players_account_id_counts_get) | **GET** /players/{account_id}/counts | GET /players/{account_id}/counts
[**players_account_id_get**](PlayersApi.md#players_account_id_get) | **GET** /players/{account_id} | GET /players/{account_id}
[**players_account_id_heroes_get**](PlayersApi.md#players_account_id_heroes_get) | **GET** /players/{account_id}/heroes | GET /players/{account_id}/heroes
[**players_account_id_histograms_field_get**](PlayersApi.md#players_account_id_histograms_field_get) | **GET** /players/{account_id}/histograms/{field} | GET /players/{account_id}/histograms
[**players_account_id_matches_get**](PlayersApi.md#players_account_id_matches_get) | **GET** /players/{account_id}/matches | GET /players/{account_id}/matches
[**players_account_id_peers_get**](PlayersApi.md#players_account_id_peers_get) | **GET** /players/{account_id}/peers | GET /players/{account_id}/peers
[**players_account_id_pros_get**](PlayersApi.md#players_account_id_pros_get) | **GET** /players/{account_id}/pros | GET /players/{account_id}/pros
[**players_account_id_rankings_get**](PlayersApi.md#players_account_id_rankings_get) | **GET** /players/{account_id}/rankings | GET /players/{account_id}/rankings
[**players_account_id_ratings_get**](PlayersApi.md#players_account_id_ratings_get) | **GET** /players/{account_id}/ratings | GET /players/{account_id}/ratings
[**players_account_id_recent_matches_get**](PlayersApi.md#players_account_id_recent_matches_get) | **GET** /players/{account_id}/recentMatches | GET /players/{account_id}/recentMatches
[**players_account_id_refresh_post**](PlayersApi.md#players_account_id_refresh_post) | **POST** /players/{account_id}/refresh | POST /players/{account_id}/refresh
[**players_account_id_totals_get**](PlayersApi.md#players_account_id_totals_get) | **GET** /players/{account_id}/totals | GET /players/{account_id}/totals
[**players_account_id_wardmap_get**](PlayersApi.md#players_account_id_wardmap_get) | **GET** /players/{account_id}/wardmap | GET /players/{account_id}/wardmap
[**players_account_id_wl_get**](PlayersApi.md#players_account_id_wl_get) | **GET** /players/{account_id}/wl | GET /players/{account_id}/wl
[**players_account_id_wordcloud_get**](PlayersApi.md#players_account_id_wordcloud_get) | **GET** /players/{account_id}/wordcloud | GET /players/{account_id}/wordcloud


# **players_account_id_counts_get**
> PlayerCountsResponse players_account_id_counts_get(account_id)

GET /players/{account_id}/counts

Counts in categories

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_counts_response import PlayerCountsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/counts
        api_response = api_instance.players_account_id_counts_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_counts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/counts
        api_response = api_instance.players_account_id_counts_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_counts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**PlayerCountsResponse**](PlayerCountsResponse.md)

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

# **players_account_id_get**
> PlayerResponse players_account_id_get(account_id)

GET /players/{account_id}

Player data

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_response import PlayerResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}
        api_response = api_instance.players_account_id_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |

### Return type

[**PlayerResponse**](PlayerResponse.md)

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

# **players_account_id_heroes_get**
> [PlayerHeroesResponse] players_account_id_heroes_get(account_id)

GET /players/{account_id}/heroes

Heroes played

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_heroes_response import PlayerHeroesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/heroes
        api_response = api_instance.players_account_id_heroes_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_heroes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/heroes
        api_response = api_instance.players_account_id_heroes_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_heroes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**[PlayerHeroesResponse]**](PlayerHeroesResponse.md)

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

# **players_account_id_histograms_field_get**
> [bool, date, datetime, dict, float, int, list, str, none_type] players_account_id_histograms_field_get(account_id, field)

GET /players/{account_id}/histograms

Distribution of matches in a single stat

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    field = "field_example" # str | Field to aggregate on
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/histograms
        api_response = api_instance.players_account_id_histograms_field_get(account_id, field)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_histograms_field_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/histograms
        api_response = api_instance.players_account_id_histograms_field_get(account_id, field, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_histograms_field_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **field** | **str**| Field to aggregate on |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

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

# **players_account_id_matches_get**
> [PlayerMatchesResponse] players_account_id_matches_get(account_id)

GET /players/{account_id}/matches

Matches played

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_matches_response import PlayerMatchesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)
    project = "project_example" # str | Fields to project (array) (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/matches
        api_response = api_instance.players_account_id_matches_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_matches_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/matches
        api_response = api_instance.players_account_id_matches_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort, project=project)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]
 **project** | **str**| Fields to project (array) | [optional]

### Return type

[**[PlayerMatchesResponse]**](PlayerMatchesResponse.md)

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

# **players_account_id_peers_get**
> [PlayerPeersResponse] players_account_id_peers_get(account_id)

GET /players/{account_id}/peers

Players played with

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_peers_response import PlayerPeersResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/peers
        api_response = api_instance.players_account_id_peers_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_peers_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/peers
        api_response = api_instance.players_account_id_peers_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_peers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**[PlayerPeersResponse]**](PlayerPeersResponse.md)

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

# **players_account_id_pros_get**
> [PlayerProsResponse] players_account_id_pros_get(account_id)

GET /players/{account_id}/pros

Pro players played with

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_pros_response import PlayerProsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/pros
        api_response = api_instance.players_account_id_pros_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_pros_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/pros
        api_response = api_instance.players_account_id_pros_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_pros_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**[PlayerProsResponse]**](PlayerProsResponse.md)

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

# **players_account_id_rankings_get**
> [PlayerRankingsResponse] players_account_id_rankings_get(account_id)

GET /players/{account_id}/rankings

Player hero rankings

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_rankings_response import PlayerRankingsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/rankings
        api_response = api_instance.players_account_id_rankings_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_rankings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |

### Return type

[**[PlayerRankingsResponse]**](PlayerRankingsResponse.md)

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

# **players_account_id_ratings_get**
> [PlayerRatingsResponse] players_account_id_ratings_get(account_id)

GET /players/{account_id}/ratings

Player rating history

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_ratings_response import PlayerRatingsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/ratings
        api_response = api_instance.players_account_id_ratings_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_ratings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |

### Return type

[**[PlayerRatingsResponse]**](PlayerRatingsResponse.md)

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

# **players_account_id_recent_matches_get**
> [PlayerRecentMatchesResponse] players_account_id_recent_matches_get(account_id)

GET /players/{account_id}/recentMatches

Recent matches played

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_recent_matches_response import PlayerRecentMatchesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/recentMatches
        api_response = api_instance.players_account_id_recent_matches_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_recent_matches_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |

### Return type

[**[PlayerRecentMatchesResponse]**](PlayerRecentMatchesResponse.md)

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

# **players_account_id_refresh_post**
> bool, date, datetime, dict, float, int, list, str, none_type players_account_id_refresh_post(account_id)

POST /players/{account_id}/refresh

Refresh player match history

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID

    # example passing only required values which don't have defaults set
    try:
        # POST /players/{account_id}/refresh
        api_response = api_instance.players_account_id_refresh_post(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_refresh_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |

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

# **players_account_id_totals_get**
> [PlayerTotalsResponse] players_account_id_totals_get(account_id)

GET /players/{account_id}/totals

Totals in stats

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_totals_response import PlayerTotalsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/totals
        api_response = api_instance.players_account_id_totals_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_totals_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/totals
        api_response = api_instance.players_account_id_totals_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_totals_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**[PlayerTotalsResponse]**](PlayerTotalsResponse.md)

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

# **players_account_id_wardmap_get**
> PlayerWardMapResponse players_account_id_wardmap_get(account_id)

GET /players/{account_id}/wardmap

Wards placed in matches played

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_ward_map_response import PlayerWardMapResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/wardmap
        api_response = api_instance.players_account_id_wardmap_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wardmap_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/wardmap
        api_response = api_instance.players_account_id_wardmap_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wardmap_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**PlayerWardMapResponse**](PlayerWardMapResponse.md)

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

# **players_account_id_wl_get**
> PlayerWinLossResponse players_account_id_wl_get(account_id)

GET /players/{account_id}/wl

Win/Loss count

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_win_loss_response import PlayerWinLossResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/wl
        api_response = api_instance.players_account_id_wl_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wl_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/wl
        api_response = api_instance.players_account_id_wl_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wl_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**PlayerWinLossResponse**](PlayerWinLossResponse.md)

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

# **players_account_id_wordcloud_get**
> PlayerWordCloudResponse players_account_id_wordcloud_get(account_id)

GET /players/{account_id}/wordcloud

Words said/read in matches played

### Example


```python
import time
import python_opendota
from python_opendota.api import players_api
from python_opendota.model.player_word_cloud_response import PlayerWordCloudResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    account_id = 1 # int | Steam32 account ID
    limit = 1 # int | Number of matches to limit to (optional)
    offset = 1 # int | Number of matches to offset start by (optional)
    win = 1 # int | Whether the player won (optional)
    patch = 1 # int | Patch ID (optional)
    game_mode = 1 # int | Game Mode ID (optional)
    lobby_type = 1 # int | Lobby type ID (optional)
    region = 1 # int | Region ID (optional)
    date = 1 # int | Days previous (optional)
    lane_role = 1 # int | Lane Role ID (optional)
    hero_id = 1 # int | Hero ID (optional)
    is_radiant = 1 # int | Whether the player was radiant (optional)
    included_account_id = 1 # int | Account IDs in the match (array) (optional)
    excluded_account_id = 1 # int | Account IDs not in the match (array) (optional)
    with_hero_id = 1 # int | Hero IDs on the player's team (array) (optional)
    against_hero_id = 1 # int | Hero IDs against the player's team (array) (optional)
    significant = 1 # int | Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. (optional)
    having = 1 # int | The minimum number of games played, for filtering hero stats (optional)
    sort = "sort_example" # str | The field to return matches sorted by in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET /players/{account_id}/wordcloud
        api_response = api_instance.players_account_id_wordcloud_get(account_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wordcloud_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET /players/{account_id}/wordcloud
        api_response = api_instance.players_account_id_wordcloud_get(account_id, limit=limit, offset=offset, win=win, patch=patch, game_mode=game_mode, lobby_type=lobby_type, region=region, date=date, lane_role=lane_role, hero_id=hero_id, is_radiant=is_radiant, included_account_id=included_account_id, excluded_account_id=excluded_account_id, with_hero_id=with_hero_id, against_hero_id=against_hero_id, significant=significant, having=having, sort=sort)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling PlayersApi->players_account_id_wordcloud_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Steam32 account ID |
 **limit** | **int**| Number of matches to limit to | [optional]
 **offset** | **int**| Number of matches to offset start by | [optional]
 **win** | **int**| Whether the player won | [optional]
 **patch** | **int**| Patch ID | [optional]
 **game_mode** | **int**| Game Mode ID | [optional]
 **lobby_type** | **int**| Lobby type ID | [optional]
 **region** | **int**| Region ID | [optional]
 **date** | **int**| Days previous | [optional]
 **lane_role** | **int**| Lane Role ID | [optional]
 **hero_id** | **int**| Hero ID | [optional]
 **is_radiant** | **int**| Whether the player was radiant | [optional]
 **included_account_id** | **int**| Account IDs in the match (array) | [optional]
 **excluded_account_id** | **int**| Account IDs not in the match (array) | [optional]
 **with_hero_id** | **int**| Hero IDs on the player&#39;s team (array) | [optional]
 **against_hero_id** | **int**| Hero IDs against the player&#39;s team (array) | [optional]
 **significant** | **int**| Whether the match was significant for aggregation purposes. Defaults to 1 (true), set this to 0 to return data for non-standard modes/matches. | [optional]
 **having** | **int**| The minimum number of games played, for filtering hero stats | [optional]
 **sort** | **str**| The field to return matches sorted by in descending order | [optional]

### Return type

[**PlayerWordCloudResponse**](PlayerWordCloudResponse.md)

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

