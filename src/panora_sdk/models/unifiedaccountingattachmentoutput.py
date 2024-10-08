"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class UnifiedAccountingAttachmentOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingAttachmentOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingAttachmentOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the attachment in the context of the 3rd Party"""
    
    

class UnifiedAccountingAttachmentOutputRemoteData(BaseModel):
    r"""The remote data of the attachment in the context of the 3rd Party"""
    
    

class UnifiedAccountingAttachmentOutputTypedDict(TypedDict):
    file_name: NotRequired[Nullable[str]]
    r"""The name of the attached file"""
    file_url: NotRequired[Nullable[str]]
    r"""The URL where the file can be accessed"""
    account_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated account"""
    field_mappings: NotRequired[Nullable[UnifiedAccountingAttachmentOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the attachment record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the attachment in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedAccountingAttachmentOutputRemoteDataTypedDict]]
    r"""The remote data of the attachment in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the attachment record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the attachment record"""
    

class UnifiedAccountingAttachmentOutput(BaseModel):
    file_name: OptionalNullable[str] = UNSET
    r"""The name of the attached file"""
    file_url: OptionalNullable[str] = UNSET
    r"""The URL where the file can be accessed"""
    account_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated account"""
    field_mappings: OptionalNullable[UnifiedAccountingAttachmentOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the attachment record"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the attachment in the context of the 3rd Party"""
    remote_data: OptionalNullable[UnifiedAccountingAttachmentOutputRemoteData] = UNSET
    r"""The remote data of the attachment in the context of the 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the attachment record"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the attachment record"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["file_name", "file_url", "account_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["file_name", "file_url", "account_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
