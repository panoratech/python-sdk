"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedTicketingCommentOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedTicketingCommentOutputRemoteData(BaseModel):
    pass
    

class UnifiedTicketingCommentOutputCreatedAtTypedDict(TypedDict):
    pass
    

class UnifiedTicketingCommentOutputCreatedAt(BaseModel):
    pass
    

class UnifiedTicketingCommentOutputModifiedAtTypedDict(TypedDict):
    pass
    

class UnifiedTicketingCommentOutputModifiedAt(BaseModel):
    pass
    

class UnifiedTicketingCommentOutputTypedDict(TypedDict):
    body: str
    r"""The body of the comment"""
    remote_data: UnifiedTicketingCommentOutputRemoteDataTypedDict
    created_at: UnifiedTicketingCommentOutputCreatedAtTypedDict
    modified_at: UnifiedTicketingCommentOutputModifiedAtTypedDict
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
    id: NotRequired[str]
    r"""The UUID of the comment"""
    remote_id: NotRequired[str]
    r"""The id of the comment in the context of the 3rd Party"""
    

class UnifiedTicketingCommentOutput(BaseModel):
    body: str
    r"""The body of the comment"""
    remote_data: UnifiedTicketingCommentOutputRemoteData
    created_at: UnifiedTicketingCommentOutputCreatedAt
    modified_at: UnifiedTicketingCommentOutputModifiedAt
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
    id: Optional[str] = None
    r"""The UUID of the comment"""
    remote_id: Optional[str] = None
    r"""The id of the comment in the context of the 3rd Party"""
    
