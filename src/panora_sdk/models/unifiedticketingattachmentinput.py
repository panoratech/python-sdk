"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, TypedDict
from typing_extensions import NotRequired


class UnifiedTicketingAttachmentInputTypedDict(TypedDict):
    file_name: Nullable[str]
    r"""The file name of the attachment"""
    file_url: Nullable[str]
    r"""The file url of the attachment"""
    uploader: Nullable[str]
    r"""The uploader's UUID of the attachment"""
    field_mappings: Nullable[Dict[str, Any]]
    r"""The custom field mappings of the attachment between the remote 3rd party & Panora"""
    ticket_id: NotRequired[Nullable[str]]
    r"""The UUID of the ticket the attachment is tied to"""
    comment_id: NotRequired[Nullable[str]]
    r"""The UUID of the comment the attachment is tied to"""
    

class UnifiedTicketingAttachmentInput(BaseModel):
    file_name: Nullable[str]
    r"""The file name of the attachment"""
    file_url: Nullable[str]
    r"""The file url of the attachment"""
    uploader: Nullable[str]
    r"""The uploader's UUID of the attachment"""
    field_mappings: Nullable[Dict[str, Any]]
    r"""The custom field mappings of the attachment between the remote 3rd party & Panora"""
    ticket_id: OptionalNullable[str] = UNSET
    r"""The UUID of the ticket the attachment is tied to"""
    comment_id: OptionalNullable[str] = UNSET
    r"""The UUID of the comment the attachment is tied to"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ticket_id", "comment_id"]
        nullable_fields = ["file_name", "file_url", "uploader", "field_mappings", "ticket_id", "comment_id"]
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
        
