"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel
from typing import TypedDict


class ProjectResponseTypedDict(TypedDict):
    id_project: str
    r"""Unique identifier for the project"""
    name: str
    r"""Name of the project"""
    sync_mode: str
    r"""Synchronization mode of the project"""
    pull_frequency: float
    r"""Frequency of pulling data in seconds"""
    redirect_url: str
    r"""Redirect URL for the project"""
    id_user: str
    r"""User ID associated with the project"""
    id_connector_set: str
    r"""Connector set ID associated with the project"""
    

class ProjectResponse(BaseModel):
    id_project: str
    r"""Unique identifier for the project"""
    name: str
    r"""Name of the project"""
    sync_mode: str
    r"""Synchronization mode of the project"""
    pull_frequency: float
    r"""Frequency of pulling data in seconds"""
    redirect_url: str
    r"""Redirect URL for the project"""
    id_user: str
    r"""User ID associated with the project"""
    id_connector_set: str
    r"""Connector set ID associated with the project"""
    
