"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class UnifiedHrisEmployeeOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedHrisEmployeeOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedHrisEmployeeOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the employee in the context of the 3rd Party"""


class UnifiedHrisEmployeeOutputRemoteData(BaseModel):
    r"""The remote data of the employee in the context of the 3rd Party"""


class UnifiedHrisEmployeeOutputTypedDict(TypedDict):
    groups: NotRequired[Nullable[List[str]]]
    r"""The groups the employee belongs to"""
    locations: NotRequired[Nullable[List[str]]]
    r"""UUIDs of the of the Location associated with the company"""
    employee_number: NotRequired[Nullable[str]]
    r"""The employee number"""
    company_id: NotRequired[Nullable[str]]
    r"""The UUID of the associated company"""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the employee"""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the employee"""
    preferred_name: NotRequired[Nullable[str]]
    r"""The preferred name of the employee"""
    display_full_name: NotRequired[Nullable[str]]
    r"""The full display name of the employee"""
    username: NotRequired[Nullable[str]]
    r"""The username of the employee"""
    work_email: NotRequired[Nullable[str]]
    r"""The work email of the employee"""
    personal_email: NotRequired[Nullable[str]]
    r"""The personal email of the employee"""
    mobile_phone_number: NotRequired[Nullable[str]]
    r"""The mobile phone number of the employee"""
    employments: NotRequired[Nullable[List[str]]]
    r"""The employments of the employee"""
    ssn: NotRequired[Nullable[str]]
    r"""The Social Security Number of the employee"""
    gender: NotRequired[Nullable[str]]
    r"""The gender of the employee"""
    ethnicity: NotRequired[Nullable[str]]
    r"""The ethnicity of the employee"""
    marital_status: NotRequired[Nullable[str]]
    r"""The marital status of the employee"""
    date_of_birth: NotRequired[Nullable[datetime]]
    r"""The date of birth of the employee"""
    start_date: NotRequired[Nullable[datetime]]
    r"""The start date of the employee"""
    employment_status: NotRequired[Nullable[str]]
    r"""The employment status of the employee"""
    termination_date: NotRequired[Nullable[datetime]]
    r"""The termination date of the employee"""
    avatar_url: NotRequired[Nullable[str]]
    r"""The URL of the employee's avatar"""
    manager_id: NotRequired[Nullable[str]]
    r"""UUID of the manager (employee) of the employee"""
    field_mappings: NotRequired[
        Nullable[UnifiedHrisEmployeeOutputFieldMappingsTypedDict]
    ]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the employee record"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the employee in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedHrisEmployeeOutputRemoteDataTypedDict]]
    r"""The remote data of the employee in the context of the 3rd Party"""
    remote_created_at: NotRequired[Nullable[datetime]]
    r"""The date when the employee was created in the 3rd party system"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the employee record"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The last modified date of the employee record"""
    remote_was_deleted: NotRequired[Nullable[bool]]
    r"""Indicates if the employee was deleted in the remote system"""


class UnifiedHrisEmployeeOutput(BaseModel):
    groups: OptionalNullable[List[str]] = UNSET
    r"""The groups the employee belongs to"""

    locations: OptionalNullable[List[str]] = UNSET
    r"""UUIDs of the of the Location associated with the company"""

    employee_number: OptionalNullable[str] = UNSET
    r"""The employee number"""

    company_id: OptionalNullable[str] = UNSET
    r"""The UUID of the associated company"""

    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the employee"""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the employee"""

    preferred_name: OptionalNullable[str] = UNSET
    r"""The preferred name of the employee"""

    display_full_name: OptionalNullable[str] = UNSET
    r"""The full display name of the employee"""

    username: OptionalNullable[str] = UNSET
    r"""The username of the employee"""

    work_email: OptionalNullable[str] = UNSET
    r"""The work email of the employee"""

    personal_email: OptionalNullable[str] = UNSET
    r"""The personal email of the employee"""

    mobile_phone_number: OptionalNullable[str] = UNSET
    r"""The mobile phone number of the employee"""

    employments: OptionalNullable[List[str]] = UNSET
    r"""The employments of the employee"""

    ssn: OptionalNullable[str] = UNSET
    r"""The Social Security Number of the employee"""

    gender: OptionalNullable[str] = UNSET
    r"""The gender of the employee"""

    ethnicity: OptionalNullable[str] = UNSET
    r"""The ethnicity of the employee"""

    marital_status: OptionalNullable[str] = UNSET
    r"""The marital status of the employee"""

    date_of_birth: OptionalNullable[datetime] = UNSET
    r"""The date of birth of the employee"""

    start_date: OptionalNullable[datetime] = UNSET
    r"""The start date of the employee"""

    employment_status: OptionalNullable[str] = UNSET
    r"""The employment status of the employee"""

    termination_date: OptionalNullable[datetime] = UNSET
    r"""The termination date of the employee"""

    avatar_url: OptionalNullable[str] = UNSET
    r"""The URL of the employee's avatar"""

    manager_id: OptionalNullable[str] = UNSET
    r"""UUID of the manager (employee) of the employee"""

    field_mappings: OptionalNullable[UnifiedHrisEmployeeOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""

    id: OptionalNullable[str] = UNSET
    r"""The UUID of the employee record"""

    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the employee in the context of the 3rd Party"""

    remote_data: OptionalNullable[UnifiedHrisEmployeeOutputRemoteData] = UNSET
    r"""The remote data of the employee in the context of the 3rd Party"""

    remote_created_at: OptionalNullable[datetime] = UNSET
    r"""The date when the employee was created in the 3rd party system"""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the employee record"""

    modified_at: OptionalNullable[datetime] = UNSET
    r"""The last modified date of the employee record"""

    remote_was_deleted: OptionalNullable[bool] = UNSET
    r"""Indicates if the employee was deleted in the remote system"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "groups",
            "locations",
            "employee_number",
            "company_id",
            "first_name",
            "last_name",
            "preferred_name",
            "display_full_name",
            "username",
            "work_email",
            "personal_email",
            "mobile_phone_number",
            "employments",
            "ssn",
            "gender",
            "ethnicity",
            "marital_status",
            "date_of_birth",
            "start_date",
            "employment_status",
            "termination_date",
            "avatar_url",
            "manager_id",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "remote_created_at",
            "created_at",
            "modified_at",
            "remote_was_deleted",
        ]
        nullable_fields = [
            "groups",
            "locations",
            "employee_number",
            "company_id",
            "first_name",
            "last_name",
            "preferred_name",
            "display_full_name",
            "username",
            "work_email",
            "personal_email",
            "mobile_phone_number",
            "employments",
            "ssn",
            "gender",
            "ethnicity",
            "marital_status",
            "date_of_birth",
            "start_date",
            "employment_status",
            "termination_date",
            "avatar_url",
            "manager_id",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "remote_created_at",
            "created_at",
            "modified_at",
            "remote_was_deleted",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
