from urllib.parse import quote

from .base import BaseService
from ..models.CreateUserDto import CreateUserDto as CreateUserDtoModel
from ..models.LoginDto import LoginDto as LoginDtoModel
from ..models.ApiKeyDto import ApiKeyDto as ApiKeyDtoModel


class Auth(BaseService):
    def sign_up(self, request_input: CreateUserDtoModel):
        """
        Register
        """

        url_endpoint = "/auth/register"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def sign_in(self, request_input: LoginDtoModel):
        """
        Log In
        """

        url_endpoint = "/auth/login"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def get_users(self):
        """
        Get users
        """

        url_endpoint = "/auth/users"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def get_api_keys(self):
        """
        Retrieve API Keys
        """

        url_endpoint = "/auth/api-keys"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def generate_api_key(self, request_input: ApiKeyDtoModel):
        """
        Create API Key
        """

        url_endpoint = "/auth/generate-apikey"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res
