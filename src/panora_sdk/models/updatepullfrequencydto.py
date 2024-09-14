"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import BaseModel
from typing import TypedDict


class UpdatePullFrequencyDtoTypedDict(TypedDict):
    crm: float
    r"""Frequency in seconds"""
    ats: float
    r"""Frequency in seconds"""
    hris: float
    r"""Frequency in seconds"""
    accounting: float
    r"""Frequency in seconds"""
    filestorage: float
    r"""Frequency in seconds"""
    ecommerce: float
    r"""Frequency in seconds"""
    ticketing: float
    r"""Frequency in seconds"""


class UpdatePullFrequencyDto(BaseModel):
    crm: float
    r"""Frequency in seconds"""

    ats: float
    r"""Frequency in seconds"""

    hris: float
    r"""Frequency in seconds"""

    accounting: float
    r"""Frequency in seconds"""

    filestorage: float
    r"""Frequency in seconds"""

    ecommerce: float
    r"""Frequency in seconds"""

    ticketing: float
    r"""Frequency in seconds"""