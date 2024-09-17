"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel
from panora_sdk.utils import FieldMetadata, HeaderMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RetrieveAccountingTrackingCategoryRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    id: str
    r"""id of the trackingcategory you want to retrieve."""
    remote_data: NotRequired[bool]
    r"""Set to true to include data from the original Accounting software."""
    

class RetrieveAccountingTrackingCategoryRequest(BaseModel):
    x_connection_token: Annotated[str, pydantic.Field(alias="x-connection-token"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    r"""The connection token"""
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""id of the trackingcategory you want to retrieve."""
    remote_data: Annotated[Optional[bool], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Set to true to include data from the original Accounting software."""
    
