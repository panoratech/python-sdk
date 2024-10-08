"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedHrisTimesheetEntryOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisTimesheetEntryOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisTimesheetEntryOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the timesheet entry in the context of the 3rd Party"""
    
    

class UnifiedHrisTimesheetEntryOutputRemoteData(BaseModel):
    r"""The remote data of the timesheet entry in the context of the 3rd Party"""
    
    

class UnifiedHrisTimesheetEntryOutputTypedDict(TypedDict):
    hours_worked: NotRequired[Nullable[float]]
    r"""The number of hours worked"""
    start_time: NotRequired[Nullable[datetime]]
    r"""The start time of the timesheet entry"""
    end_time: NotRequired[Nullable[datetime]]
    r"""The end time of the timesheet entry"""
    employee_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated employee"""
    remote_was_deleted: NotRequired[bool]
    r"""Indicates if the timesheet entry was deleted in the remote system"""
    field_mappings: NotRequired[Nullable[UnifiedHrisTimesheetEntryOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the timesheet entry record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the timesheet entry"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The date when the timesheet entry was created in the remote system"""
    created_at: NotRequired[datetime]
    r"""The created date of the timesheet entry"""
    modified_at: NotRequired[datetime]
    r"""The last modified date of the timesheet entry"""
    remote_data: NotRequired[Nullable[UnifiedHrisTimesheetEntryOutputRemoteDataTypedDict]]
    r"""The remote data of the timesheet entry in the context of the 3rd Party"""
    

class UnifiedHrisTimesheetEntryOutput(BaseModel):
    hours_worked: OptionalNullable[float] = UNSET
    r"""The number of hours worked"""
    start_time: OptionalNullable[datetime] = UNSET
    r"""The start time of the timesheet entry"""
    end_time: OptionalNullable[datetime] = UNSET
    r"""The end time of the timesheet entry"""
    employee_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated employee"""
    remote_was_deleted: Optional[bool] = None
    r"""Indicates if the timesheet entry was deleted in the remote system"""
    field_mappings: OptionalNullable[UnifiedHrisTimesheetEntryOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the timesheet entry record"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the timesheet entry"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The date when the timesheet entry was created in the remote system"""
    created_at: Optional[datetime] = None
    r"""The created date of the timesheet entry"""
    modified_at: Optional[datetime] = None
    r"""The last modified date of the timesheet entry"""
    remote_data: OptionalNullable[UnifiedHrisTimesheetEntryOutputRemoteData] = UNSET
    r"""The remote data of the timesheet entry in the context of the 3rd Party"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["hours_worked", "start_time", "end_time", "employee_id", "remote_was_deleted", "field_mappings", "id", "remote_id", "remote_created_at", "created_at", "modified_at", "remote_data"]
        nullable_fields = ["hours_worked", "start_time", "end_time", "employee_id", "field_mappings", "id", "remote_id", "remote_created_at", "remote_data"]
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
        
