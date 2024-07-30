"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel
from typing import TypedDict


class PayloadTypedDict(TypedDict):
    r"""The payload event of the webhook."""
    
    

class Payload(BaseModel):
    r"""The payload event of the webhook."""
    
    

class SignatureVerificationDtoTypedDict(TypedDict):
    payload: PayloadTypedDict
    r"""The payload event of the webhook."""
    signature: str
    r"""The signature of the webhook."""
    secret: str
    r"""The secret of the webhook."""
    

class SignatureVerificationDto(BaseModel):
    payload: Payload
    r"""The payload event of the webhook."""
    signature: str
    r"""The signature of the webhook."""
    secret: str
    r"""The secret of the webhook."""
    