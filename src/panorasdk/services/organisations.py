from urllib.parse import quote

from .base import BaseService
from ..models.CreateOrganizationDto import (
    CreateOrganizationDto as CreateOrganizationDtoModel,
)


class Organisations(BaseService):
    def get_organisations(self):
        url_endpoint = "/organisations"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def create_organisation(self, request_input: CreateOrganizationDtoModel):
        url_endpoint = "/organisations/create"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res
