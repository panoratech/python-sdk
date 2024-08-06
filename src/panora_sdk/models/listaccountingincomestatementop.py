"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedaccountingincomestatementoutput import UnifiedAccountingIncomestatementOutput, UnifiedAccountingIncomestatementOutputTypedDict
from panora_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from panora_sdk.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Callable, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListAccountingIncomeStatementRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    remote_data: NotRequired[bool]
    r"""Set to true to include data from the original software."""
    limit: NotRequired[float]
    r"""Set to get the number of records."""
    cursor: NotRequired[str]
    r"""Set to get the number of records after this cursor."""
    

class ListAccountingIncomeStatementRequest(BaseModel):
    x_connection_token: Annotated[str, pydantic.Field(alias="x-connection-token"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    r"""The connection token"""
    remote_data: Annotated[Optional[bool], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Set to true to include data from the original software."""
    limit: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Set to get the number of records."""
    cursor: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Set to get the number of records after this cursor."""
    

class ListAccountingIncomeStatementResponseBodyTypedDict(TypedDict):
    prev_cursor: Nullable[str]
    next_cursor: Nullable[str]
    data: List[UnifiedAccountingIncomestatementOutputTypedDict]
    

class ListAccountingIncomeStatementResponseBody(BaseModel):
    prev_cursor: Nullable[str]
    next_cursor: Nullable[str]
    data: List[UnifiedAccountingIncomestatementOutput]
    
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

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        

class ListAccountingIncomeStatementResponseTypedDict(TypedDict):
    result: ListAccountingIncomeStatementResponseBodyTypedDict
    

class ListAccountingIncomeStatementResponse(BaseModel):
    next: Callable[[], Optional[ListAccountingIncomeStatementResponse]]
    
    result: ListAccountingIncomeStatementResponseBody
    
