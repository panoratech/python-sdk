"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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


class ItemsModelTypedDict(TypedDict):
    r"""The items in the fulfilment"""


class ItemsModel(BaseModel):
    r"""The items in the fulfilment"""


class UnifiedEcommerceFulfillmentOutputFieldMappingsTypedDict(TypedDict):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedEcommerceFulfillmentOutputFieldMappings(BaseModel):
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""


class UnifiedEcommerceFulfillmentOutputRemoteDataTypedDict(TypedDict):
    r"""The remote data of the customer in the context of the 3rd Party"""


class UnifiedEcommerceFulfillmentOutputRemoteData(BaseModel):
    r"""The remote data of the customer in the context of the 3rd Party"""


class UnifiedEcommerceFulfillmentOutputTypedDict(TypedDict):
    carrier: NotRequired[Nullable[str]]
    r"""The carrier of the fulfilment"""
    tracking_urls: NotRequired[Nullable[List[str]]]
    r"""The tracking URLs of the fulfilment"""
    tracking_numbers: NotRequired[Nullable[List[str]]]
    r"""The tracking numbers of the fulfilment"""
    items: NotRequired[Nullable[ItemsModelTypedDict]]
    r"""The items in the fulfilment"""
    order_id: NotRequired[Nullable[str]]
    r"""The UUID of the order associated with the fulfilment"""
    field_mappings: NotRequired[
        Nullable[UnifiedEcommerceFulfillmentOutputFieldMappingsTypedDict]
    ]
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""
    id: NotRequired[Nullable[str]]
    r"""The UUID of the fulfilment"""
    remote_id: NotRequired[Nullable[str]]
    r"""The remote ID of the fulfilment in the context of the 3rd Party"""
    remote_data: NotRequired[
        Nullable[UnifiedEcommerceFulfillmentOutputRemoteDataTypedDict]
    ]
    r"""The remote data of the customer in the context of the 3rd Party"""
    created_at: NotRequired[Nullable[str]]
    r"""The created date of the object"""
    modified_at: NotRequired[Nullable[str]]
    r"""The modified date of the object"""


class UnifiedEcommerceFulfillmentOutput(BaseModel):
    carrier: OptionalNullable[str] = UNSET
    r"""The carrier of the fulfilment"""

    tracking_urls: OptionalNullable[List[str]] = UNSET
    r"""The tracking URLs of the fulfilment"""

    tracking_numbers: OptionalNullable[List[str]] = UNSET
    r"""The tracking numbers of the fulfilment"""

    items: OptionalNullable[ItemsModel] = UNSET
    r"""The items in the fulfilment"""

    order_id: OptionalNullable[str] = UNSET
    r"""The UUID of the order associated with the fulfilment"""

    field_mappings: OptionalNullable[UnifiedEcommerceFulfillmentOutputFieldMappings] = (
        UNSET
    )
    r"""The custom field mappings of the object between the remote 3rd party & Panora"""

    id: OptionalNullable[str] = UNSET
    r"""The UUID of the fulfilment"""

    remote_id: OptionalNullable[str] = UNSET
    r"""The remote ID of the fulfilment in the context of the 3rd Party"""

    remote_data: OptionalNullable[UnifiedEcommerceFulfillmentOutputRemoteData] = UNSET
    r"""The remote data of the customer in the context of the 3rd Party"""

    created_at: OptionalNullable[str] = UNSET
    r"""The created date of the object"""

    modified_at: OptionalNullable[str] = UNSET
    r"""The modified date of the object"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "carrier",
            "tracking_urls",
            "tracking_numbers",
            "items",
            "order_id",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "created_at",
            "modified_at",
        ]
        nullable_fields = [
            "carrier",
            "tracking_urls",
            "tracking_numbers",
            "items",
            "order_id",
            "field_mappings",
            "id",
            "remote_id",
            "remote_data",
            "created_at",
            "modified_at",
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