"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .variant import Variant, VariantTypedDict
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedEcommerceProductOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedEcommerceProductOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    
    

class UnifiedEcommerceProductOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the customer in the context of the 3rd Party"""
    
    

class UnifiedEcommerceProductOutputRemoteData(BaseModel):
    r"""The remote data of the customer in the context of the 3rd Party"""
    
    

class UnifiedEcommerceProductOutputTypedDict(TypedDict):
    product_url: NotRequired[Nullable[str]]
    r"""The URL of the product"""
    product_type: NotRequired[Nullable[str]]
    r"""The type of the product"""
    product_status: NotRequired[Nullable[str]]
    r"""The status of the product. Either ACTIVE, DRAFT OR ARCHIVED."""
    images_urls: NotRequired[Nullable[List[str]]]
    r"""The URLs of the product images"""
    description: NotRequired[Nullable[str]]
    r"""The description of the product"""
    vendor: NotRequired[Nullable[str]]
    r"""The vendor of the product"""
    variants: NotRequired[List[VariantTypedDict]]
    r"""The variants of the product"""
    tags: NotRequired[Nullable[List[str]]]
    r"""The tags associated with the product"""
    field_mappings: NotRequired[Nullable[UnifiedEcommerceProductOutputFieldMappingsTypedDict]]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the product"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the product in the context of the 3rd Party"""
    remote_data: NotRequired[Nullable[UnifiedEcommerceProductOutputRemoteDataTypedDict]]
    r"""The remote data of the customer in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[str]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[str]]
    r"""The modified date of the object"""
    

class UnifiedEcommerceProductOutput(BaseModel):
    product_url: OptionalNullable[str] = UNSET
    r"""The URL of the product"""
    product_type: OptionalNullable[str] = UNSET
    r"""The type of the product"""
    product_status: OptionalNullable[str] = UNSET
    r"""The status of the product. Either ACTIVE, DRAFT OR ARCHIVED."""
    images_urls: OptionalNullable[List[str]] = UNSET
    r"""The URLs of the product images"""
    description: OptionalNullable[str] = UNSET
    r"""The description of the product"""
    vendor: OptionalNullable[str] = UNSET
    r"""The vendor of the product"""
    variants: Optional[List[Variant]] = None
    r"""The variants of the product"""
    tags: OptionalNullable[List[str]] = UNSET
    r"""The tags associated with the product"""
    field_mappings: OptionalNullable[UnifiedEcommerceProductOutputFieldMappings] = UNSET
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: OptionalNullable[str] = UNSET
    r"""The UUID of the product"""
    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the product in the context of the 3rd Party"""
    remote_data: OptionalNullable[UnifiedEcommerceProductOutputRemoteData] = UNSET
    r"""The remote data of the customer in the context of the 3rd Party"""
    created_at: OptionalNullable[str] = UNSET
    r"""The created date of the object"""
    modified_at: OptionalNullable[str] = UNSET
    r"""The modified date of the object"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["product_url", "product_type", "product_status", "images_urls", "description", "vendor", "variants", "tags", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
        nullable_fields = ["product_url", "product_type", "product_status", "images_urls", "description", "vendor", "tags", "field_mappings", "id", "remote_id", "remote_data", "created_at", "modified_at"]
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
        
