"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class EmailTypedDict(TypedDict):
    email_address: str
    r"""The email address"""
    email_address_type: str
    r"""The email address type. Authorized values are either PERSONAL or WORK."""
    owner_type: NotRequired[str]
    r"""The owner type of an email"""
    

class Email(BaseModel):
    email_address: str
    r"""The email address"""
    email_address_type: str
    r"""The email address type. Authorized values are either PERSONAL or WORK."""
    owner_type: Optional[str] = None
    r"""The owner type of an email"""
    