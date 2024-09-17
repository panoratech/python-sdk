"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class DeductionItemTypedDict(TypedDict):
    name: NotRequired[Nullable[str]]
    r"""The name of the deduction"""
    employee_deduction: NotRequired[Nullable[float]]
    r"""The amount of employee deduction"""
    company_deduction: NotRequired[Nullable[float]]
    r"""The amount of company deduction"""
    

class DeductionItem(BaseModel):
    name: OptionalNullable[str] = UNSET
    r"""The name of the deduction"""
    employee_deduction: OptionalNullable[float] = UNSET
    r"""The amount of employee deduction"""
    company_deduction: OptionalNullable[float] = UNSET
    r"""The amount of company deduction"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "employee_deduction", "company_deduction"]
        nullable_fields = ["name", "employee_deduction", "company_deduction"]
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
        
