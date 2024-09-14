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


class UnifiedAccountingContactOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedAccountingContactOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedAccountingContactOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the contact in the context of the 3rd Party"""


class UnifiedAccountingContactOutputRemoteData(BaseModel):
    r"""The remote data of the contact in the context of the 3rd Party"""


class UnifiedAccountingContactOutputTypedDict(TypedDict):
    name: NotRequired[Nullable[str]]
    r"""The name of the contact"""
    is_supplier: NotRequired[Nullable[bool]]
    r"""Indicates if the contact is a supplier"""
    is_customer: NotRequired[Nullable[bool]]
    r"""Indicates if the contact is a customer"""
    email_address: NotRequired[Nullable[str]]
    r"""The email address of the contact"""
    tax_number: NotRequired[Nullable[str]]
    r"""The tax number of the contact"""
    status: NotRequired[Nullable[str]]
    r"""The status of the contact"""
    currency: NotRequired[Nullable[str]]
    r"""The currency associated with the contact"""
    remote_updated_at: NotRequired[Nullable[str]]
    r"""The date when the contact was last updated in the remote system"""
    company_info_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated company info"""
    field_mappings: NotRequired[
        Nullable[UnifiedAccountingContactOutputFieldMappingsTypedDict]
    ]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the contact record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the contact in the context of the 3rd Party"""
    remote_data: NotRequired[
        Nullable[UnifiedAccountingContactOutputRemoteDataTypedDict]
    ]
    r"""The remote data of the contact in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the contact record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the contact record"""


class UnifiedAccountingContactOutput(BaseModel):
    name: OptionalNullable[str] = UNSET
    r"""The name of the contact"""

    is_supplier: OptionalNullable[bool] = UNSET
    r"""Indicates if the contact is a supplier"""

    is_customer: OptionalNullable[bool] = UNSET
    r"""Indicates if the contact is a customer"""

    email_address: OptionalNullable[str] = UNSET
    r"""The email address of the contact"""

    tax_number: OptionalNullable[str] = UNSET
    r"""The tax number of the contact"""

    status: OptionalNullable[str] = UNSET
    r"""The status of the contact"""

    currency: OptionalNullable[str] = UNSET
    r"""The currency associated with the contact"""

    remote_updated_at: OptionalNullable[str] = UNSET
    r"""The date when the contact was last updated in the remote system"""

    company_info_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated company info"""

    field_mappings: OptionalNullable[UnifiedAccountingContactOutputFieldMappings] = (
        UNSET
    )
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""

    id: OptionalNullable[str] = UNSET
    r"""The UUID of the contact record"""

    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the contact in the context of the 3rd Party"""

    remote_data: OptionalNullable[UnifiedAccountingContactOutputRemoteData] = UNSET
    r"""The remote data of the contact in the context of the 3rd Party"""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the contact record"""

    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the contact record"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "is_supplier",
            "is_customer",
            "email_address",
            "tax_number",
            "status",
            "currency",
            "remote_updated_at",
            "company_info_id",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "created_at",
            "modified_at",
        ]
        nullable_fields = [
            "name",
            "is_supplier",
            "is_customer",
            "email_address",
            "tax_number",
            "status",
            "currency",
            "remote_updated_at",
            "company_info_id",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "created_at",
            "modified_at",
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
