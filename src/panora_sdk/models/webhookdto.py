"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel
from typing import List, TypedDict


class WebhookDtoTypedDict(TypedDict):
    url: str
    r"""The endpoint url of the webhook."""
    description: str
    r"""The description of the webhook."""
    scope: List[str]
    r"""The events that the webhook listen to."""
    

class WebhookDto(BaseModel):
    url: str
    r"""The endpoint url of the webhook."""
    description: str
    r"""The description of the webhook."""
    scope: List[str]
    r"""The events that the webhook listen to."""
    