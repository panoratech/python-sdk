"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedcrmengagementinput import UnifiedCrmEngagementInput, UnifiedCrmEngagementInputTypedDict
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata, RequestMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateCrmEngagementRequestTypedDict(TypedDict):
    x_connection_token: str
    r"""The connection token"""
    unified_crm_engagement_input: UnifiedCrmEngagementInputTypedDict
    remote_data: NotRequired[bool]
    r"""Set to true to include data from the original Crm software."""
    

class CreateCrmEngagementRequest(BaseModel):
    x_connection_token: Annotated[str, pydantic.Field(alias="x-connection-token"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    r"""The connection token"""
    unified_crm_engagement_input: Annotated[UnifiedCrmEngagementInput, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    remote_data: Annotated[Optional[bool], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Set to true to include data from the original Crm software."""
    
