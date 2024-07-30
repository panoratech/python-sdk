"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .email import Email, EmailTypedDict
from .phone import Phone, PhoneTypedDict
from .url import URL, URLTypedDict
from datetime import datetime
from openapi.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsCandidateInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedAtsCandidateInputFieldMappings(BaseModel):
    pass
    

class UnifiedAtsCandidateInputTypedDict(TypedDict):
    field_mappings: UnifiedAtsCandidateInputFieldMappingsTypedDict
    first_name: NotRequired[str]
    r"""The first name of the candidate"""
    last_name: NotRequired[str]
    r"""The last name of the candidate"""
    company: NotRequired[str]
    r"""The company of the candidate"""
    title: NotRequired[str]
    r"""The title of the candidate"""
    locations: NotRequired[str]
    r"""The locations of the candidate"""
    is_private: NotRequired[bool]
    r"""Whether the candidate is private"""
    email_reachable: NotRequired[bool]
    r"""Whether the candidate is reachable by email"""
    remote_created_at: NotRequired[datetime]
    r"""The remote creation date of the candidate"""
    remote_modified_at: NotRequired[datetime]
    r"""The remote modification date of the candidate"""
    last_interaction_at: NotRequired[datetime]
    r"""The last interaction date with the candidate"""
    attachments: NotRequired[List[str]]
    r"""The attachments UUIDs of the candidate"""
    applications: NotRequired[List[str]]
    r"""The applications UUIDs of the candidate"""
    tags: NotRequired[List[str]]
    r"""The tags of the candidate"""
    urls: NotRequired[List[URLTypedDict]]
    r"""The urls of the candidate, possible values for Url type are WEBSITE, BLOG, LINKEDIN, GITHUB, or OTHER"""
    phone_numbers: NotRequired[List[PhoneTypedDict]]
    r"""The phone numbers of the candidate"""
    email_addresses: NotRequired[List[EmailTypedDict]]
    r"""The email addresses of the candidate"""
    

class UnifiedAtsCandidateInput(BaseModel):
    field_mappings: UnifiedAtsCandidateInputFieldMappings
    first_name: Optional[str] = None
    r"""The first name of the candidate"""
    last_name: Optional[str] = None
    r"""The last name of the candidate"""
    company: Optional[str] = None
    r"""The company of the candidate"""
    title: Optional[str] = None
    r"""The title of the candidate"""
    locations: Optional[str] = None
    r"""The locations of the candidate"""
    is_private: Optional[bool] = None
    r"""Whether the candidate is private"""
    email_reachable: Optional[bool] = None
    r"""Whether the candidate is reachable by email"""
    remote_created_at: Optional[datetime] = None
    r"""The remote creation date of the candidate"""
    remote_modified_at: Optional[datetime] = None
    r"""The remote modification date of the candidate"""
    last_interaction_at: Optional[datetime] = None
    r"""The last interaction date with the candidate"""
    attachments: Optional[List[str]] = None
    r"""The attachments UUIDs of the candidate"""
    applications: Optional[List[str]] = None
    r"""The applications UUIDs of the candidate"""
    tags: Optional[List[str]] = None
    r"""The tags of the candidate"""
    urls: Optional[List[URL]] = None
    r"""The urls of the candidate, possible values for Url type are WEBSITE, BLOG, LINKEDIN, GITHUB, or OTHER"""
    phone_numbers: Optional[List[Phone]] = None
    r"""The phone numbers of the candidate"""
    email_addresses: Optional[List[Email]] = None
    r"""The email addresses of the candidate"""
    
