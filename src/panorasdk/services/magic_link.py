from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.CreateMagicLinkDto import CreateMagicLinkDto as CreateMagicLinkDtoModel


class MagicLink(BaseService):
    def create_magic_link(self, request_input: CreateMagicLinkDtoModel):
        """
        Create a Magic Link
        """

        url_endpoint = "/magic-link/create"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def get_magic_links(self):
        """
        Retrieve Magic Links
        """

        url_endpoint = "/magic-link"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_magic_link(self, id: str):
        """
        Retrieve a Magic Link
        Parameters:
        ----------
            id: str
        """

        url_endpoint = "/magic-link/single"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not id:
            raise ValueError("Parameter id is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "id", id))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res
