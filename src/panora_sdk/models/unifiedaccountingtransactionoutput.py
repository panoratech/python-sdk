"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .lineitem import LineItem, LineItemTypedDict
from datetime import datetime
from panora_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAccountingTransactionOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedAccountingTransactionOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedAccountingTransactionOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the tracking category in the context of the 3rd Party"""


class UnifiedAccountingTransactionOutputRemoteData(BaseModel):
    r"""The remote data of the tracking category in the context of the 3rd Party"""


class UnifiedAccountingTransactionOutputTypedDict(TypedDict):
    transaction_type: NotRequired[Nullable[str]]
    r"""The type of the transaction"""
    number: NotRequired[Nullable[str]]
    r"""The transaction number"""
    transaction_date: NotRequired[Nullable[datetime]]
    r"""The date of the transaction"""
    total_amount: NotRequired[Nullable[str]]
    r"""The total amount of the transaction"""
    exchange_rate: NotRequired[Nullable[str]]
    r"""The exchange rate applied to the transaction"""
    currency: NotRequired[Nullable[str]]
    r"""The currency of the transaction"""
    tracking_categories: NotRequired[Nullable[List[str]]]
    r"""The UUIDs of the tracking categories associated with the transaction"""
    account_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated account"""
    contact_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated contact"""
    company_info_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated company info"""
    accounting_period_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated accounting period"""
    line_items: NotRequired[List[LineItemTypedDict]]
    r"""The line items associated with this transaction"""
    field_mappings: NotRequired[
        Nullable[UnifiedAccountingTransactionOutputFieldMappingsTypedDict]
    ]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the transaction record"""
    remote_id: NotRequired[str]
    r"""The remote ID of the transaction"""
    created_at: NotRequired[datetime]
    r"""The created date of the transaction"""
    remote_data: NotRequired[
        Nullable[UnifiedAccountingTransactionOutputRemoteDataTypedDict]
    ]
    r"""The remote data of the tracking category in the context of the 3rd Party"""
    modified_at: NotRequired[datetime]
    r"""The last modified date of the transaction"""
    remote_updated_at: NotRequired[Nullable[datetime]]
    r"""The date when the transaction was last updated in the remote system"""


class UnifiedAccountingTransactionOutput(BaseModel):
    transaction_type: OptionalNullable[str] = UNSET
    r"""The type of the transaction"""

    number: OptionalNullable[str] = UNSET
    r"""The transaction number"""

    transaction_date: OptionalNullable[datetime] = UNSET
    r"""The date of the transaction"""

    total_amount: OptionalNullable[str] = UNSET
    r"""The total amount of the transaction"""

    exchange_rate: OptionalNullable[str] = UNSET
    r"""The exchange rate applied to the transaction"""

    currency: OptionalNullable[str] = UNSET
    r"""The currency of the transaction"""

    tracking_categories: OptionalNullable[List[str]] = UNSET
    r"""The UUIDs of the tracking categories associated with the transaction"""

    account_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated account"""

    contact_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated contact"""

    company_info_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated company info"""

    accounting_period_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated accounting period"""

    line_items: Optional[List[LineItem]] = None
    r"""The line items associated with this transaction"""

    field_mappings: OptionalNullable[
        UnifiedAccountingTransactionOutputFieldMappings
    ] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""

    id: OptionalNullable[str] = UNSET
    r"""The UUID of the transaction record"""

    remote_id: Optional[str] = None
    r"""The remote ID of the transaction"""

    created_at: Optional[datetime] = None
    r"""The created date of the transaction"""

    remote_data: OptionalNullable[UnifiedAccountingTransactionOutputRemoteData] = UNSET
    r"""The remote data of the tracking category in the context of the 3rd Party"""

    modified_at: Optional[datetime] = None
    r"""The last modified date of the transaction"""

    remote_updated_at: OptionalNullable[datetime] = UNSET
    r"""The date when the transaction was last updated in the remote system"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "transaction_type",
            "number",
            "transaction_date",
            "total_amount",
            "exchange_rate",
            "currency",
            "tracking_categories",
            "account_id",
            "contact_id",
            "company_info_id",
            "accounting_period_id",
            "line_items",
            "field_mappings",
            "id",
            "remote_id",
            "created_at",
            "remote_data",
            "modified_at",
            "remote_updated_at",
        ]
        nullable_fields = [
            "transaction_type",
            "number",
            "transaction_date",
            "total_amount",
            "exchange_rate",
            "currency",
            "tracking_categories",
            "account_id",
            "contact_id",
            "company_info_id",
            "accounting_period_id",
            "field_mappings",
            "id",
            "remote_data",
            "remote_updated_at",
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
