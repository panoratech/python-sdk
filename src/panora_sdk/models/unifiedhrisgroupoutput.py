"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class UnifiedHrisGroupOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedHrisGroupOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedHrisGroupOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the group in the context of the 3rd Party"""


class UnifiedHrisGroupOutputRemoteData(BaseModel):
    r"""The remote data of the group in the context of the 3rd Party"""


class UnifiedHrisGroupOutputTypedDict(TypedDict):
    parent_group: NotRequired[Nullable[str]]
    r"""The UUID of the parent group"""
    name: NotRequired[Nullable[str]]
    r"""The name of the group"""
    type: NotRequired[Nullable[str]]
    r"""The type of the group"""
    field_mappings: NotRequired[Nullable[UnifiedHrisGroupOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the group record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the group in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedHrisGroupOutputRemoteDataTypedDict]]
    r"""The remote data of the group in the context of the 3rd Party"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The date when the group was created in the 3rd party system"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the group record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the group record"""
    remote_was_deleted: NotRequired[Nullable[bool]]
    r"""Indicates if the group was deleted in the remote system"""


class UnifiedHrisGroupOutput(BaseModel):
    parent_group: OptionalNullable[str] = UNSET
    r"""The UUID of the parent group"""

    name: OptionalNullable[str] = UNSET
    r"""The name of the group"""

    type: OptionalNullable[str] = UNSET
    r"""The type of the group"""

    field_mappings: OptionalNullable[UnifiedHrisGroupOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""

    id: OptionalNullable[str] = UNSET
    r"""The UUID of the group record"""

    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the group in the context of the 3rd Party"""

    remote_data: OptionalNullable[UnifiedHrisGroupOutputRemoteData] = UNSET
    r"""The remote data of the group in the context of the 3rd Party"""

    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The date when the group was created in the 3rd party system"""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the group record"""

    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the group record"""

    remote_was_deleted: OptionalNullable[bool] = UNSET
    r"""Indicates if the group was deleted in the remote system"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "parent_group",
            "name",
            "type",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "remote_created_at",
            "created_at",
            "modified_at",
            "remote_was_deleted",
        ]
        nullable_fields = [
            "parent_group",
            "name",
            "type",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "remote_created_at",
            "created_at",
            "modified_at",
            "remote_was_deleted",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
