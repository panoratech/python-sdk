"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsAttachmentInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedAtsAttachmentInputFieldMappings(BaseModel):
    pass
    

class UnifiedAtsAttachmentInputTypedDict(TypedDict):
    field_mappings: UnifiedAtsAttachmentInputFieldMappingsTypedDict
    file_url: NotRequired[str]
    r"""The URL of the file"""
    file_name: NotRequired[str]
    r"""The name of the file"""
    attachment_type: NotRequired[str]
    r"""The type of the file"""
    remote_created_at: NotRequired[datetime]
    r"""The remote creation date of the attachment"""
    remote_modified_at: NotRequired[datetime]
    r"""The remote modification date of the attachment"""
    candidate_id: NotRequired[str]
    r"""The UUID of the candidate"""
    

class UnifiedAtsAttachmentInput(BaseModel):
    field_mappings: UnifiedAtsAttachmentInputFieldMappings
    file_url: Optional[str] = None
    r"""The URL of the file"""
    file_name: Optional[str] = None
    r"""The name of the file"""
    attachment_type: Optional[str] = None
    r"""The type of the file"""
    remote_created_at: Optional[datetime] = None
    r"""The remote creation date of the attachment"""
    remote_modified_at: Optional[datetime] = None
    r"""The remote modification date of the attachment"""
    candidate_id: Optional[str] = None
    r"""The UUID of the candidate"""
    
