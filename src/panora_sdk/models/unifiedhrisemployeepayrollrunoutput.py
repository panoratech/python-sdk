"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .deductionitem import DeductionItem, DeductionItemTypedDict
from .earningitem import EarningItem, EarningItemTypedDict
from .taxitem import TaxItem, TaxItemTypedDict
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class UnifiedHrisEmployeepayrollrunOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisEmployeepayrollrunOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisEmployeepayrollrunOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the employee payroll run in the context of the 3rd Party"""
    
    

class UnifiedHrisEmployeepayrollrunOutputRemoteData(BaseModel):
    r"""The remote data of the employee payroll run in the context of the 3rd Party"""
    
    

class UnifiedHrisEmployeepayrollrunOutputTypedDict(TypedDict):
    employee_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated employee"""
    payroll_run_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated payroll run"""
    gross_pay: NotRequired[Nullable[float]]
    r"""The gross pay amount"""
    net_pay: NotRequired[Nullable[float]]
    r"""The net pay amount"""
    start_date: NotRequired[Nullable[datetime]]
    r"""The start date of the pay period"""
    end_date: NotRequired[Nullable[datetime]]
    r"""The end date of the pay period"""
    check_date: NotRequired[Nullable[datetime]]
    r"""The date the check was issued"""
    deductions: NotRequired[Nullable[List[DeductionItemTypedDict]]]
    r"""The list of deductions for this payroll run"""
    earnings: NotRequired[Nullable[List[EarningItemTypedDict]]]
    r"""The list of earnings for this payroll run"""
    taxes: NotRequired[Nullable[List[TaxItemTypedDict]]]
    r"""The list of taxes for this payroll run"""
    field_mappings: NotRequired[Nullable[UnifiedHrisEmployeepayrollrunOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the employee payroll run record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the employee payroll run in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedHrisEmployeepayrollrunOutputRemoteDataTypedDict]]
    r"""The remote data of the employee payroll run in the context of the 3rd Party"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The date when the employee payroll run was created in the 3rd party system"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the employee payroll run record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the employee payroll run record"""
    remote_was_deleted: NotRequired[Nullable[bool]]
    r"""Indicates if the employee payroll run was deleted in the remote system"""
    

class UnifiedHrisEmployeepayrollrunOutput(BaseModel):
    employee_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated employee"""
    payroll_run_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated payroll run"""
    gross_pay: OptionalNullable[float] = UNSET
    r"""The gross pay amount"""
    net_pay: OptionalNullable[float] = UNSET
    r"""The net pay amount"""
    start_date: OptionalNullable[datetime] = UNSET
    r"""The start date of the pay period"""
    end_date: OptionalNullable[datetime] = UNSET
    r"""The end date of the pay period"""
    check_date: OptionalNullable[datetime] = UNSET
    r"""The date the check was issued"""
    deductions: OptionalNullable[List[DeductionItem]] = UNSET
    r"""The list of deductions for this payroll run"""
    earnings: OptionalNullable[List[EarningItem]] = UNSET
    r"""The list of earnings for this payroll run"""
    taxes: OptionalNullable[List[TaxItem]] = UNSET
    r"""The list of taxes for this payroll run"""
    field_mappings: OptionalNullable[UnifiedHrisEmployeepayrollrunOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the employee payroll run record"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the employee payroll run in the context of the 3rd Party"""
    remote_data: OptionalNullable[UnifiedHrisEmployeepayrollrunOutputRemoteData] = UNSET
    r"""The remote data of the employee payroll run in the context of the 3rd Party"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The date when the employee payroll run was created in the 3rd party system"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the employee payroll run record"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the employee payroll run record"""
    remote_was_deleted: OptionalNullable[bool] = UNSET
    r"""Indicates if the employee payroll run was deleted in the remote system"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["employee_id", "payroll_run_id", "gross_pay", "net_pay", "start_date", "end_date", "check_date", "deductions", "earnings", "taxes", "field_mappings", "id", "remote_id", "remote_data", "remote_created_at", "created_at", "modified_at", "remote_was_deleted"]
        nullable_fields = ["employee_id", "payroll_run_id", "gross_pay", "net_pay", "start_date", "end_date", "check_date", "deductions", "earnings", "taxes", "field_mappings", "id", "remote_id", "remote_data", "remote_created_at", "created_at", "modified_at", "remote_was_deleted"]
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
        
