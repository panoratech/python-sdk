"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class UnifiedHrisDependentOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisDependentOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedHrisDependentOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the dependent in the context of the 3rd Party"""
    
    

class UnifiedHrisDependentOutputRemoteData(BaseModel):
    r"""The remote data of the dependent in the context of the 3rd Party"""
    
    

class UnifiedHrisDependentOutputTypedDict(TypedDict):
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the dependent"""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the dependent"""
    middle_name: NotRequired[Nullable[str]]
    r"""The middle name of the dependent"""
    relationship: NotRequired[Nullable[str]]
    r"""The relationship of the dependent to the employee"""
    date_of_birth: NotRequired[Nullable[datetime]]
    r"""The date of birth of the dependent"""
    gender: NotRequired[Nullable[str]]
    r"""The gender of the dependent"""
    phone_number: NotRequired[Nullable[str]]
    r"""The phone number of the dependent"""
    home_location: NotRequired[Nullable[str]]
    r"""The UUID of the home location"""
    is_student: NotRequired[Nullable[bool]]
    r"""Indicates if the dependent is a student"""
    ssn: NotRequired[Nullable[str]]
    r"""The Social Security Number of the dependent"""
    employee_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated employee"""
    field_mappings: NotRequired[Nullable[UnifiedHrisDependentOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the dependent record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the dependent in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedHrisDependentOutputRemoteDataTypedDict]]
    r"""The remote data of the dependent in the context of the 3rd Party"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The date when the dependent was created in the 3rd party system"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the dependent record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the dependent record"""
    remote_was_deleted: NotRequired[Nullable[bool]]
    r"""Indicates if the dependent was deleted in the remote system"""
    

class UnifiedHrisDependentOutput(BaseModel):
    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the dependent"""
    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the dependent"""
    middle_name: OptionalNullable[str] = UNSET
    r"""The middle name of the dependent"""
    relationship: OptionalNullable[str] = UNSET
    r"""The relationship of the dependent to the employee"""
    date_of_birth: OptionalNullable[datetime] = UNSET
    r"""The date of birth of the dependent"""
    gender: OptionalNullable[str] = UNSET
    r"""The gender of the dependent"""
    phone_number: OptionalNullable[str] = UNSET
    r"""The phone number of the dependent"""
    home_location: OptionalNullable[str] = UNSET
    r"""The UUID of the home location"""
    is_student: OptionalNullable[bool] = UNSET
    r"""Indicates if the dependent is a student"""
    ssn: OptionalNullable[str] = UNSET
    r"""The Social Security Number of the dependent"""
    employee_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated employee"""
    field_mappings: OptionalNullable[UnifiedHrisDependentOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the dependent record"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the dependent in the context of the 3rd Party"""
    remote_data: OptionalNullable[UnifiedHrisDependentOutputRemoteData] = UNSET
    r"""The remote data of the dependent in the context of the 3rd Party"""
    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The date when the dependent was created in the 3rd party system"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the dependent record"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the dependent record"""
    remote_was_deleted: OptionalNullable[bool] = UNSET
    r"""Indicates if the dependent was deleted in the remote system"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["first_name", "last_name", "middle_name", "relationship", "date_of_birth", "gender", "phone_number", "home_location", "is_student", "ssn", "employee_id", "field_mappings", "id", "remote_id", "remote_data", "remote_created_at", "created_at", "modified_at", "remote_was_deleted"]
        nullable_fields = ["first_name", "last_name", "middle_name", "relationship", "date_of_birth", "gender", "phone_number", "home_location", "is_student", "ssn", "employee_id", "field_mappings", "id", "remote_id", "remote_data", "remote_created_at", "created_at", "modified_at", "remote_was_deleted"]
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
        
