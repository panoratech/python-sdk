"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsUserOutputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedAtsUserOutputFieldMappings(BaseModel):
    pass
    

class UnifiedAtsUserOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedAtsUserOutputRemoteData(BaseModel):
    pass
    

class UnifiedAtsUserOutputCreatedAtTypedDict(TypedDict):
    pass
    

class UnifiedAtsUserOutputCreatedAt(BaseModel):
    pass
    

class UnifiedAtsUserOutputModifiedAtTypedDict(TypedDict):
    pass
    

class UnifiedAtsUserOutputModifiedAt(BaseModel):
    pass
    

class UnifiedAtsUserOutputTypedDict(TypedDict):
    field_mappings: UnifiedAtsUserOutputFieldMappingsTypedDict
    remote_data: UnifiedAtsUserOutputRemoteDataTypedDict
    created_at: UnifiedAtsUserOutputCreatedAtTypedDict
    modified_at: UnifiedAtsUserOutputModifiedAtTypedDict
    first_name: NotRequired[str]
    r"""The first name of the user"""
    last_name: NotRequired[str]
    r"""The last name of the user"""
    email: NotRequired[str]
    r"""The email of the user"""
    disabled: NotRequired[bool]
    r"""Whether the user is disabled"""
    access_role: NotRequired[str]
    r"""The access role of the user"""
    remote_created_at: NotRequired[datetime]
    r"""The remote creation date of the user"""
    remote_modified_at: NotRequired[datetime]
    r"""The remote modification date of the user"""
    id: NotRequired[str]
    r"""The UUID of the user"""
    remote_id: NotRequired[str]
    r"""The remote ID of the user in the context of the 3rd Party"""
    

class UnifiedAtsUserOutput(BaseModel):
    field_mappings: UnifiedAtsUserOutputFieldMappings
    remote_data: UnifiedAtsUserOutputRemoteData
    created_at: UnifiedAtsUserOutputCreatedAt
    modified_at: UnifiedAtsUserOutputModifiedAt
    first_name: Optional[str] = None
    r"""The first name of the user"""
    last_name: Optional[str] = None
    r"""The last name of the user"""
    email: Optional[str] = None
    r"""The email of the user"""
    disabled: Optional[bool] = None
    r"""Whether the user is disabled"""
    access_role: Optional[str] = None
    r"""The access role of the user"""
    remote_created_at: Optional[datetime] = None
    r"""The remote creation date of the user"""
    remote_modified_at: Optional[datetime] = None
    r"""The remote modification date of the user"""
    id: Optional[str] = None
    r"""The UUID of the user"""
    remote_id: Optional[str] = None
    r"""The remote ID of the user in the context of the 3rd Party"""
    
