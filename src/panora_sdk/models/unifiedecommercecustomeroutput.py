"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class UnifiedEcommerceCustomerOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedEcommerceCustomerOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedEcommerceCustomerOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the customer in the context of the 3rd Party"""
    
    

class UnifiedEcommerceCustomerOutputRemoteData(BaseModel):
    r"""The remote data of the customer in the context of the 3rd Party"""
    
    

class UnifiedEcommerceCustomerOutputTypedDict(TypedDict):
    email: NotRequired[Nullable[str]]
    r"""The email of the customer"""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the customer"""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the customer"""
    phone_number: NotRequired[Nullable[str]]
    r"""The phone number of the customer"""
    addresses: NotRequired[Nullable[List[AddressTypedDict]]]
    r"""The addresses of the customer"""
    field_mappings: NotRequired[Nullable[UnifiedEcommerceCustomerOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the customer"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the customer in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedEcommerceCustomerOutputRemoteDataTypedDict]]
    r"""The remote data of the customer in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[str]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[str]]
    r"""The modified date of the object"""
    

class UnifiedEcommerceCustomerOutput(BaseModel):
    email: OptionalNullable[str] = UNSET
    r"""The email of the customer"""
    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the customer"""
    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the customer"""
    phone_number: OptionalNullable[str] = UNSET
    r"""The phone number of the customer"""
    addresses: OptionalNullable[List[Address]] = UNSET
    r"""The addresses of the customer"""
    field_mappings: OptionalNullable[UnifiedEcommerceCustomerOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the customer"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the customer in the context of the 3rd Party"""
    remote_data: OptionalNullable[UnifiedEcommerceCustomerOutputRemoteData] = UNSET
    r"""The remote data of the customer in the context of the 3rd Party"""
    created_at: OptionalNullable[str] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[str] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email", "first_name", "last_name", "phone_number", "addresses", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["email", "first_name", "last_name", "phone_number", "addresses", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
