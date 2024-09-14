"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class WebhookDtoTypedDict(TypedDict):
    url: Nullable[str]
    r"""The endpoint url of the webhook."""
    scope: Nullable[List[str]]
    r"""The events that the webhook listen to."""
    description: NotRequired[Nullable[str]]
    r"""The description of the webhook."""


class WebhookDto(BaseModel):
    url: Nullable[str]
    r"""The endpoint url of the webhook."""

    scope: Nullable[List[str]]
    r"""The events that the webhook listen to."""

    description: OptionalNullable[str] = UNSET
    r"""The description of the webhook."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description"]
        nullable_fields = ["url", "scope", "description"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
