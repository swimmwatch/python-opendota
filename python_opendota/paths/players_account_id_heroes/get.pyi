# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from python_opendota import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from python_opendota import schemas  # noqa: F401

# Query params
LimitSchema = schemas.IntSchema
OffsetSchema = schemas.IntSchema
WinSchema = schemas.IntSchema
PatchSchema = schemas.IntSchema
GameModeSchema = schemas.IntSchema
LobbyTypeSchema = schemas.IntSchema
RegionSchema = schemas.IntSchema
DateSchema = schemas.IntSchema
LaneRoleSchema = schemas.IntSchema
HeroIdSchema = schemas.IntSchema
IsRadiantSchema = schemas.IntSchema
IncludedAccountIdSchema = schemas.IntSchema
ExcludedAccountIdSchema = schemas.IntSchema
WithHeroIdSchema = schemas.IntSchema
AgainstHeroIdSchema = schemas.IntSchema
SignificantSchema = schemas.IntSchema
HavingSchema = schemas.IntSchema
SortSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    "RequestRequiredQueryParams", {}
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    "RequestOptionalQueryParams",
    {
        "limit": typing.Union[
            LimitSchema,
            decimal.Decimal,
            int,
        ],
        "offset": typing.Union[
            OffsetSchema,
            decimal.Decimal,
            int,
        ],
        "win": typing.Union[
            WinSchema,
            decimal.Decimal,
            int,
        ],
        "patch": typing.Union[
            PatchSchema,
            decimal.Decimal,
            int,
        ],
        "game_mode": typing.Union[
            GameModeSchema,
            decimal.Decimal,
            int,
        ],
        "lobby_type": typing.Union[
            LobbyTypeSchema,
            decimal.Decimal,
            int,
        ],
        "region": typing.Union[
            RegionSchema,
            decimal.Decimal,
            int,
        ],
        "date": typing.Union[
            DateSchema,
            decimal.Decimal,
            int,
        ],
        "lane_role": typing.Union[
            LaneRoleSchema,
            decimal.Decimal,
            int,
        ],
        "hero_id": typing.Union[
            HeroIdSchema,
            decimal.Decimal,
            int,
        ],
        "is_radiant": typing.Union[
            IsRadiantSchema,
            decimal.Decimal,
            int,
        ],
        "included_account_id": typing.Union[
            IncludedAccountIdSchema,
            decimal.Decimal,
            int,
        ],
        "excluded_account_id": typing.Union[
            ExcludedAccountIdSchema,
            decimal.Decimal,
            int,
        ],
        "with_hero_id": typing.Union[
            WithHeroIdSchema,
            decimal.Decimal,
            int,
        ],
        "against_hero_id": typing.Union[
            AgainstHeroIdSchema,
            decimal.Decimal,
            int,
        ],
        "significant": typing.Union[
            SignificantSchema,
            decimal.Decimal,
            int,
        ],
        "having": typing.Union[
            HavingSchema,
            decimal.Decimal,
            int,
        ],
        "sort": typing.Union[
            SortSchema,
            str,
        ],
    },
    total=False,
)

class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass

