"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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


class UnifiedAccountingAccountInputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedAccountingAccountInputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedAccountingAccountInputTypedDict(TypedDict):
    name: NotRequired[Nullable[str]]
    r"""The name of the account"""
    description: NotRequired[Nullable[str]]
    r"""A description of the account"""
    classification: NotRequired[Nullable[str]]
    r"""The classification of the account"""
    type: NotRequired[Nullable[str]]
    r"""The type of the account"""
    status: NotRequired[Nullable[str]]
    r"""The status of the account"""
    current_balance: NotRequired[Nullable[float]]
    r"""The current balance of the account"""
    currency: NotRequired[Nullable[str]]
    r"""The currency of the account"""
    account_number: NotRequired[Nullable[str]]
    r"""The account number"""
    parent_account: NotRequired[Nullable[str]]
    r"""The UUID of the parent account"""
    company_info_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated company info"""
    field_mappings: NotRequired[
        Nullable[UnifiedAccountingAccountInputFieldMappingsTypedDict]
    ]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedAccountingAccountInput(BaseModel):
    name: OptionalNullable[str] = UNSET
    r"""The name of the account"""

    description: OptionalNullable[str] = UNSET
    r"""A description of the account"""

    classification: OptionalNullable[str] = UNSET
    r"""The classification of the account"""

    type: OptionalNullable[str] = UNSET
    r"""The type of the account"""

    status: OptionalNullable[str] = UNSET
    r"""The status of the account"""

    current_balance: OptionalNullable[float] = UNSET
    r"""The current balance of the account"""

    currency: OptionalNullable[str] = UNSET
    r"""The currency of the account"""

    account_number: OptionalNullable[str] = UNSET
    r"""The account number"""

    parent_account: OptionalNullable[str] = UNSET
    r"""The UUID of the parent account"""

    company_info_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated company info"""

    field_mappings: OptionalNullable[UnifiedAccountingAccountInputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "description",
            "classification",
            "type",
            "status",
            "current_balance",
            "currency",
            "account_number",
            "parent_account",
            "company_info_id",
            "field_mappings",
        ]
        nullable_fields = [
            "name",
            "description",
            "classification",
            "type",
            "status",
            "current_balance",
            "currency",
            "account_number",
            "parent_account",
            "company_info_id",
            "field_mappings",
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
