"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedfilestoragefolderinput import UnifiedFilestorageFolderInput, UnifiedFilestorageFolderInputTypedDict
from panora_sdk.types import BaseModel
from panora_sdk.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class CreateFilestorageFolderRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    remote_data: bool
    unified_filestorage_folder_input: UnifiedFilestorageFolderInputTypedDict
    

class CreateFilestorageFolderRequest(BaseModel):
    x_connection_token: Annotated[str, pydantic.Field(alias="x-connection-token"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    r"""The connection token"""
    remote_data: Annotated[bool, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))]
    unified_filestorage_folder_input: Annotated[UnifiedFilestorageFolderInput, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    