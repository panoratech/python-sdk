"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class UnifiedHrisEmploymentOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisEmploymentOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisEmploymentOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the employment in the context of the 3rd Party"""
    
    

class UnifiedHrisEmploymentOutputRemoteData(BaseModel):
    r"""The remote data of the employment in the context of the 3rd Party"""
    
    

class UnifiedHrisEmploymentOutputTypedDict(TypedDict):
    job_title: NotRequired[Nullable[str]]
    r"""The job title of the employment"""
    pay_rate: NotRequired[Nullable[float]]
    r"""The pay rate of the employment"""
    pay_period: NotRequired[Nullable[str]]
    r"""The pay period of the employment"""
    pay_frequency: NotRequired[Nullable[str]]
    r"""The pay frequency of the employment"""
    pay_currency: NotRequired[Nullable[str]]
    r"""The currency of the pay"""
    flsa_status: NotRequired[Nullable[str]]
    r"""The FLSA status of the employment"""
    effective_date: NotRequired[Nullable[datetime]]
    r"""The effective date of the employment"""
    employment_type: NotRequired[Nullable[str]]
    r"""The type of employment"""
    pay_group_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated pay group"""
    employee_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated employee"""
    field_mappings: NotRequired[Nullable[UnifiedHrisEmploymentOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the employment record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the employment in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedHrisEmploymentOutputRemoteDataTypedDict]]
    r"""The remote data of the employment in the context of the 3rd Party"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The date when the employment was created in the 3rd party system"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the employment record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the employment record"""
    remote_was_deleted: NotRequired[Nullable[bool]]
    r"""Indicates if the employment was deleted in the remote system"""
    

class UnifiedHrisEmploymentOutput(BaseModel):
    job_title: OptionalNullable[str] = UNSET
    r"""The job title of the employment"""
    pay_rate: OptionalNullable[float] = UNSET
    r"""The pay rate of the employment"""
    pay_period: OptionalNullable[str] = UNSET
    r"""The pay period of the employment"""
    pay_frequency: OptionalNullable[str] = UNSET
    r"""The pay frequency of the employment"""
    pay_currency: OptionalNullable[str] = UNSET
    r"""The currency of the pay"""
    flsa_status: OptionalNullable[str] = UNSET
    r"""The FLSA status of the employment"""
    effective_date: OptionalNullable[datetime] = UNSET
    r"""The effective date of the employment"""
    employment_type: OptionalNullable[str] = UNSET
    r"""The type of employment"""
    pay_group_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated pay group"""
    employee_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated employee"""
    field_mappings: OptionalNullable[UnifiedHrisEmploymentOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the employment record"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the employment in the context of the 3rd Party"""
    remote_data: OptionalNullable[UnifiedHrisEmploymentOutputRemoteData] = UNSET
    r"""The remote data of the employment in the context of the 3rd Party"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The date when the employment was created in the 3rd party system"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the employment record"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the employment record"""
    remote_was_deleted: OptionalNullable[bool] = UNSET
    r"""Indicates if the employment was deleted in the remote system"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["job_title", "pay_rate", "pay_period", "pay_frequency", "pay_currency", "flsa_status", "effective_date", "employment_type", "pay_group_id", "employee_id", "field_mappings", "id", "remote_id", "remote_data", "remote_created_at", "created_at", "modified_at", "remote_was_deleted"]
        nullable_fields = ["job_title", "pay_rate", "pay_period", "pay_frequency", "pay_currency", "flsa_status", "effective_date", "employment_type", "pay_group_id", "employee_id", "field_mappings", "id", "remote_id", "remote_data", "remote_created_at", "created_at", "modified_at", "remote_was_deleted"]
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
        
