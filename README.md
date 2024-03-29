# python-opendota
# Introduction
The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.

You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.

**Beginning 2018-04-22, the OpenDota API is limited to 50,000 free calls per month and 60 requests/minute** We offer a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 19.0.0
- Package version: 3.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/swimmwatch/python-opendota.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/swimmwatch/python-opendota.git`)

Then import the package:
```python
import python_opendota
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import python_opendota
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import python_opendota
from pprint import pprint
from python_opendota.apis.tags import benchmarks_api
# Defining the host is optional and defaults to http://api.opendota.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = python_opendota.Configuration(
    host = "http://api.opendota.com/api"
)


# Enter a context with an instance of the API client
with python_opendota.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = benchmarks_api.BenchmarksApi(api_client)
    hero_id = "hero_id_example" # str | Hero ID

    try:
        # GET /benchmarks
        api_response = api_instance.benchmarks_get(hero_id)
        pprint(api_response)
    except python_opendota.ApiException as e:
        print("Exception when calling BenchmarksApi->benchmarks_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api.opendota.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BenchmarksApi* | [**benchmarks_get**](docs/apis/tags/BenchmarksApi.md#benchmarks_get) | **get** /benchmarks | GET /benchmarks
*ConstantsApi* | [**constants_get**](docs/apis/tags/ConstantsApi.md#constants_get) | **get** /constants | GET /constants
*ConstantsApi* | [**constants_resource_get**](docs/apis/tags/ConstantsApi.md#constants_resource_get) | **get** /constants/{resource} | GET /constants
*DistributionsApi* | [**distributions_get**](docs/apis/tags/DistributionsApi.md#distributions_get) | **get** /distributions | GET /distributions
*ExplorerApi* | [**explorer_get**](docs/apis/tags/ExplorerApi.md#explorer_get) | **get** /explorer | GET /explorer
*FindMatchesApi* | [**find_matches_get**](docs/apis/tags/FindMatchesApi.md#find_matches_get) | **get** /findMatches | GET /
*HealthApi* | [**health_get**](docs/apis/tags/HealthApi.md#health_get) | **get** /health | GET /health
*HeroStatsApi* | [**hero_stats_get**](docs/apis/tags/HeroStatsApi.md#hero_stats_get) | **get** /heroStats | GET /heroStats
*HeroesApi* | [**heroes_get**](docs/apis/tags/HeroesApi.md#heroes_get) | **get** /heroes | GET /heroes
*HeroesApi* | [**heroes_hero_id_durations_get**](docs/apis/tags/HeroesApi.md#heroes_hero_id_durations_get) | **get** /heroes/{hero_id}/durations | GET /heroes/{hero_id}/durations
*HeroesApi* | [**heroes_hero_id_item_popularity_get**](docs/apis/tags/HeroesApi.md#heroes_hero_id_item_popularity_get) | **get** /heroes/{hero_id}/itemPopularity | GET /heroes/{hero_id}/itemPopularity
*HeroesApi* | [**heroes_hero_id_matches_get**](docs/apis/tags/HeroesApi.md#heroes_hero_id_matches_get) | **get** /heroes/{hero_id}/matches | GET /heroes/{hero_id}/matches
*HeroesApi* | [**heroes_hero_id_matchups_get**](docs/apis/tags/HeroesApi.md#heroes_hero_id_matchups_get) | **get** /heroes/{hero_id}/matchups | GET /heroes/{hero_id}/matchups
*HeroesApi* | [**heroes_hero_id_players_get**](docs/apis/tags/HeroesApi.md#heroes_hero_id_players_get) | **get** /heroes/{hero_id}/players | GET /heroes/{hero_id}/players
*LeaguesApi* | [**leagues_get**](docs/apis/tags/LeaguesApi.md#leagues_get) | **get** /leagues | GET /leagues
*LeaguesApi* | [**leagues_league_id_get**](docs/apis/tags/LeaguesApi.md#leagues_league_id_get) | **get** /leagues/{league_id} | GET /leagues/{league_id}
*LeaguesApi* | [**leagues_league_id_matches_get**](docs/apis/tags/LeaguesApi.md#leagues_league_id_matches_get) | **get** /leagues/{league_id}/matches | GET /leagues/{league_id}/matches
*LeaguesApi* | [**leagues_league_id_teams_get**](docs/apis/tags/LeaguesApi.md#leagues_league_id_teams_get) | **get** /leagues/{league_id}/teams | GET /leagues/{league_id}/teams
*LiveApi* | [**live_get**](docs/apis/tags/LiveApi.md#live_get) | **get** /live | GET /live
*MatchesApi* | [**matches_match_id_get**](docs/apis/tags/MatchesApi.md#matches_match_id_get) | **get** /matches/{match_id} | GET /matches/{match_id}
*MetadataApi* | [**metadata_get**](docs/apis/tags/MetadataApi.md#metadata_get) | **get** /metadata | GET /metadata
*ParsedMatchesApi* | [**parsed_matches_get**](docs/apis/tags/ParsedMatchesApi.md#parsed_matches_get) | **get** /parsedMatches | GET /parsedMatches
*PlayersApi* | [**players_account_id_counts_get**](docs/apis/tags/PlayersApi.md#players_account_id_counts_get) | **get** /players/{account_id}/counts | GET /players/{account_id}/counts
*PlayersApi* | [**players_account_id_get**](docs/apis/tags/PlayersApi.md#players_account_id_get) | **get** /players/{account_id} | GET /players/{account_id}
*PlayersApi* | [**players_account_id_heroes_get**](docs/apis/tags/PlayersApi.md#players_account_id_heroes_get) | **get** /players/{account_id}/heroes | GET /players/{account_id}/heroes
*PlayersApi* | [**players_account_id_histograms_field_get**](docs/apis/tags/PlayersApi.md#players_account_id_histograms_field_get) | **get** /players/{account_id}/histograms/{field} | GET /players/{account_id}/histograms
*PlayersApi* | [**players_account_id_matches_get**](docs/apis/tags/PlayersApi.md#players_account_id_matches_get) | **get** /players/{account_id}/matches | GET /players/{account_id}/matches
*PlayersApi* | [**players_account_id_peers_get**](docs/apis/tags/PlayersApi.md#players_account_id_peers_get) | **get** /players/{account_id}/peers | GET /players/{account_id}/peers
*PlayersApi* | [**players_account_id_pros_get**](docs/apis/tags/PlayersApi.md#players_account_id_pros_get) | **get** /players/{account_id}/pros | GET /players/{account_id}/pros
*PlayersApi* | [**players_account_id_rankings_get**](docs/apis/tags/PlayersApi.md#players_account_id_rankings_get) | **get** /players/{account_id}/rankings | GET /players/{account_id}/rankings
*PlayersApi* | [**players_account_id_ratings_get**](docs/apis/tags/PlayersApi.md#players_account_id_ratings_get) | **get** /players/{account_id}/ratings | GET /players/{account_id}/ratings
*PlayersApi* | [**players_account_id_recent_matches_get**](docs/apis/tags/PlayersApi.md#players_account_id_recent_matches_get) | **get** /players/{account_id}/recentMatches | GET /players/{account_id}/recentMatches
*PlayersApi* | [**players_account_id_refresh_post**](docs/apis/tags/PlayersApi.md#players_account_id_refresh_post) | **post** /players/{account_id}/refresh | POST /players/{account_id}/refresh
*PlayersApi* | [**players_account_id_totals_get**](docs/apis/tags/PlayersApi.md#players_account_id_totals_get) | **get** /players/{account_id}/totals | GET /players/{account_id}/totals
*PlayersApi* | [**players_account_id_wardmap_get**](docs/apis/tags/PlayersApi.md#players_account_id_wardmap_get) | **get** /players/{account_id}/wardmap | GET /players/{account_id}/wardmap
*PlayersApi* | [**players_account_id_wl_get**](docs/apis/tags/PlayersApi.md#players_account_id_wl_get) | **get** /players/{account_id}/wl | GET /players/{account_id}/wl
*PlayersApi* | [**players_account_id_wordcloud_get**](docs/apis/tags/PlayersApi.md#players_account_id_wordcloud_get) | **get** /players/{account_id}/wordcloud | GET /players/{account_id}/wordcloud
*PlayersByRankApi* | [**players_by_rank_get**](docs/apis/tags/PlayersByRankApi.md#players_by_rank_get) | **get** /playersByRank | GET /playersByRank
*ProMatchesApi* | [**pro_matches_get**](docs/apis/tags/ProMatchesApi.md#pro_matches_get) | **get** /proMatches | GET /proMatches
*ProPlayersApi* | [**pro_players_get**](docs/apis/tags/ProPlayersApi.md#pro_players_get) | **get** /proPlayers | GET /proPlayers
*PublicMatchesApi* | [**public_matches_get**](docs/apis/tags/PublicMatchesApi.md#public_matches_get) | **get** /publicMatches | GET /publicMatches
*RankingsApi* | [**rankings_get**](docs/apis/tags/RankingsApi.md#rankings_get) | **get** /rankings | GET /rankings
*RecordsApi* | [**records_field_get**](docs/apis/tags/RecordsApi.md#records_field_get) | **get** /records/{field} | GET /records/{field}
*ReplaysApi* | [**replays_get**](docs/apis/tags/ReplaysApi.md#replays_get) | **get** /replays | GET /replays
*RequestApi* | [**request_job_id_get**](docs/apis/tags/RequestApi.md#request_job_id_get) | **get** /request/{jobId} | GET /request/{jobId}
*RequestApi* | [**request_match_id_post**](docs/apis/tags/RequestApi.md#request_match_id_post) | **post** /request/{match_id} | POST /request/{match_id}
*ScenariosApi* | [**scenarios_item_timings_get**](docs/apis/tags/ScenariosApi.md#scenarios_item_timings_get) | **get** /scenarios/itemTimings | GET /scenarios/itemTimings
*ScenariosApi* | [**scenarios_lane_roles_get**](docs/apis/tags/ScenariosApi.md#scenarios_lane_roles_get) | **get** /scenarios/laneRoles | GET /scenarios/laneRoles
*ScenariosApi* | [**scenarios_misc_get**](docs/apis/tags/ScenariosApi.md#scenarios_misc_get) | **get** /scenarios/misc | GET /scenarios/misc
*SchemaApi* | [**schema_get**](docs/apis/tags/SchemaApi.md#schema_get) | **get** /schema | GET /schema
*SearchApi* | [**search_get**](docs/apis/tags/SearchApi.md#search_get) | **get** /search | GET /search
*StatusApi* | [**status_get**](docs/apis/tags/StatusApi.md#status_get) | **get** /status | GET /status
*TeamsApi* | [**teams_get**](docs/apis/tags/TeamsApi.md#teams_get) | **get** /teams | GET /teams
*TeamsApi* | [**teams_team_id_get**](docs/apis/tags/TeamsApi.md#teams_team_id_get) | **get** /teams/{team_id} | GET /teams/{team_id}
*TeamsApi* | [**teams_team_id_heroes_get**](docs/apis/tags/TeamsApi.md#teams_team_id_heroes_get) | **get** /teams/{team_id}/heroes | GET /teams/{team_id}/heroes
*TeamsApi* | [**teams_team_id_matches_get**](docs/apis/tags/TeamsApi.md#teams_team_id_matches_get) | **get** /teams/{team_id}/matches | GET /teams/{team_id}/matches
*TeamsApi* | [**teams_team_id_players_get**](docs/apis/tags/TeamsApi.md#teams_team_id_players_get) | **get** /teams/{team_id}/players | GET /teams/{team_id}/players

## Documentation For Models


## Documentation For Authorization

 Authentication schemes defined for the API:
## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Author





























## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in python_opendota.apis and python_opendota.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from python_opendota.apis.default_api import DefaultApi`
- `from python_opendota.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import python_opendota
from python_opendota.apis import *
from python_opendota.models import *
```
