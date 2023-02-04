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

# Path params
TeamIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    "RequestRequiredPathParams",
    {
        "team_id": typing.Union[
            TeamIdSchema,
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

request_path_team_id = api_client.PathParameter(
    name="team_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TeamIdSchema,
    required=True,
)

class SchemaFor200ResponseBodyApplicationJson(schemas.DictSchema):
    class MetaOapg:
        class properties:
            match_id = schemas.IntSchema
            radiant = schemas.BoolSchema
            radiant_win = schemas.BoolSchema
            radiant_score = schemas.IntSchema
            dire_score = schemas.IntSchema
            duration = schemas.IntSchema
            start_time = schemas.IntSchema
            leagueid = schemas.IntSchema
            league_name = schemas.StrSchema
            cluster = schemas.IntSchema
            opposing_team_id = schemas.IntSchema
            opposing_team_name = schemas.StrSchema
            opposing_team_logo = schemas.StrSchema
            __annotations__ = {
                "match_id": match_id,
                "radiant": radiant,
                "radiant_win": radiant_win,
                "radiant_score": radiant_score,
                "dire_score": dire_score,
                "duration": duration,
                "start_time": start_time,
                "leagueid": leagueid,
                "league_name": league_name,
                "cluster": cluster,
                "opposing_team_id": opposing_team_id,
                "opposing_team_name": opposing_team_name,
                "opposing_team_logo": opposing_team_logo,
            }
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["match_id"]
    ) -> MetaOapg.properties.match_id: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["radiant"]
    ) -> MetaOapg.properties.radiant: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["radiant_win"]
    ) -> MetaOapg.properties.radiant_win: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["radiant_score"]
    ) -> MetaOapg.properties.radiant_score: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["dire_score"]
    ) -> MetaOapg.properties.dire_score: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["duration"]
    ) -> MetaOapg.properties.duration: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["start_time"]
    ) -> MetaOapg.properties.start_time: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["leagueid"]
    ) -> MetaOapg.properties.leagueid: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["league_name"]
    ) -> MetaOapg.properties.league_name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["cluster"]
    ) -> MetaOapg.properties.cluster: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["opposing_team_id"]
    ) -> MetaOapg.properties.opposing_team_id: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["opposing_team_name"]
    ) -> MetaOapg.properties.opposing_team_name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["opposing_team_logo"]
    ) -> MetaOapg.properties.opposing_team_logo: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "match_id",
                "radiant",
                "radiant_win",
                "radiant_score",
                "dire_score",
                "duration",
                "start_time",
                "leagueid",
                "league_name",
                "cluster",
                "opposing_team_id",
                "opposing_team_name",
                "opposing_team_logo",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["match_id"]
    ) -> typing.Union[MetaOapg.properties.match_id, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["radiant"]
    ) -> typing.Union[MetaOapg.properties.radiant, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["radiant_win"]
    ) -> typing.Union[MetaOapg.properties.radiant_win, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["radiant_score"]
    ) -> typing.Union[MetaOapg.properties.radiant_score, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["dire_score"]
    ) -> typing.Union[MetaOapg.properties.dire_score, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["duration"]
    ) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["start_time"]
    ) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["leagueid"]
    ) -> typing.Union[MetaOapg.properties.leagueid, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["league_name"]
    ) -> typing.Union[MetaOapg.properties.league_name, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["cluster"]
    ) -> typing.Union[MetaOapg.properties.cluster, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["opposing_team_id"]
    ) -> typing.Union[MetaOapg.properties.opposing_team_id, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["opposing_team_name"]
    ) -> typing.Union[MetaOapg.properties.opposing_team_name, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["opposing_team_logo"]
    ) -> typing.Union[MetaOapg.properties.opposing_team_logo, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "match_id",
                "radiant",
                "radiant_win",
                "radiant_score",
                "dire_score",
                "duration",
                "start_time",
                "leagueid",
                "league_name",
                "cluster",
                "opposing_team_id",
                "opposing_team_name",
                "opposing_team_logo",
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
        match_id: typing.Union[
            MetaOapg.properties.match_id, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        radiant: typing.Union[
            MetaOapg.properties.radiant, bool, schemas.Unset
        ] = schemas.unset,
        radiant_win: typing.Union[
            MetaOapg.properties.radiant_win, bool, schemas.Unset
        ] = schemas.unset,
        radiant_score: typing.Union[
            MetaOapg.properties.radiant_score, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        dire_score: typing.Union[
            MetaOapg.properties.dire_score, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        duration: typing.Union[
            MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        start_time: typing.Union[
            MetaOapg.properties.start_time, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        leagueid: typing.Union[
            MetaOapg.properties.leagueid, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        league_name: typing.Union[
            MetaOapg.properties.league_name, str, schemas.Unset
        ] = schemas.unset,
        cluster: typing.Union[
            MetaOapg.properties.cluster, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        opposing_team_id: typing.Union[
            MetaOapg.properties.opposing_team_id, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        opposing_team_name: typing.Union[
            MetaOapg.properties.opposing_team_name, str, schemas.Unset
        ] = schemas.unset,
        opposing_team_logo: typing.Union[
            MetaOapg.properties.opposing_team_logo, str, schemas.Unset
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
    ) -> "SchemaFor200ResponseBodyApplicationJson":
        return super().__new__(
            cls,
            *_args,
            match_id=match_id,
            radiant=radiant,
            radiant_win=radiant_win,
            radiant_score=radiant_score,
            dire_score=dire_score,
            duration=duration,
            start_time=start_time,
            leagueid=leagueid,
            league_name=league_name,
            cluster=cluster,
            opposing_team_id=opposing_team_id,
            opposing_team_name=opposing_team_name,
            opposing_team_logo=opposing_team_logo,
            _configuration=_configuration,
            **kwargs,
        )

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
    def _teams_team_id_matches_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def _teams_team_id_matches_get_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _teams_team_id_matches_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def _teams_team_id_matches_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        GET /teams/{team_id}/matches
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (request_path_team_id,):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace("{%s}" % k, v)

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

class TeamsTeamIdMatchesGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def teams_team_id_matches_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def teams_team_id_matches_get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def teams_team_id_matches_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...
    def teams_team_id_matches_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._teams_team_id_matches_get_oapg(
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
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def get(
        self,
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
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._teams_team_id_matches_get_oapg(
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
