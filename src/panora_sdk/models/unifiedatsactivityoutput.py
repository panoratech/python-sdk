"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, TypedDict
from typing_extensions import NotRequired


class UnifiedAtsActivityOutputTypedDict(TypedDict):
    activity_type: NotRequired[Nullable[str]]
    r"""The type of activity"""
    subject: NotRequired[Nullable[str]]
    r"""The subject of the activity"""
    body: NotRequired[Nullable[str]]
    r"""The body of the activity"""
    visibility: NotRequired[Nullable[str]]
    r"""The visibility of the activity"""
    candidate_id: NotRequired[Nullable[str]]
    r"""The UUID of the candidate"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The remote creation date of the activity"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the activity"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the activity in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[Dict[str, Any]]]
    r"""The remote data of the activity in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The modified date of the object"""
    

class UnifiedAtsActivityOutput(BaseModel):
    activity_type: OptionalNullable[str] = UNSET
    r"""The type of activity"""
    subject: OptionalNullable[str] = UNSET
    r"""The subject of the activity"""
    body: OptionalNullable[str] = UNSET
    r"""The body of the activity"""
    visibility: OptionalNullable[str] = UNSET
    r"""The visibility of the activity"""
    candidate_id: OptionalNullable[str] = UNSET
    r"""The UUID of the candidate"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The remote creation date of the activity"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the activity"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the activity in the context of the 3rd Party"""
    remote_data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The remote data of the activity in the context of the 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["activity_type", "subject", "body", "visibility", "candidate_id", "remote_created_at", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["activity_type", "subject", "body", "visibility", "candidate_id", "remote_created_at", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
