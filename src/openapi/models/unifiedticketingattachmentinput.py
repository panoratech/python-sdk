"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedTicketingAttachmentInputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedTicketingAttachmentInputFieldMappings(BaseModel):
    pass
    

class UnifiedTicketingAttachmentInputTypedDict(TypedDict):
    file_name: str
    r"""The file name of the attachment"""
    file_url: str
    r"""The file url of the attachment"""
    uploader: str
    r"""The uploader's UUID of the attachment"""
    field_mappings: UnifiedTicketingAttachmentInputFieldMappingsTypedDict
    ticket_id: NotRequired[str]
    r"""The UUID of the ticket the attachment is tied to"""
    comment_id: NotRequired[str]
    r"""The UUID of the comment the attachment is tied to"""
    

class UnifiedTicketingAttachmentInput(BaseModel):
    file_name: str
    r"""The file name of the attachment"""
    file_url: str
    r"""The file url of the attachment"""
    uploader: str
    r"""The uploader's UUID of the attachment"""
    field_mappings: UnifiedTicketingAttachmentInputFieldMappings
    ticket_id: Optional[str] = None
    r"""The UUID of the ticket the attachment is tied to"""
    comment_id: Optional[str] = None
    r"""The UUID of the comment the attachment is tied to"""
    
