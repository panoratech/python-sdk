"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, List, TypedDict
from typing_extensions import NotRequired


class UnifiedTicketingTicketInputStatus(str, Enum):
    r"""The status of the ticket. Authorized values are OPEN or CLOSED."""
    OPEN = "OPEN"
    CLOSED = "CLOSED"

class UnifiedTicketingTicketInputType(str, Enum):
    r"""The type of the ticket. Authorized values are PROBLEM, QUESTION, or TASK"""
    BUG = "BUG"
    SUBTASK = "SUBTASK"
    TASK = "TASK"
    TO_DO = "TO-DO"

class UnifiedTicketingTicketInputPriority(str, Enum):
    r"""The priority of the ticket. Authorized values are HIGH, MEDIUM or LOW."""
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class UnifiedTicketingTicketInputCreatorType(str, Enum):
    r"""The creator type of the comment. Authorized values are either USER or CONTACT"""
    USER = "USER"
    CONTACT = "CONTACT"

class UnifiedTicketingTicketInputCommentTypedDict(TypedDict):
    r"""The comment of the ticket"""
    
    body: Nullable[str]
    r"""The body of the comment"""
    html_body: NotRequired[Nullable[str]]
    r"""The html body of the comment"""
    is_private: NotRequired[Nullable[bool]]
    r"""The public status of the comment"""
    creator_type: NotRequired[Nullable[UnifiedTicketingTicketInputCreatorType]]
    r"""The creator type of the comment. Authorized values are either USER or CONTACT"""
    ticket_id: NotRequired[Nullable[str]]
    r"""The UUID of the ticket the comment is tied to"""
    contact_id: NotRequired[Nullable[str]]
    r"""The UUID of the contact which the comment belongs to (if no user_id specified)"""
    user_id: NotRequired[Nullable[str]]
    r"""The UUID of the user which the comment belongs to (if no contact_id specified)"""
    attachments: NotRequired[Nullable[List[str]]]
    r"""The attachements UUIDs tied to the comment"""
    

class UnifiedTicketingTicketInputComment(BaseModel):
    r"""The comment of the ticket"""
    
    body: Nullable[str]
    r"""The body of the comment"""
    html_body: OptionalNullable[str] = UNSET
    r"""The html body of the comment"""
    is_private: OptionalNullable[bool] = UNSET
    r"""The public status of the comment"""
    creator_type: OptionalNullable[UnifiedTicketingTicketInputCreatorType] = UNSET
    r"""The creator type of the comment. Authorized values are either USER or CONTACT"""
    ticket_id: OptionalNullable[str] = UNSET
    r"""The UUID of the ticket the comment is tied to"""
    contact_id: OptionalNullable[str] = UNSET
    r"""The UUID of the contact which the comment belongs to (if no user_id specified)"""
    user_id: OptionalNullable[str] = UNSET
    r"""The UUID of the user which the comment belongs to (if no contact_id specified)"""
    attachments: OptionalNullable[List[str]] = UNSET
    r"""The attachements UUIDs tied to the comment"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["html_body", "is_private", "creator_type", "ticket_id", "contact_id", "user_id", "attachments"]
        nullable_fields = ["body", "html_body", "is_private", "creator_type", "ticket_id", "contact_id", "user_id", "attachments"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        

class UnifiedTicketingTicketInputTypedDict(TypedDict):
    name: Nullable[str]
    r"""The name of the ticket"""
    description: Nullable[str]
    r"""The description of the ticket"""
    status: NotRequired[Nullable[UnifiedTicketingTicketInputStatus]]
    r"""The status of the ticket. Authorized values are OPEN or CLOSED."""
    due_date: NotRequired[Nullable[datetime]]
    r"""The date the ticket is due"""
    type: NotRequired[Nullable[UnifiedTicketingTicketInputType]]
    r"""The type of the ticket. Authorized values are PROBLEM, QUESTION, or TASK"""
    parent_ticket: NotRequired[Nullable[str]]
    r"""The UUID of the parent ticket"""
    collections: NotRequired[Nullable[str]]
    r"""The collection UUIDs the ticket belongs to"""
    tags: NotRequired[Nullable[List[str]]]
    r"""The tags names of the ticket"""
    completed_at: NotRequired[Nullable[datetime]]
    r"""The date the ticket has been completed"""
    priority: NotRequired[Nullable[UnifiedTicketingTicketInputPriority]]
    r"""The priority of the ticket. Authorized values are HIGH, MEDIUM or LOW."""
    assigned_to: NotRequired[Nullable[List[str]]]
    r"""The users UUIDs the ticket is assigned to"""
    comment: NotRequired[Nullable[UnifiedTicketingTicketInputCommentTypedDict]]
    r"""The comment of the ticket"""
    account_id: NotRequired[Nullable[str]]
    r"""The UUID of the account which the ticket belongs to"""
    contact_id: NotRequired[Nullable[str]]
    r"""The UUID of the contact which the ticket belongs to"""
    attachments: NotRequired[Nullable[List[str]]]
    r"""The attachements UUIDs tied to the ticket"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the ticket between the remote 3rd party & Panora"""
    

class UnifiedTicketingTicketInput(BaseModel):
    name: Nullable[str]
    r"""The name of the ticket"""
    description: Nullable[str]
    r"""The description of the ticket"""
    status: OptionalNullable[UnifiedTicketingTicketInputStatus] = UNSET
    r"""The status of the ticket. Authorized values are OPEN or CLOSED."""
    due_date: OptionalNullable[datetime] = UNSET
    r"""The date the ticket is due"""
    type: OptionalNullable[UnifiedTicketingTicketInputType] = UNSET
    r"""The type of the ticket. Authorized values are PROBLEM, QUESTION, or TASK"""
    parent_ticket: OptionalNullable[str] = UNSET
    r"""The UUID of the parent ticket"""
    collections: OptionalNullable[str] = UNSET
    r"""The collection UUIDs the ticket belongs to"""
    tags: OptionalNullable[List[str]] = UNSET
    r"""The tags names of the ticket"""
    completed_at: OptionalNullable[datetime] = UNSET
    r"""The date the ticket has been completed"""
    priority: OptionalNullable[UnifiedTicketingTicketInputPriority] = UNSET
    r"""The priority of the ticket. Authorized values are HIGH, MEDIUM or LOW."""
    assigned_to: OptionalNullable[List[str]] = UNSET
    r"""The users UUIDs the ticket is assigned to"""
    comment: OptionalNullable[UnifiedTicketingTicketInputComment] = UNSET
    r"""The comment of the ticket"""
    account_id: OptionalNullable[str] = UNSET
    r"""The UUID of the account which the ticket belongs to"""
    contact_id: OptionalNullable[str] = UNSET
    r"""The UUID of the contact which the ticket belongs to"""
    attachments: OptionalNullable[List[str]] = UNSET
    r"""The attachements UUIDs tied to the ticket"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the ticket between the remote 3rd party & Panora"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["status", "due_date", "type", "parent_ticket", "collections", "tags", "completed_at", "priority", "assigned_to", "comment", "account_id", "contact_id", "attachments", "field_mappings"]
        nullable_fields = ["name", "description", "status", "due_date", "type", "parent_ticket", "collections", "tags", "completed_at", "priority", "assigned_to", "comment", "account_id", "contact_id", "attachments", "field_mappings"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        
