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
                    account_id = schemas.IntSchema
                    match_id = schemas.IntSchema
                    solo_competitive_rank = schemas.IntSchema
                    competitive_rank = schemas.IntSchema
                    time = schemas.IntSchema
                    __annotations__ = {
                        "account_id": account_id,
                        "match_id": match_id,
                        "solo_competitive_rank": solo_competitive_rank,
                        "competitive_rank": competitive_rank,
                        "time": time,
                    }
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["account_id"]
            ) -> MetaOapg.properties.account_id: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["match_id"]
            ) -> MetaOapg.properties.match_id: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["solo_competitive_rank"]
            ) -> MetaOapg.properties.solo_competitive_rank: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["competitive_rank"]
            ) -> MetaOapg.properties.competitive_rank: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["time"]
            ) -> MetaOapg.properties.time: ...
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            def __getitem__(
                self,
                name: typing.Union[
                    typing_extensions.Literal[
                        "account_id",
                        "match_id",
                        "solo_competitive_rank",
                        "competitive_rank",
                        "time",
                    ],
                    str,
                ],
            ):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["account_id"]
            ) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["match_id"]
            ) -> typing.Union[MetaOapg.properties.match_id, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["solo_competitive_rank"]
            ) -> typing.Union[
                MetaOapg.properties.solo_competitive_rank, schemas.Unset
            ]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["competitive_rank"]
            ) -> typing.Union[MetaOapg.properties.competitive_rank, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["time"]
            ) -> typing.Union[MetaOapg.properties.time, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: str
            ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            def get_item_oapg(
                self,
                name: typing.Union[
                    typing_extensions.Literal[
                        "account_id",
                        "match_id",
                        "solo_competitive_rank",
                        "competitive_rank",
                        "time",
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
                account_id: typing.Union[
                    MetaOapg.properties.account_id, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                match_id: typing.Union[
                    MetaOapg.properties.match_id, decimal.Decimal, int, schemas.Unset
                ] = schemas.unset,
                solo_competitive_rank: typing.Union[
                    MetaOapg.properties.solo_competitive_rank,
                    decimal.Decimal,
                    int,
                    schemas.Unset,
                ] = schemas.unset,
                competitive_rank: typing.Union[
                    MetaOapg.properties.competitive_rank,
                    decimal.Decimal,
                    int,
                    schemas.Unset,
                ] = schemas.unset,
                time: typing.Union[
                    MetaOapg.properties.time, decimal.Decimal, int, schemas.Unset
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
                    account_id=account_id,
                    match_id=match_id,
                    solo_competitive_rank=solo_competitive_rank,
                    competitive_rank=competitive_rank,
                    time=time,
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
    def _players_account_id_ratings_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def _players_account_id_ratings_get_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _players_account_id_ratings_get_oapg(
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
    def _players_account_id_ratings_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        GET /players/{account_id}/ratings
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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

class PlayersAccountIdRatingsGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def players_account_id_ratings_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]: ...
    @typing.overload
    def players_account_id_ratings_get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def players_account_id_ratings_get(
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
    def players_account_id_ratings_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._players_account_id_ratings_get_oapg(
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
        return self._players_account_id_ratings_get_oapg(
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
