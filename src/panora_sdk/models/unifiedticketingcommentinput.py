"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class UnifiedTicketingCommentInputTypedDict(TypedDict):
    body: Nullable[str]
    r"""The body of the comment"""
    html_body: NotRequired[Nullable[str]]
    r"""The html body of the comment"""
    is_private: NotRequired[Nullable[bool]]
    r"""The public status of the comment"""
    creator_type: NotRequired[Nullable[str]]
    r"""The creator type of the comment. Authorized values are either USER or CONTACT"""
    ticket_id: NotRequired[Nullable[str]]
    r"""The UUID of the ticket the comment is tied to"""
    contact_id: NotRequired[Nullable[str]]
    r"""The UUID of the contact which the comment belongs to (if no user_id specified)"""
    user_id: NotRequired[Nullable[str]]
    r"""The UUID of the user which the comment belongs to (if no contact_id specified)"""
    attachments: NotRequired[Nullable[List[str]]]
    r"""The attachements UUIDs tied to the comment"""
    

class UnifiedTicketingCommentInput(BaseModel):
    body: Nullable[str]
    r"""The body of the comment"""
    html_body: OptionalNullable[str] = UNSET
    r"""The html body of the comment"""
    is_private: OptionalNullable[bool] = UNSET
    r"""The public status of the comment"""
    creator_type: OptionalNullable[str] = UNSET
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
        
