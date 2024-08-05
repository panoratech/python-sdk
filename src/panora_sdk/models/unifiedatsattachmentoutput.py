"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, TypedDict
from typing_extensions import NotRequired


class AttachmentType(str, Enum):
    r"""The type of the file"""
    RESUME = "RESUME"
    COVER_LETTER = "COVER_LETTER"
    OFFER_LETTER = "OFFER_LETTER"
    OTHER = "OTHER"

class UnifiedAtsAttachmentOutputTypedDict(TypedDict):
    file_url: NotRequired[Nullable[str]]
    r"""The URL of the file"""
    file_name: NotRequired[Nullable[str]]
    r"""The name of the file"""
    attachment_type: NotRequired[Nullable[AttachmentType]]
    r"""The type of the file"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The remote creation date of the attachment"""
    remote_modified_at: NotRequired[Nullable[datetime]]
    r"""The remote modification date of the attachment"""
    candidate_id: NotRequired[Nullable[str]]
    r"""The UUID of the candidate"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the attachment"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the attachment"""
    remote_data: NotRequired[Nullable[Dict[str, Any]]]
    r"""The remote data of the attachment in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The modified date of the object"""
    

class UnifiedAtsAttachmentOutput(BaseModel):
    file_url: OptionalNullable[str] = UNSET
    r"""The URL of the file"""
    file_name: OptionalNullable[str] = UNSET
    r"""The name of the file"""
    attachment_type: OptionalNullable[AttachmentType] = UNSET
    r"""The type of the file"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The remote creation date of the attachment"""
    remote_modified_at: OptionalNullable[datetime] = UNSET
    r"""The remote modification date of the attachment"""
    candidate_id: OptionalNullable[str] = UNSET
    r"""The UUID of the candidate"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the attachment"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the attachment"""
    remote_data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The remote data of the attachment in the context of the 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["file_url", "file_name", "attachment_type", "remote_created_at", "remote_modified_at", "candidate_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["file_url", "file_name", "attachment_type", "remote_created_at", "remote_modified_at", "candidate_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
