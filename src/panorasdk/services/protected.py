from urllib.parse import quote

from .base import BaseService


class Protected(BaseService):
    def app_controller_get_hello2(self):
        url_endpoint = "/protected"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res
