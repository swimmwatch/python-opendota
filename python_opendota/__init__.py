# flake8: noqa

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.  You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.  **Beginning 2018-04-22, the OpenDota API is limited to 50,000 free calls per month and 60 requests/minute** We offer a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more.   # noqa: E501

    The version of the OpenAPI document: 18.0.0
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.3"

# import ApiClient
from python_opendota.api_client import ApiClient

# import Configuration
from python_opendota.configuration import Configuration

# import exceptions
from python_opendota.exceptions import OpenApiException
from python_opendota.exceptions import ApiAttributeError
from python_opendota.exceptions import ApiTypeError
from python_opendota.exceptions import ApiValueError
from python_opendota.exceptions import ApiKeyError
from python_opendota.exceptions import ApiException
