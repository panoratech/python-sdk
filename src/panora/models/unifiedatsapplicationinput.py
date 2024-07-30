"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsApplicationInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedAtsApplicationInputFieldMappings(BaseModel):
    pass
    

class UnifiedAtsApplicationInputTypedDict(TypedDict):
    field_mappings: UnifiedAtsApplicationInputFieldMappingsTypedDict
    applied_at: NotRequired[datetime]
    r"""The application date"""
    rejected_at: NotRequired[datetime]
    r"""The rejection date"""
    offers: NotRequired[List[str]]
    r"""The offers UUIDs for the application"""
    source: NotRequired[str]
    r"""The source of the application"""
    credited_to: NotRequired[str]
    r"""The UUID of the person credited for the application"""
    current_stage: NotRequired[str]
    r"""The UUID of the current stage of the application"""
    reject_reason: NotRequired[str]
    r"""The rejection reason for the application"""
    candidate_id: NotRequired[str]
    r"""The UUID of the candidate"""
    job_id: NotRequired[str]
    r"""The UUID of the job"""
    

class UnifiedAtsApplicationInput(BaseModel):
    field_mappings: UnifiedAtsApplicationInputFieldMappings
    applied_at: Optional[datetime] = None
    r"""The application date"""
    rejected_at: Optional[datetime] = None
    r"""The rejection date"""
    offers: Optional[List[str]] = None
    r"""The offers UUIDs for the application"""
    source: Optional[str] = None
    r"""The source of the application"""
    credited_to: Optional[str] = None
    r"""The UUID of the person credited for the application"""
    current_stage: Optional[str] = None
    r"""The UUID of the current stage of the application"""
    reject_reason: Optional[str] = None
    r"""The rejection reason for the application"""
    candidate_id: Optional[str] = None
    r"""The UUID of the candidate"""
    job_id: Optional[str] = None
    r"""The UUID of the job"""
    
