"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsActivityInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedAtsActivityInputFieldMappings(BaseModel):
    pass
    

class UnifiedAtsActivityInputTypedDict(TypedDict):
    field_mappings: UnifiedAtsActivityInputFieldMappingsTypedDict
    activity_type: NotRequired[str]
    r"""The type of activity"""
    subject: NotRequired[str]
    r"""The subject of the activity"""
    body: NotRequired[str]
    r"""The body of the activity"""
    visibility: NotRequired[str]
    r"""The visibility of the activity"""
    candidate_id: NotRequired[str]
    r"""The UUID of the candidate"""
    remote_created_at: NotRequired[datetime]
    r"""The remote creation date of the activity"""
    

class UnifiedAtsActivityInput(BaseModel):
    field_mappings: UnifiedAtsActivityInputFieldMappings
    activity_type: Optional[str] = None
    r"""The type of activity"""
    subject: Optional[str] = None
    r"""The subject of the activity"""
    body: Optional[str] = None
    r"""The body of the activity"""
    visibility: Optional[str] = None
    r"""The visibility of the activity"""
    candidate_id: Optional[str] = None
    r"""The UUID of the candidate"""
    remote_created_at: Optional[datetime] = None
    r"""The remote creation date of the activity"""
    
