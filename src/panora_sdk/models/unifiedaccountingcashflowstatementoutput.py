"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .lineitem import LineItem, LineItemTypedDict
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedAccountingCashflowstatementOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingCashflowstatementOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedAccountingCashflowstatementOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the cash flow statement in the context of the 3rd Party"""
    
    

class UnifiedAccountingCashflowstatementOutputRemoteData(BaseModel):
    r"""The remote data of the cash flow statement in the context of the 3rd Party"""
    
    

class UnifiedAccountingCashflowstatementOutputTypedDict(TypedDict):
    name: NotRequired[Nullable[str]]
    r"""The name of the cash flow statement"""
    currency: NotRequired[Nullable[str]]
    r"""The currency used in the cash flow statement"""
    company_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated company"""
    start_period: NotRequired[Nullable[datetime]]
    r"""The start date of the period covered by the cash flow statement"""
    end_period: NotRequired[Nullable[datetime]]
    r"""The end date of the period covered by the cash flow statement"""
    cash_at_beginning_of_period: NotRequired[Nullable[float]]
    r"""The cash balance at the beginning of the period"""
    cash_at_end_of_period: NotRequired[Nullable[float]]
    r"""The cash balance at the end of the period"""
    remote_generated_at: NotRequired[Nullable[datetime]]
    r"""The date when the cash flow statement was generated in the remote system"""
    line_items: NotRequired[List[LineItemTypedDict]]
    r"""The report items associated with this cash flow statement"""
    field_mappings: NotRequired[Nullable[UnifiedAccountingCashflowstatementOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the cash flow statement record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the cash flow statement in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedAccountingCashflowstatementOutputRemoteDataTypedDict]]
    r"""The remote data of the cash flow statement in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the cash flow statement record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the cash flow statement record"""
    

class UnifiedAccountingCashflowstatementOutput(BaseModel):
    name: OptionalNullable[str] = UNSET
    r"""The name of the cash flow statement"""
    currency: OptionalNullable[str] = UNSET
    r"""The currency used in the cash flow statement"""
    company_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated company"""
    start_period: OptionalNullable[datetime] = UNSET
    r"""The start date of the period covered by the cash flow statement"""
    end_period: OptionalNullable[datetime] = UNSET
    r"""The end date of the period covered by the cash flow statement"""
    cash_at_beginning_of_period: OptionalNullable[float] = UNSET
    r"""The cash balance at the beginning of the period"""
    cash_at_end_of_period: OptionalNullable[float] = UNSET
    r"""The cash balance at the end of the period"""
    remote_generated_at: OptionalNullable[datetime] = UNSET
    r"""The date when the cash flow statement was generated in the remote system"""
    line_items: Optional[List[LineItem]] = None
    r"""The report items associated with this cash flow statement"""
    field_mappings: OptionalNullable[UnifiedAccountingCashflowstatementOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the cash flow statement record"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the cash flow statement in the context of the 3rd Party"""
    remote_data: OptionalNullable[UnifiedAccountingCashflowstatementOutputRemoteData] = UNSET
    r"""The remote data of the cash flow statement in the context of the 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the cash flow statement record"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the cash flow statement record"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "currency", "company_id", "start_period", "end_period", "cash_at_beginning_of_period", "cash_at_end_of_period", "remote_generated_at", "line_items", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["name", "currency", "company_id", "start_period", "end_period", "cash_at_beginning_of_period", "cash_at_end_of_period", "remote_generated_at", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
