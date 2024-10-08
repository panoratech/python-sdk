"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Dict, TypedDict
from typing_extensions import NotRequired


class UnifiedCrmDealInputTypedDict(TypedDict):
    name: Nullable[str]
    r"""The name of the deal"""
    description: Nullable[str]
    r"""The description of the deal"""
    amount: Nullable[float]
    r"""The amount of the deal"""
    user_id: NotRequired[Nullable[str]]
    r"""The UUID of the user who is on the deal"""
    stage_id: NotRequired[Nullable[str]]
    r"""The UUID of the stage of the deal"""
    company_id: NotRequired[Nullable[str]]
    r"""The UUID of the company tied to the deal"""
    field_mappings: NotRequired[Nullable[Dict[str, Any]]]
    r"""The custom field mappings of the company between the remote 3rd party & Panora"""
    

class UnifiedCrmDealInput(BaseModel):
    name: Nullable[str]
    r"""The name of the deal"""
    description: Nullable[str]
    r"""The description of the deal"""
    amount: Nullable[float]
    r"""The amount of the deal"""
    user_id: OptionalNullable[str] = UNSET
    r"""The UUID of the user who is on the deal"""
    stage_id: OptionalNullable[str] = UNSET
    r"""The UUID of the stage of the deal"""
    company_id: OptionalNullable[str] = UNSET
    r"""The UUID of the company tied to the deal"""
    field_mappings: OptionalNullable[Dict[str, Any]] = UNSET
    r"""The custom field mappings of the company between the remote 3rd party & Panora"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["user_id", "stage_id", "company_id", "field_mappings"]
        nullable_fields = ["name", "description", "amount", "user_id", "stage_id", "company_id", "field_mappings"]
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
        
