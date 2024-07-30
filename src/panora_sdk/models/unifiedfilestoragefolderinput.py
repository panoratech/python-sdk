"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel
from typing import TypedDict


class UnifiedFilestorageFolderInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageFolderInputFieldMappings(BaseModel):
    pass
    

class UnifiedFilestorageFolderInputTypedDict(TypedDict):
    name: str
    r"""The name of the folder"""
    size: str
    r"""The size of the folder"""
    folder_url: str
    r"""The url of the folder"""
    description: str
    r"""The description of the folder"""
    drive_id: str
    r"""The UUID of the drive tied to the folder"""
    parent_folder_id: str
    r"""The UUID of the parent folder"""
    shared_link: str
    r"""The UUID of the shared link tied to the folder"""
    permission: str
    r"""The UUID of the permission tied to the folder"""
    field_mappings: UnifiedFilestorageFolderInputFieldMappingsTypedDict
    

class UnifiedFilestorageFolderInput(BaseModel):
    name: str
    r"""The name of the folder"""
    size: str
    r"""The size of the folder"""
    folder_url: str
    r"""The url of the folder"""
    description: str
    r"""The description of the folder"""
    drive_id: str
    r"""The UUID of the drive tied to the folder"""
    parent_folder_id: str
    r"""The UUID of the parent folder"""
    shared_link: str
    r"""The UUID of the shared link tied to the folder"""
    permission: str
    r"""The UUID of the permission tied to the folder"""
    field_mappings: UnifiedFilestorageFolderInputFieldMappings
    