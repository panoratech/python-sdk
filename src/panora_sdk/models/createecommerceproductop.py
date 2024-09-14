"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedecommerceproductinput import (
    UnifiedEcommerceProductInput,
    UnifiedEcommerceProductInputTypedDict,
)
from panora_sdk.types import BaseModel
from panora_sdk.utils import (
    FieldMetadata,
    HeaderMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateEcommerceProductRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    unified_ecommerce_product_input: UnifiedEcommerceProductInputTypedDict
    remote_data: NotRequired[bool]
    r"""Set to true to include data from the original Accounting software."""


class CreateEcommerceProductRequest(BaseModel):
    x_connection_token: Annotated[
        str,
        pydantic.Field(alias="x-connection-token"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""The connection token"""

    unified_ecommerce_product_input: Annotated[
        UnifiedEcommerceProductInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    remote_data: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Set to true to include data from the original Accounting software."""