request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_win = api_client.QueryParameter(
    name="win",
    style=api_client.ParameterStyle.FORM,
    schema=WinSchema,
    explode=True,
)
request_query_patch = api_client.QueryParameter(
    name="patch",
    style=api_client.ParameterStyle.FORM,
    schema=PatchSchema,
    explode=True,
)
request_query_game_mode = api_client.QueryParameter(
    name="game_mode",
    style=api_client.ParameterStyle.FORM,
    schema=GameModeSchema,
    explode=True,
)
request_query_lobby_type = api_client.QueryParameter(
    name="lobby_type",
    style=api_client.ParameterStyle.FORM,
    schema=LobbyTypeSchema,
    explode=True,
)
request_query_region = api_client.QueryParameter(
    name="region",
    style=api_client.ParameterStyle.FORM,
    schema=RegionSchema,
    explode=True,
)
request_query_date = api_client.QueryParameter(
    name="date",
    style=api_client.ParameterStyle.FORM,
    schema=DateSchema,
    explode=True,
)
request_query_lane_role = api_client.QueryParameter(
    name="lane_role",
    style=api_client.ParameterStyle.FORM,
    schema=LaneRoleSchema,
    explode=True,
)
request_query_hero_id = api_client.QueryParameter(
    name="hero_id",
    style=api_client.ParameterStyle.FORM,
    schema=HeroIdSchema,
    explode=True,
)
request_query_is_radiant = api_client.QueryParameter(
    name="is_radiant",
    style=api_client.ParameterStyle.FORM,
    schema=IsRadiantSchema,
    explode=True,
)
request_query_included_account_id = api_client.QueryParameter(
    name="included_account_id",
    style=api_client.ParameterStyle.FORM,
    schema=IncludedAccountIdSchema,
    explode=True,
)
request_query_excluded_account_id = api_client.QueryParameter(
    name="excluded_account_id",
    style=api_client.ParameterStyle.FORM,
    schema=ExcludedAccountIdSchema,
    explode=True,
)
request_query_with_hero_id = api_client.QueryParameter(
    name="with_hero_id",
    style=api_client.ParameterStyle.FORM,
    schema=WithHeroIdSchema,
    explode=True,
)
request_query_against_hero_id = api_client.QueryParameter(
    name="against_hero_id",
    style=api_client.ParameterStyle.FORM,
    schema=AgainstHeroIdSchema,
    explode=True,
)
request_query_significant = api_client.QueryParameter(
    name="significant",
    style=api_client.ParameterStyle.FORM,
    schema=SignificantSchema,
    explode=True,
)
request_query_having = api_client.QueryParameter(
    name="having",
    style=api_client.ParameterStyle.FORM,
    schema=HavingSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
# Path params
AccountIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    "RequestRequiredPathParams",
    {
        "account_id": typing.Union[
            AccountIdSchema,
            decimal.Decimal,
            int,
        ],
    },
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    "RequestOptionalPathParams", {}, total=False
)

class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass

request_path_account_id = api_client.PathParameter(
    name="account_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccountIdSchema,
    required=True,
)

