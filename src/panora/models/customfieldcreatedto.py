"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora.types import BaseModel
from typing import TypedDict


class CustomFieldCreateDtoTypedDict(TypedDict):
    object_type_owner: str
    name: str
    description: str
    data_type: str
    source_custom_field_id: str
    source_provider: str
    linked_user_id: str
    

class CustomFieldCreateDto(BaseModel):
    object_type_owner: str
    name: str
    description: str
    data_type: str
    source_custom_field_id: str
    source_provider: str
    linked_user_id: str
    
