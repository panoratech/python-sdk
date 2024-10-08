"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedfilestoragefileinput import UnifiedFilestorageFileInput, UnifiedFilestorageFileInputTypedDict
from panora.types import BaseModel
from panora.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class CreateFilestorageFileRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    remote_data: bool
    unified_filestorage_file_input: UnifiedFilestorageFileInputTypedDict
    

class CreateFilestorageFileRequest(BaseModel):
    x_connection_token: Annotated[str, pydantic.Field(alias="x-connection-token"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    r"""The connection token"""
    remote_data: Annotated[bool, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    unified_filestorage_file_input: Annotated[UnifiedFilestorageFileInput, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
