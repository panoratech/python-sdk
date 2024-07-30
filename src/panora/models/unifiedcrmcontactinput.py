"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .email import Email, EmailTypedDict
from .phone import Phone, PhoneTypedDict
from panora.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedCrmContactInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedCrmContactInputFieldMappings(BaseModel):
    pass
    

class UnifiedCrmContactInputTypedDict(TypedDict):
    first_name: str
    r"""The first name of the contact"""
    last_name: str
    r"""The last name of the contact"""
    field_mappings: UnifiedCrmContactInputFieldMappingsTypedDict
    email_addresses: NotRequired[List[EmailTypedDict]]
    r"""The email addresses of the contact"""
    phone_numbers: NotRequired[List[PhoneTypedDict]]
    r"""The phone numbers of the contact"""
    addresses: NotRequired[List[AddressTypedDict]]
    r"""The addresses of the contact"""
    user_id: NotRequired[str]
    r"""The UUID of the user who owns the contact"""
    

class UnifiedCrmContactInput(BaseModel):
    first_name: str
    r"""The first name of the contact"""
    last_name: str
    r"""The last name of the contact"""
    field_mappings: UnifiedCrmContactInputFieldMappings
    email_addresses: Optional[List[Email]] = None
    r"""The email addresses of the contact"""
    phone_numbers: Optional[List[Phone]] = None
    r"""The phone numbers of the contact"""
    addresses: Optional[List[Address]] = None
    r"""The addresses of the contact"""
    user_id: Optional[str] = None
    r"""The UUID of the user who owns the contact"""
    
