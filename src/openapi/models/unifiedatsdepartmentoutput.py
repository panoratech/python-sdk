"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsDepartmentOutputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedAtsDepartmentOutputFieldMappings(BaseModel):
    pass
    

class UnifiedAtsDepartmentOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedAtsDepartmentOutputRemoteData(BaseModel):
    pass
    

class UnifiedAtsDepartmentOutputCreatedAtTypedDict(TypedDict):
    pass
    

class UnifiedAtsDepartmentOutputCreatedAt(BaseModel):
    pass
    

class UnifiedAtsDepartmentOutputModifiedAtTypedDict(TypedDict):
    pass
    

class UnifiedAtsDepartmentOutputModifiedAt(BaseModel):
    pass
    

class UnifiedAtsDepartmentOutputTypedDict(TypedDict):
    field_mappings: UnifiedAtsDepartmentOutputFieldMappingsTypedDict
    remote_data: UnifiedAtsDepartmentOutputRemoteDataTypedDict
    created_at: UnifiedAtsDepartmentOutputCreatedAtTypedDict
    modified_at: UnifiedAtsDepartmentOutputModifiedAtTypedDict
    name: NotRequired[str]
    r"""The name of the department"""
    id: NotRequired[str]
    r"""The UUID of the department"""
    remote_id: NotRequired[str]
    r"""The remote ID of the department in the context of the 3rd Party"""
    

class UnifiedAtsDepartmentOutput(BaseModel):
    field_mappings: UnifiedAtsDepartmentOutputFieldMappings
    remote_data: UnifiedAtsDepartmentOutputRemoteData
    created_at: UnifiedAtsDepartmentOutputCreatedAt
    modified_at: UnifiedAtsDepartmentOutputModifiedAt
    name: Optional[str] = None
    r"""The name of the department"""
    id: Optional[str] = None
    r"""The UUID of the department"""
    remote_id: Optional[str] = None
    r"""The remote ID of the department in the context of the 3rd Party"""
    
