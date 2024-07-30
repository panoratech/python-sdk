"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedCrmEngagementOutputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedCrmEngagementOutputFieldMappings(BaseModel):
    pass
    

class UnifiedCrmEngagementOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedCrmEngagementOutputRemoteData(BaseModel):
    pass
    

class UnifiedCrmEngagementOutputCreatedAtTypedDict(TypedDict):
    pass
    

class UnifiedCrmEngagementOutputCreatedAt(BaseModel):
    pass
    

class UnifiedCrmEngagementOutputModifiedAtTypedDict(TypedDict):
    pass
    

class UnifiedCrmEngagementOutputModifiedAt(BaseModel):
    pass
    

class UnifiedCrmEngagementOutputTypedDict(TypedDict):
    type: str
    r"""The type of the engagement. Authorized values are EMAIL, CALL or MEETING"""
    field_mappings: UnifiedCrmEngagementOutputFieldMappingsTypedDict
    remote_data: UnifiedCrmEngagementOutputRemoteDataTypedDict
    created_at: UnifiedCrmEngagementOutputCreatedAtTypedDict
    modified_at: UnifiedCrmEngagementOutputModifiedAtTypedDict
    content: NotRequired[str]
    r"""The content of the engagement"""
    direction: NotRequired[str]
    r"""The direction of the engagement. Authorized values are INBOUND or OUTBOUND"""
    subject: NotRequired[str]
    r"""The subject of the engagement"""
    start_at: NotRequired[datetime]
    r"""The start time of the engagement"""
    end_time: NotRequired[datetime]
    r"""The end time of the engagement"""
    user_id: NotRequired[str]
    r"""The UUID of the user tied to the engagement"""
    company_id: NotRequired[str]
    r"""The UUID of the company tied to the engagement"""
    contacts: NotRequired[List[str]]
    r"""The UUIDs of contacts tied to the engagement object"""
    id: NotRequired[str]
    r"""The UUID of the engagement"""
    remote_id: NotRequired[str]
    r"""The id of the engagement in the context of the Crm 3rd Party"""
    

class UnifiedCrmEngagementOutput(BaseModel):
    type: str
    r"""The type of the engagement. Authorized values are EMAIL, CALL or MEETING"""
    field_mappings: UnifiedCrmEngagementOutputFieldMappings
    remote_data: UnifiedCrmEngagementOutputRemoteData
    created_at: UnifiedCrmEngagementOutputCreatedAt
    modified_at: UnifiedCrmEngagementOutputModifiedAt
    content: Optional[str] = None
    r"""The content of the engagement"""
    direction: Optional[str] = None
    r"""The direction of the engagement. Authorized values are INBOUND or OUTBOUND"""
    subject: Optional[str] = None
    r"""The subject of the engagement"""
    start_at: Optional[datetime] = None
    r"""The start time of the engagement"""
    end_time: Optional[datetime] = None
    r"""The end time of the engagement"""
    user_id: Optional[str] = None
    r"""The UUID of the user tied to the engagement"""
    company_id: Optional[str] = None
    r"""The UUID of the company tied to the engagement"""
    contacts: Optional[List[str]] = None
    r"""The UUIDs of contacts tied to the engagement object"""
    id: Optional[str] = None
    r"""The UUID of the engagement"""
    remote_id: Optional[str] = None
    r"""The id of the engagement in the context of the Crm 3rd Party"""
    
