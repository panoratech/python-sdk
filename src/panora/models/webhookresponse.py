"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora.types import BaseModel
from typing import List, TypedDict


class WebhookResponseTypedDict(TypedDict):
    id_webhook_endpoint: str
    r"""The unique UUID of the webhook."""
    endpoint_description: str
    r"""The description of the webhook."""
    url: str
    r"""The endpoint url of the webhook."""
    secret: str
    r"""The secret of the webhook."""
    active: bool
    r"""The status of the webhook."""
    created_at: datetime
    r"""The created date  of the webhook."""
    scope: List[str]
    r"""The events that the webhook listen to."""
    id_project: str
    r"""The project id tied to the webhook."""
    last_update: datetime
    r"""The last update date of the webhook."""
    

class WebhookResponse(BaseModel):
    id_webhook_endpoint: str
    r"""The unique UUID of the webhook."""
    endpoint_description: str
    r"""The description of the webhook."""
    url: str
    r"""The endpoint url of the webhook."""
    secret: str
    r"""The secret of the webhook."""
    active: bool
    r"""The status of the webhook."""
    created_at: datetime
    r"""The created date  of the webhook."""
    scope: List[str]
    r"""The events that the webhook listen to."""
    id_project: str
    r"""The project id tied to the webhook."""
    last_update: datetime
    r"""The last update date of the webhook."""
    
