"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class UnifiedAccountingAttachmentInputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingAttachmentInputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingAttachmentInputTypedDict(TypedDict):
    file_name: NotRequired[Nullable[str]]
    r"""The name of the attached file"""
    file_url: NotRequired[Nullable[str]]
    r"""The URL where the file can be accessed"""
    account_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated account"""
    field_mappings: NotRequired[Nullable[UnifiedAccountingAttachmentInputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    

class UnifiedAccountingAttachmentInput(BaseModel):
    file_name: OptionalNullable[str] = UNSET
    r"""The name of the attached file"""
    file_url: OptionalNullable[str] = UNSET
    r"""The URL where the file can be accessed"""
    account_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated account"""
    field_mappings: OptionalNullable[UnifiedAccountingAttachmentInputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["file_name", "file_url", "account_id", "field_mappings"]
        nullable_fields = ["file_name", "file_url", "account_id", "field_mappings"]
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
        
