"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedFilestorageFolderOutputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageFolderOutputFieldMappings(BaseModel):
    pass
    

class UnifiedFilestorageFolderOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageFolderOutputRemoteData(BaseModel):
    pass
    

class UnifiedFilestorageFolderOutputCreatedAtTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageFolderOutputCreatedAt(BaseModel):
    pass
    

class UnifiedFilestorageFolderOutputModifiedAtTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageFolderOutputModifiedAt(BaseModel):
    pass
    

class UnifiedFilestorageFolderOutputTypedDict(TypedDict):
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
    field_mappings: UnifiedFilestorageFolderOutputFieldMappingsTypedDict
    remote_data: UnifiedFilestorageFolderOutputRemoteDataTypedDict
    created_at: UnifiedFilestorageFolderOutputCreatedAtTypedDict
    modified_at: UnifiedFilestorageFolderOutputModifiedAtTypedDict
    id: NotRequired[str]
    r"""The UUID of the folder"""
    remote_id: NotRequired[str]
    r"""The id of the folder in the context of the 3rd Party"""
    

class UnifiedFilestorageFolderOutput(BaseModel):
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
    field_mappings: UnifiedFilestorageFolderOutputFieldMappings
    remote_data: UnifiedFilestorageFolderOutputRemoteData
    created_at: UnifiedFilestorageFolderOutputCreatedAt
    modified_at: UnifiedFilestorageFolderOutputModifiedAt
    id: Optional[str] = None
    r"""The UUID of the folder"""
    remote_id: Optional[str] = None
    r"""The id of the folder in the context of the 3rd Party"""
    
