"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from panora_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class CustomFieldCreateDtoObjectTypeOwner(str, Enum):
    COMPANY = "company"
    CONTACT = "contact"
    DEAL = "deal"
    LEAD = "lead"
    NOTE = "note"
    TASK = "task"
    ENGAGEMENT = "engagement"
    STAGE = "stage"
    USER = "user"

class CustomFieldCreateDtoDataType(str, Enum):
    r"""The data type of the custom field"""
    STRING = "string"
    NUMBER = "number"

class CustomFieldCreateDtoTypedDict(TypedDict):
    object_type_owner: Nullable[CustomFieldCreateDtoObjectTypeOwner]
    name: Nullable[str]
    r"""The name of the custom field"""
    description: Nullable[str]
    r"""The description of the custom field"""
    data_type: Nullable[CustomFieldCreateDtoDataType]
    r"""The data type of the custom field"""
    source_custom_field_id: Nullable[str]
    r"""The source custom field ID"""
    source_provider: Nullable[str]
    r"""The name of the source software/provider"""
    linked_user_id: Nullable[str]
    r"""The linked user ID"""
    

class CustomFieldCreateDto(BaseModel):
    object_type_owner: Nullable[CustomFieldCreateDtoObjectTypeOwner]
    name: Nullable[str]
    r"""The name of the custom field"""
    description: Nullable[str]
    r"""The description of the custom field"""
    data_type: Nullable[CustomFieldCreateDtoDataType]
    r"""The data type of the custom field"""
    source_custom_field_id: Nullable[str]
    r"""The source custom field ID"""
    source_provider: Nullable[str]
    r"""The name of the source software/provider"""
    linked_user_id: Nullable[str]
    r"""The linked user ID"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["object_type_owner", "name", "description", "data_type", "source_custom_field_id", "source_provider", "linked_user_id"]
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
        
