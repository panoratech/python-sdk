"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, TypedDict
from typing_extensions import NotRequired


class UnifiedFilestorageDriveOutputTypedDict(TypedDict):
    name: Nullable[str]
    r"""The name of the drive"""
    remote_created_at: Nullable[str]
    r"""When the third party s drive was created."""
    drive_url: Nullable[str]
    r"""The url of the drive"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the drive"""
    remote_id: NotRequired[Nullable[str]]
    r"""The id of the drive in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[Dict[str, Any]]]
    r"""The remote data of the drive in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The modified date of the object"""
    

class UnifiedFilestorageDriveOutput(BaseModel):
    name: Nullable[str]
    r"""The name of the drive"""
    remote_created_at: Nullable[str]
    r"""When the third party s drive was created."""
    drive_url: Nullable[str]
    r"""The url of the drive"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the drive"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The id of the drive in the context of the 3rd Party"""
    remote_data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The remote data of the drive in the context of the 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["name", "remote_created_at", "drive_url", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
