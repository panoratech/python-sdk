from urllib.parse import quote

from .base import BaseService


class Events(BaseService):
    def get_events(self):
        """
        Retrieve Events
        """

        url_endpoint = "/events"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res
