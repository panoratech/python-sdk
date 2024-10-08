"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsTagOutputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedAtsTagOutputFieldMappings(BaseModel):
    pass
    

class UnifiedAtsTagOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedAtsTagOutputRemoteData(BaseModel):
    pass
    

class UnifiedAtsTagOutputTypedDict(TypedDict):
    field_mappings: UnifiedAtsTagOutputFieldMappingsTypedDict
    remote_data: UnifiedAtsTagOutputRemoteDataTypedDict
    name: NotRequired[str]
    r"""The name of the tag"""
    id_ats_candidate: NotRequired[str]
    r"""The UUID of the candidate"""
    id: NotRequired[str]
    r"""The UUID of the tag"""
    remote_id: NotRequired[str]
    r"""The remote ID of the tag in the context of the 3rd Party"""
    created_at: NotRequired[datetime]
    r"""The creation date of the tag"""
    modified_at: NotRequired[datetime]
    r"""The modification date of the tag"""
    

class UnifiedAtsTagOutput(BaseModel):
    field_mappings: UnifiedAtsTagOutputFieldMappings
    remote_data: UnifiedAtsTagOutputRemoteData
    name: Optional[str] = None
    r"""The name of the tag"""
    id_ats_candidate: Optional[str] = None
    r"""The UUID of the candidate"""
    id: Optional[str] = None
    r"""The UUID of the tag"""
    remote_id: Optional[str] = None
    r"""The remote ID of the tag in the context of the 3rd Party"""
    created_at: Optional[datetime] = None
    r"""The creation date of the tag"""
    modified_at: Optional[datetime] = None
    r"""The modification date of the tag"""
    
