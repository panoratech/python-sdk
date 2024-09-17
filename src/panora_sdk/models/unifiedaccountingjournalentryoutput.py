"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .lineitem import LineItem, LineItemTypedDict
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAccountingJournalentryOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingJournalentryOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingJournalentryOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the journal entry in the context of the 3rd Party"""
    
    

class UnifiedAccountingJournalentryOutputRemoteData(BaseModel):
    r"""The remote data of the journal entry in the context of the 3rd Party"""
    
    

class UnifiedAccountingJournalentryOutputTypedDict(TypedDict):
    transaction_date: NotRequired[Nullable[datetime]]
    r"""The date of the transaction"""
    payments: NotRequired[Nullable[List[str]]]
    r"""The payments associated with the journal entry"""
    applied_payments: NotRequired[Nullable[List[str]]]
    r"""The applied payments for the journal entry"""
    memo: NotRequired[Nullable[str]]
    r"""A memo or note for the journal entry"""
    currency: NotRequired[Nullable[str]]
    r"""The currency of the journal entry"""
    exchange_rate: NotRequired[Nullable[str]]
    r"""The exchange rate applied to the journal entry"""
    id_acc_company_info: NotRequired[str]
    r"""The UUID of the associated company info"""
    journal_number: NotRequired[Nullable[str]]
    r"""The journal number"""
    tracking_categories: NotRequired[Nullable[List[str]]]
    r"""The UUIDs of the tracking categories associated with the journal entry"""
    id_acc_accounting_period: NotRequired[Nullable[str]]
    r"""The UUID of the associated accounting period"""
    posting_status: NotRequired[Nullable[str]]
    r"""The posting status of the journal entry"""
    line_items: NotRequired[List[LineItemTypedDict]]
    r"""The line items associated with this journal entry"""
    field_mappings: NotRequired[Nullable[UnifiedAccountingJournalentryOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the journal entry record"""
    remote_id: NotRequired[str]
    r"""The remote ID of the journal entry in the context of the 3rd Party"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The date when the journal entry was created in the remote system"""
    remote_modiified_at: NotRequired[Nullable[datetime]]
    r"""The date when the journal entry was last modified in the remote system"""
    remote_data: NotRequired[Nullable[UnifiedAccountingJournalentryOutputRemoteDataTypedDict]]
    r"""The remote data of the journal entry in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the journal entry record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the journal entry record"""
    

class UnifiedAccountingJournalentryOutput(BaseModel):
    transaction_date: OptionalNullable[datetime] = UNSET
    r"""The date of the transaction"""
    payments: OptionalNullable[List[str]] = UNSET
    r"""The payments associated with the journal entry"""
    applied_payments: OptionalNullable[List[str]] = UNSET
    r"""The applied payments for the journal entry"""
    memo: OptionalNullable[str] = UNSET
    r"""A memo or note for the journal entry"""
    currency: OptionalNullable[str] = UNSET
    r"""The currency of the journal entry"""
    exchange_rate: OptionalNullable[str] = UNSET
    r"""The exchange rate applied to the journal entry"""
    id_acc_company_info: Optional[str] = None
    r"""The UUID of the associated company info"""
    journal_number: OptionalNullable[str] = UNSET
    r"""The journal number"""
    tracking_categories: OptionalNullable[List[str]] = UNSET
    r"""The UUIDs of the tracking categories associated with the journal entry"""
    id_acc_accounting_period: OptionalNullable[str] = UNSET
    r"""The UUID of the associated accounting period"""
    posting_status: OptionalNullable[str] = UNSET
    r"""The posting status of the journal entry"""
    line_items: Optional[List[LineItem]] = None
    r"""The line items associated with this journal entry"""
    field_mappings: OptionalNullable[UnifiedAccountingJournalentryOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the journal entry record"""
    remote_id: Optional[str] = None
    r"""The remote ID of the journal entry in the context of the 3rd Party"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The date when the journal entry was created in the remote system"""
    remote_modiified_at: OptionalNullable[datetime] = UNSET
    r"""The date when the journal entry was last modified in the remote system"""
    remote_data: OptionalNullable[UnifiedAccountingJournalentryOutputRemoteData] = UNSET
    r"""The remote data of the journal entry in the context of the 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the journal entry record"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the journal entry record"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["transaction_date", "payments", "applied_payments", "memo", "currency", "exchange_rate", "id_acc_company_info", "journal_number", "tracking_categories", "id_acc_accounting_period", "posting_status", "line_items", "field_mappings", "id", "remote_id", "remote_created_at", "remote_modiified_at", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["transaction_date", "payments", "applied_payments", "memo", "currency", "exchange_rate", "journal_number", "tracking_categories", "id_acc_accounting_period", "posting_status", "field_mappings", "id", "remote_created_at", "remote_modiified_at", "remote_data", "created_at", "modified_at"]
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
        
