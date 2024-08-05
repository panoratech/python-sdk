"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, List, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsInterviewOutputStatus(str, Enum):
    r"""The status of the interview"""
    SCHEDULED = "SCHEDULED"
    AWAITING_FEEDBACK = "AWAITING_FEEDBACK"
    COMPLETED = "COMPLETED"

class UnifiedAtsInterviewOutputTypedDict(TypedDict):
    status: NotRequired[Nullable[UnifiedAtsInterviewOutputStatus]]
    r"""The status of the interview"""
    application_id: NotRequired[Nullable[str]]
    r"""The UUID of the application"""
    job_interview_stage_id: NotRequired[Nullable[str]]
    r"""The UUID of the job interview stage"""
    organized_by: NotRequired[Nullable[str]]
    r"""The UUID of the organizer"""
    interviewers: NotRequired[Nullable[List[str]]]
    r"""The UUIDs of the interviewers"""
    location: NotRequired[Nullable[str]]
    r"""The location of the interview"""
    start_at: NotRequired[Nullable[datetime]]
    r"""The start date and time of the interview"""
    end_at: NotRequired[Nullable[datetime]]
    r"""The end date and time of the interview"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The remote creation date of the interview"""
    remote_updated_at: NotRequired[Nullable[datetime]]
    r"""The remote modification date of the interview"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the interview"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the interview in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[Dict[str, Any]]]
    r"""The remote data of the interview in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The modified date of the object"""
    

class UnifiedAtsInterviewOutput(BaseModel):
    status: OptionalNullable[UnifiedAtsInterviewOutputStatus] = UNSET
    r"""The status of the interview"""
    application_id: OptionalNullable[str] = UNSET
    r"""The UUID of the application"""
    job_interview_stage_id: OptionalNullable[str] = UNSET
    r"""The UUID of the job interview stage"""
    organized_by: OptionalNullable[str] = UNSET
    r"""The UUID of the organizer"""
    interviewers: OptionalNullable[List[str]] = UNSET
    r"""The UUIDs of the interviewers"""
    location: OptionalNullable[str] = UNSET
    r"""The location of the interview"""
    start_at: OptionalNullable[datetime] = UNSET
    r"""The start date and time of the interview"""
    end_at: OptionalNullable[datetime] = UNSET
    r"""The end date and time of the interview"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The remote creation date of the interview"""
    remote_updated_at: OptionalNullable[datetime] = UNSET
    r"""The remote modification date of the interview"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the interview"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the interview in the context of the 3rd Party"""
    remote_data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The remote data of the interview in the context of the 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["status", "application_id", "job_interview_stage_id", "organized_by", "interviewers", "location", "start_at", "end_at", "remote_created_at", "remote_updated_at", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["status", "application_id", "job_interview_stage_id", "organized_by", "interviewers", "location", "start_at", "end_at", "remote_created_at", "remote_updated_at", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