class SchemaFor200ResponseBodyApplicationJson(schemas.ListSchema):
    class MetaOapg:
        class items(schemas.DictSchema):
            class MetaOapg:
                class properties:
                    hero_id = schemas.StrSchema
                    last_played = schemas.IntSchema
                    games = schemas.IntSchema
                    win = schemas.IntSchema
                    with_games = schemas.IntSchema
                    with_win = schemas.IntSchema
                    against_games = schemas.IntSchema
                    against_win = schemas.IntSchema
                    __annotations__ = {
                        "hero_id": hero_id,
                        "last_played": last_played,
                        "games": games,
                        "win": win,
                        "with_games": with_games,
                        "with_win": with_win,
                        "against_games": against_games,
                        "against_win": against_win,
                    }
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["hero_id"]
            ) -> MetaOapg.properties.hero_id: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["last_played"]
            ) -> MetaOapg.properties.last_played: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["games"]
            ) -> MetaOapg.properties.games: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["win"]
            ) -> MetaOapg.properties.win: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["with_games"]
            ) -> MetaOapg.properties.with_games: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["with_win"]
            ) -> MetaOapg.properties.with_win: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["against_games"]
            ) -> MetaOapg.properties.against_games: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["against_win"]
            ) -> MetaOapg.properties.against_win: ...
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            def __getitem__(
                self,
                name: typing.Union[
                    typing_extensions.Literal[
                        "hero_id",
                        "last_played",
                        "games",
                        "win",
                        "with_games",
                        "with_win",
                        "against_games",
                        "against_win",
                    ],
                    str,
                ],
            ):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["hero_id"]
            ) -> typing.Union[MetaOapg.properties.hero_id, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["last_played"]
            ) -> typing.Union[MetaOapg.properties.last_played, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["games"]
            ) -> typing.Union[MetaOapg.properties.games, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["win"]
            ) -> typing.Union[MetaOapg.properties.win, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["with_games"]
            ) -> typing.Union[MetaOapg.properties.with_games, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["with_win"]
            ) -> typing.Union[MetaOapg.properties.with_win, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["against_games"]
            ) -> typing.Union[MetaOapg.properties.against_games, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["against_win"]
            ) -> typing.Union[MetaOapg.properties.against_win, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: str
            ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            def get_item_oapg(
                self,
                name: typing.Union[
                    typing_extensions.Literal[
                        "hero_id",
                        "last_played",
                        "games",
                        "win",
                        "with_games",
                        "with_win",
                        "against_games",
                        "against_win",
                    ],
                    str,
                ],
            ):
                return super().get_item_oapg(name)
            def __new__(
                cls,
                *_args: typing.Union[
                    dict,
                    frozendict.frozendict,
                ],
                hero_id: typing.Union[
                    MetaOapg.properties.hero_id, str, schemas.Unset
                ] = schemas.unset,
                last_played: typing.Union[
                    MetaOapg.properties.last_played, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                games: typing.Union[
                    MetaOapg.properties.games, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                win: typing.Union[
                    MetaOapg.properties.win, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                with_games: typing.Union[
                    MetaOapg.properties.with_games, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                with_win: typing.Union[
                    MetaOapg.properties.with_win, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                against_games: typing.Union[
                    MetaOapg.properties.against_games,
                    decimal.Decimal,
                    int,
                    schemas.Unset,
                ] = schemas.unset,
                against_win: typing.Union[
                    MetaOapg.properties.against_win, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[
                    schemas.AnyTypeSchema,
                    dict,
                    frozendict.frozendict,
                    str,
                    date,
                    datetime,
                    uuid.UUID,
                    int,
                    float,
                    decimal.Decimal,
                    None,
                    list,
                    tuple,
                    bytes,
                ],
            ) -> "items":
                return super().__new__(
                    cls,
                    *_args,
                    hero_id=hero_id,
                    last_played=last_played,
                    games=games,
                    win=win,
                    with_games=with_games,
                    with_win=with_win,
                    against_games=against_games,
                    against_win=against_win,
                    _configuration=_configuration,
                    **kwargs,
                )
    def __new__(
        cls,
        _arg: typing.Union[
            typing.Tuple[
                typing.Union[
                    MetaOapg.items,
                    dict,
                    frozendict.frozendict,
                ]
            ],
            typing.List[
                typing.Union[
                    MetaOapg.items,
                    dict,
                    frozendict.frozendict,
                ]
            ],
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> "SchemaFor200ResponseBodyApplicationJson":
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )
    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset

_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        "application/json": api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson
        ),
    },
)
_all_accept_content_types = ("application/json",)

class BaseApi(api_client.Api):
    @typing.overload
    def _players_account_id_heroes_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def _players_account_id_heroes_get_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _players_account_id_heroes_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def _players_account_id_heroes_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        GET /players/{account_id}/heroes
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (request_path_account_id,):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace("{%s}" % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_win,
            request_query_patch,
            request_query_game_mode,
            request_query_lobby_type,
            request_query_region,
            request_query_date,
            request_query_lane_role,
            request_query_hero_id,
            request_query_is_radiant,
            request_query_included_account_id,
            request_query_excluded_account_id,
            request_query_with_hero_id,
            request_query_against_hero_id,
            request_query_significant,
            request_query_having,
            request_query_sort,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(
                parameter_data, prefix_separator_iterator
            )
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add("Accept", accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method="get".upper(),
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(
                response=response
            )
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(
                    response, self.api_client.configuration
                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response
                )

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response,
            )

        return api_response

class PlayersAccountIdHeroesGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def players_account_id_heroes_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def players_account_id_heroes_get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def players_account_id_heroes_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def players_account_id_heroes_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._players_account_id_heroes_get_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )

class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._players_account_id_heroes_get_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
