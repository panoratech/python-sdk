"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedCrmDealInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedCrmDealInputFieldMappings(BaseModel):
    pass
    

class UnifiedCrmDealInputTypedDict(TypedDict):
    name: str
    r"""The name of the deal"""
    description: str
    r"""The description of the deal"""
    amount: float
    r"""The amount of the deal"""
    field_mappings: UnifiedCrmDealInputFieldMappingsTypedDict
    user_id: NotRequired[str]
    r"""The UUID of the user who is on the deal"""
    stage_id: NotRequired[str]
    r"""The UUID of the stage of the deal"""
    company_id: NotRequired[str]
    r"""The UUID of the company tied to the deal"""
    

class UnifiedCrmDealInput(BaseModel):
    name: str
    r"""The name of the deal"""
    description: str
    r"""The description of the deal"""
    amount: float
    r"""The amount of the deal"""
    field_mappings: UnifiedCrmDealInputFieldMappings
    user_id: Optional[str] = None
    r"""The UUID of the user who is on the deal"""
    stage_id: Optional[str] = None
    r"""The UUID of the stage of the deal"""
    company_id: Optional[str] = None
    r"""The UUID of the company tied to the deal"""
    
