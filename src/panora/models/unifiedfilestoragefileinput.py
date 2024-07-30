"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora.types import BaseModel
from typing import TypedDict


class UnifiedFilestorageFileInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageFileInputFieldMappings(BaseModel):
    pass
    

class UnifiedFilestorageFileInputTypedDict(TypedDict):
    name: str
    r"""The name of the file"""
    file_url: str
    r"""The url of the file"""
    mime_type: str
    r"""The mime type of the file"""
    size: str
    r"""The size of the file"""
    folder_id: str
    r"""The UUID of the folder tied to the file"""
    permission: str
    r"""The UUID of the permission tied to the file"""
    shared_link: str
    r"""The UUID of the shared link tied to the file"""
    field_mappings: UnifiedFilestorageFileInputFieldMappingsTypedDict
    

class UnifiedFilestorageFileInput(BaseModel):
    name: str
    r"""The name of the file"""
    file_url: str
    r"""The url of the file"""
    mime_type: str
    r"""The mime type of the file"""
    size: str
    r"""The size of the file"""
    folder_id: str
    r"""The UUID of the folder tied to the file"""
    permission: str
    r"""The UUID of the permission tied to the file"""
    shared_link: str
    r"""The UUID of the shared link tied to the file"""
    field_mappings: UnifiedFilestorageFileInputFieldMappings
    
