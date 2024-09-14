"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedticketingcommentoutput import (
    UnifiedTicketingCommentOutput,
    UnifiedTicketingCommentOutputTypedDict,
)
from panora_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from panora_sdk.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RetrieveTicketingCommentRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    id: str
    r"""id of the `comment` you want to retrive."""
    remote_data: NotRequired[bool]
    r"""Set to true to include data from the original Ticketing software."""


class RetrieveTicketingCommentRequest(BaseModel):
    x_connection_token: Annotated[
        str,
        pydantic.Field(alias="x-connection-token"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""The connection token"""

    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""id of the `comment` you want to retrive."""

    remote_data: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Set to true to include data from the original Ticketing software."""


class RetrieveTicketingCommentResponseBodyTypedDict(TypedDict):
    prev_cursor: Nullable[str]
    next_cursor: Nullable[str]
    data: List[UnifiedTicketingCommentOutputTypedDict]


class RetrieveTicketingCommentResponseBody(BaseModel):
    prev_cursor: Nullable[str]

    next_cursor: Nullable[str]

    data: List[UnifiedTicketingCommentOutput]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["prev_cursor", "next_cursor"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
