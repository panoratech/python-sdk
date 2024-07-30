"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import TypedDict


class PassThroughResponseDataTypedDict(TypedDict):
    pass
    

class PassThroughResponseData(BaseModel):
    pass
    

class PassThroughResponseTypedDict(TypedDict):
    url: str
    status: float
    data: PassThroughResponseDataTypedDict
    

class PassThroughResponse(BaseModel):
    url: str
    status: float
    data: PassThroughResponseData
    
