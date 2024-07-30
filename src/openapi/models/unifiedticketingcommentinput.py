"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedTicketingCommentInputTypedDict(TypedDict):
    body: str
    r"""The body of the comment"""
    html_body: NotRequired[str]
    r"""The html body of the comment"""
    is_private: NotRequired[bool]
    r"""The public status of the comment"""
    creator_type: NotRequired[str]
    r"""The creator type of the comment. Authorized values are either USER or CONTACT"""
    ticket_id: NotRequired[str]
    r"""The UUID of the ticket the comment is tied to"""
    contact_id: NotRequired[str]
    r"""The UUID of the contact which the comment belongs to (if no user_id specified)"""
    user_id: NotRequired[str]
    r"""The UUID of the user which the comment belongs to (if no contact_id specified)"""
    attachments: NotRequired[List[str]]
    r"""The attachements UUIDs tied to the comment"""
    

class UnifiedTicketingCommentInput(BaseModel):
    body: str
    r"""The body of the comment"""
    html_body: Optional[str] = None
    r"""The html body of the comment"""
    is_private: Optional[bool] = None
    r"""The public status of the comment"""
    creator_type: Optional[str] = None
    r"""The creator type of the comment. Authorized values are either USER or CONTACT"""
    ticket_id: Optional[str] = None
    r"""The UUID of the ticket the comment is tied to"""
    contact_id: Optional[str] = None
    r"""The UUID of the contact which the comment belongs to (if no user_id specified)"""
    user_id: Optional[str] = None
    r"""The UUID of the user which the comment belongs to (if no contact_id specified)"""
    attachments: Optional[List[str]] = None
    r"""The attachements UUIDs tied to the comment"""
    
