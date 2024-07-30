"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedfilestoragefolderoutput import UnifiedFilestorageFolderOutput, UnifiedFilestorageFolderOutputTypedDict
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListFilestorageFolderRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    remote_data: NotRequired[bool]
    r"""Set to true to include data from the original software."""
    limit: NotRequired[float]
    r"""Set to get the number of records."""
    cursor: NotRequired[str]
    r"""Set to get the number of records after this cursor."""
    

class ListFilestorageFolderRequest(BaseModel):
    x_connection_token: Annotated[str, pydantic.Field(alias="x-connection-token"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    r"""The connection token"""
    remote_data: Annotated[Optional[bool], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Set to true to include data from the original software."""
    limit: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 50
    r"""Set to get the number of records."""
    cursor: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Set to get the number of records after this cursor."""
    

class ListFilestorageFolderResponseBodyTypedDict(TypedDict):
    prev_cursor: str
    next_cursor: str
    data: List[UnifiedFilestorageFolderOutputTypedDict]
    

class ListFilestorageFolderResponseBody(BaseModel):
    prev_cursor: str
    next_cursor: str
    data: List[UnifiedFilestorageFolderOutput]
    
