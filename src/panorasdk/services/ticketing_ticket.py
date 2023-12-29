from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.UnifiedTicketInput import UnifiedTicketInput as UnifiedTicketInputModel
from ..models.AddTicketsRequest import AddTicketsRequest as AddTicketsRequestModel


class TicketingTicket(BaseService):
    def get_tickets(
        self, linked_user_id: str, integration_id: str, remote_data: bool = None
    ):
        """
        List a batch of Tickets
        Parameters:
        ----------
            integration_id: str
            linked_user_id: str
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/ticket"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not integration_id:
            raise ValueError(
                "Parameter integration_id is required, cannot be empty or blank."
            )
        headers["integrationId"] = query_serializer.serialize_header(
            False, integration_id
        )
        if not linked_user_id:
            raise ValueError(
                "Parameter linked_user_id is required, cannot be empty or blank."
            )
        headers["linkedUserId"] = query_serializer.serialize_header(
            False, linked_user_id
        )
        if remote_data:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "remoteData", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def add_ticket(
        self,
        request_input: UnifiedTicketInputModel,
        linked_user_id: str,
        integration_id: str,
        remote_data: bool = None,
    ):
        """
        Create a Ticket
        Parameters:
        ----------
            integration_id: str
                The integration ID
            linked_user_id: str
                The linked user ID
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/ticket"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not integration_id:
            raise ValueError(
                "Parameter integration_id is required, cannot be empty or blank."
            )
        headers["integrationId"] = query_serializer.serialize_header(
            False, integration_id
        )
        if not linked_user_id:
            raise ValueError(
                "Parameter linked_user_id is required, cannot be empty or blank."
            )
        headers["linkedUserId"] = query_serializer.serialize_header(
            False, linked_user_id
        )
        if remote_data:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "remoteData", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def update_ticket(self, id: str):
        """
        Update a Ticket
        Parameters:
        ----------
            id: str
        """

        url_endpoint = "/ticketing/ticket"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not id:
            raise ValueError("Parameter id is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "id", id))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.patch(final_url, headers, {}, True)
        return res

    def get_ticket(self, id: str, remote_data: bool = None):
        """
        Retrieve a Ticket
        Parameters:
        ----------
            id: str
                id of the `ticket` you want to retrive.
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/ticket/{id}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not id:
            raise ValueError("Parameter id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{id}",
            quote(str(query_serializer.serialize_path("simple", False, id, None))),
        )
        if remote_data:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "remoteData", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def add_tickets(
        self,
        request_input: AddTicketsRequestModel,
        linked_user_id: str,
        integration_id: str,
        remote_data: bool = None,
    ):
        """
        Add a batch of Tickets
        Parameters:
        ----------
            integration_id: str
            linked_user_id: str
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/ticket/batch"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not integration_id:
            raise ValueError(
                "Parameter integration_id is required, cannot be empty or blank."
            )
        headers["integrationId"] = query_serializer.serialize_header(
            False, integration_id
        )
        if not linked_user_id:
            raise ValueError(
                "Parameter linked_user_id is required, cannot be empty or blank."
            )
        headers["linkedUserId"] = query_serializer.serialize_header(
            False, linked_user_id
        )
        if remote_data:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "remoteData", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        return res
