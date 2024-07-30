"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class PhoneTypedDict(TypedDict):
    phone_number: str
    r"""The phone number starting with a plus (+) followed by the country code (e.g +336676778890 for France)"""
    phone_type: str
    r"""The phone type. Authorized values are either MOBILE or WORK"""
    owner_type: NotRequired[str]
    r"""The owner type of a phone number"""
    

class Phone(BaseModel):
    phone_number: str
    r"""The phone number starting with a plus (+) followed by the country code (e.g +336676778890 for France)"""
    phone_type: str
    r"""The phone type. Authorized values are either MOBILE or WORK"""
    owner_type: Optional[str] = None
    r"""The owner type of a phone number"""
    
