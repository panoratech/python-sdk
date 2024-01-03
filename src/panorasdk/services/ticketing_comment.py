from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.UnifiedCommentInput import UnifiedCommentInput as UnifiedCommentInputModel
from ..models.AddCommentsRequest import AddCommentsRequest as AddCommentsRequestModel


class TicketingComment(BaseService):
    def get_comments(
        self, linked_user_id: str, integration_id: str, remote_data: bool = None
    ):
        """
        List a batch of Comments
        Parameters:
        ----------
            integration_id: str
            linked_user_id: str
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/comment"
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

    def add_comment(
        self,
        request_input: UnifiedCommentInputModel,
        linked_user_id: str,
        integration_id: str,
        remote_data: bool = None,
    ):
        """
        Create a Comment
        Parameters:
        ----------
            integration_id: str
                The integration ID
            linked_user_id: str
                The linked user ID
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/comment"
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

    def update_comment(self, id: str):
        """
        Update a Comment
        Parameters:
        ----------
            id: str
        """

        url_endpoint = "/ticketing/comment"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not id:
            raise ValueError("Parameter id is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "id", id))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.patch(final_url, headers, {}, True)
        return res

    def get_comment(self, id: str, remote_data: bool = None):
        """
        Retrieve a Comment
        Parameters:
        ----------
            id: str
                id of the `ticket` you want to retrive.
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/comment/{id}"
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

    def add_comments(
        self,
        request_input: AddCommentsRequestModel,
        linked_user_id: str,
        integration_id: str,
        remote_data: bool = None,
    ):
        """
        Add a batch of Comments
        Parameters:
        ----------
            integration_id: str
            linked_user_id: str
            remote_data: bool
                Set to true to include data from the original Ticketing software.
        """

        url_endpoint = "/ticketing/comment/batch"
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
