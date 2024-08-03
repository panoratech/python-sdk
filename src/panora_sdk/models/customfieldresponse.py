"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from panora_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict


class CustomFieldResponseTypedDict(TypedDict):
    id_attribute: Nullable[str]
    r"""Attribute Id"""
    status: Nullable[str]
    r"""Attribute Status"""
    ressource_owner_type: Nullable[str]
    r"""Attribute Ressource Owner Type"""
    slug: Nullable[str]
    r"""Attribute Slug"""
    description: Nullable[str]
    r"""Attribute Description"""
    data_type: Nullable[str]
    r"""Attribute Data Type"""
    remote_id: Nullable[str]
    r"""Attribute Remote Id"""
    source: Nullable[str]
    r"""Attribute Source"""
    id_entity: Nullable[str]
    r"""Attribute Id Entity"""
    id_project: Nullable[str]
    r"""Attribute Id Project"""
    scope: Nullable[str]
    r"""Attribute Scope"""
    id_consumer: Nullable[str]
    r"""Attribute Id Consumer"""
    created_at: Nullable[datetime]
    r"""Attribute Created Date"""
    modified_at: Nullable[datetime]
    r"""Attribute Modified Date"""
    

class CustomFieldResponse(BaseModel):
    id_attribute: Nullable[str]
    r"""Attribute Id"""
    status: Nullable[str]
    r"""Attribute Status"""
    ressource_owner_type: Nullable[str]
    r"""Attribute Ressource Owner Type"""
    slug: Nullable[str]
    r"""Attribute Slug"""
    description: Nullable[str]
    r"""Attribute Description"""
    data_type: Nullable[str]
    r"""Attribute Data Type"""
    remote_id: Nullable[str]
    r"""Attribute Remote Id"""
    source: Nullable[str]
    r"""Attribute Source"""
    id_entity: Nullable[str]
    r"""Attribute Id Entity"""
    id_project: Nullable[str]
    r"""Attribute Id Project"""
    scope: Nullable[str]
    r"""Attribute Scope"""
    id_consumer: Nullable[str]
    r"""Attribute Id Consumer"""
    created_at: Nullable[datetime]
    r"""Attribute Created Date"""
    modified_at: Nullable[datetime]
    r"""Attribute Modified Date"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["id_attribute", "status", "ressource_owner_type", "slug", "description", "data_type", "remote_id", "source", "id_entity", "id_project", "scope", "id_consumer", "created_at", "modified_at"]
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
        