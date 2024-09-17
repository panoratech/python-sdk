"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .email import Email, EmailTypedDict
from .phone import Phone, PhoneTypedDict
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, List, TypedDict
from typing_extensions import NotRequired


class UnifiedCrmContactOutputTypedDict(TypedDict):
    first_name: Nullable[str]
    r"""The first name of the contact"""
    last_name: Nullable[str]
    r"""The last name of the contact"""
    email_addresses: NotRequired[Nullable[List[EmailTypedDict]]]
    r"""The email addresses of the contact"""
    phone_numbers: NotRequired[Nullable[List[PhoneTypedDict]]]
    r"""The phone numbers of the contact"""
    addresses: NotRequired[Nullable[List[AddressTypedDict]]]
    r"""The addresses of the contact"""
    user_id: NotRequired[Nullable[str]]
    r"""The UUID of the user who owns the contact"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the contact between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the contact"""
    remote_id: NotRequired[Nullable[str]]
    r"""The id of the contact in the context of the Crm 3rd Party"""
    remote_data: NotRequired[Nullable[Dict[str, Any]]]
    r"""The remote data of the contact in the context of the Crm 3rd Party"""
    created_at: NotRequired[Nullable[datetime]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[datetime]]
    r"""The modified date of the object"""
    

class UnifiedCrmContactOutput(BaseModel):
    first_name: Nullable[str]
    r"""The first name of the contact"""
    last_name: Nullable[str]
    r"""The last name of the contact"""
    email_addresses: OptionalNullable[List[Email]] = UNSET
    r"""The email addresses of the contact"""
    phone_numbers: OptionalNullable[List[Phone]] = UNSET
    r"""The phone numbers of the contact"""
    addresses: OptionalNullable[List[Address]] = UNSET
    r"""The addresses of the contact"""
    user_id: OptionalNullable[str] = UNSET
    r"""The UUID of the user who owns the contact"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the contact between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the contact"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The id of the contact in the context of the Crm 3rd Party"""
    remote_data: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The remote data of the contact in the context of the Crm 3rd Party"""
    created_at: OptionalNullable[datetime] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[datetime] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email_addresses", "phone_numbers", "addresses", "user_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["first_name", "last_name", "email_addresses", "phone_numbers", "addresses", "user_id", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
