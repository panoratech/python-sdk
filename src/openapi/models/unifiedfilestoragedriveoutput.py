"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedFilestorageDriveOutputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageDriveOutputFieldMappings(BaseModel):
    pass
    

class UnifiedFilestorageDriveOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageDriveOutputRemoteData(BaseModel):
    pass
    

class UnifiedFilestorageDriveOutputCreatedAtTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageDriveOutputCreatedAt(BaseModel):
    pass
    

class UnifiedFilestorageDriveOutputModifiedAtTypedDict(TypedDict):
    pass
    

class UnifiedFilestorageDriveOutputModifiedAt(BaseModel):
    pass
    

class UnifiedFilestorageDriveOutputTypedDict(TypedDict):
    name: str
    r"""The name of the drive"""
    remote_created_at: str
    r"""When the third party s drive was created."""
    drive_url: str
    r"""The url of the drive"""
    field_mappings: UnifiedFilestorageDriveOutputFieldMappingsTypedDict
    remote_data: UnifiedFilestorageDriveOutputRemoteDataTypedDict
    created_at: UnifiedFilestorageDriveOutputCreatedAtTypedDict
    modified_at: UnifiedFilestorageDriveOutputModifiedAtTypedDict
    id: NotRequired[str]
    r"""The UUID of the drive"""
    remote_id: NotRequired[str]
    r"""The id of the drive in the context of the 3rd Party"""
    

class UnifiedFilestorageDriveOutput(BaseModel):
    name: str
    r"""The name of the drive"""
    remote_created_at: str
    r"""When the third party s drive was created."""
    drive_url: str
    r"""The url of the drive"""
    field_mappings: UnifiedFilestorageDriveOutputFieldMappings
    remote_data: UnifiedFilestorageDriveOutputRemoteData
    created_at: UnifiedFilestorageDriveOutputCreatedAt
    modified_at: UnifiedFilestorageDriveOutputModifiedAt
    id: Optional[str] = None
    r"""The UUID of the drive"""
    remote_id: Optional[str] = None
    r"""The id of the drive in the context of the 3rd Party"""
    
