"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, TypedDict
from typing_extensions import NotRequired


class UnifiedCrmTaskOutputStatus(str, Enum):
    r"""The status of the task. Authorized values are PENDING, COMPLETED."""
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"

class UnifiedCrmTaskOutputTypedDict(TypedDict):
    subject: Nullable[str]
    r"""The subject of the task"""
    content: Nullable[str]
    r"""The content of the task"""
    status: Nullable[UnifiedCrmTaskOutputStatus]
    r"""The status of the task. Authorized values are PENDING, COMPLETED."""
    due_date: NotRequired[Nullable[str]]
    r"""The due date of the task"""
    finished_date: NotRequired[Nullable[str]]
    r"""The finished date of the task"""
    user_id: NotRequired[Nullable[str]]
    r"""The UUID of the user tied to the task"""
    company_id: NotRequired[Nullable[str]]
    r"""The UUID of the company tied to the task"""
    deal_id: NotRequired[Nullable[str]]
    r"""The UUID of the deal tied to the task"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the task between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the task"""
    remote_id: NotRequired[Nullable[str]]
    r"""The ID of the task in the context of the Crm 3rd Party"""
    remote_data: NotRequired[Nullable[Dict[str, Any]]]
    r"""The remote data of the task in the context of the Crm 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The modified date of the object"""
    

class UnifiedCrmTaskOutput(BaseModel):
    subject: Nullable[str]
    r"""The subject of the task"""
    content: Nullable[str]
    r"""The content of the task"""
    status: Nullable[UnifiedCrmTaskOutputStatus]
    r"""The status of the task. Authorized values are PENDING, COMPLETED."""
    due_date: OptionalNullable[str] = UNSET
    r"""The due date of the task"""
    finished_date: OptionalNullable[str] = UNSET
    r"""The finished date of the task"""
    user_id: OptionalNullable[str] = UNSET
    r"""The UUID of the user tied to the task"""
    company_id: OptionalNullable[str] = UNSET
    r"""The UUID of the company tied to the task"""
    deal_id: OptionalNullable[str] = UNSET
    r"""The UUID of the deal tied to the task"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the task between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the task"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The ID of the task in the context of the Crm 3rd Party"""
    remote_data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The remote data of the task in the context of the Crm 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["due_date", "finished_date", "user_id", "company_id", "deal_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["subject", "content", "status", "due_date", "finished_date", "user_id", "company_id", "deal_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
