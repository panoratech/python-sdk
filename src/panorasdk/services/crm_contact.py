from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetContactsResponse import GetContactsResponse as GetContactsResponseModel
from ..models.UnifiedContactInput import UnifiedContactInput as UnifiedContactInputModel
from ..models.AddContactResponse import AddContactResponse as AddContactResponseModel
from ..models.GetContactResponse import GetContactResponse as GetContactResponseModel
from ..models.AddContactsRequest import AddContactsRequest as AddContactsRequestModel
from ..models.AddContactsResponse import AddContactsResponse as AddContactsResponseModel


class CrmContact(BaseService):
    def get_contacts(
        self, linked_user_id: str, integration_id: str, remote_data: bool = None
    ) -> GetContactsResponseModel:
        url_endpoint = "/crm/contact"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not integration_id:
            raise ValueError(
                "Parameter integration_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "integrationId", integration_id
            )
        )
        if not linked_user_id:
            raise ValueError(
                "Parameter linked_user_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "linkedUserId", linked_user_id
            )
        )
        if remote_data:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "remote_data", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetContactsResponseModel(**res)
        return res

    def add_contact(
        self,
        request_input: UnifiedContactInputModel,
        linked_user_id: str,
        integration_id: str,
        remote_data: bool = None,
    ) -> AddContactResponseModel:
        """
        Create CRM Contact
        Parameters:
        ----------
            integration_id: str
            linked_user_id: str
            remote_data: bool
        """

        url_endpoint = "/crm/contact"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not integration_id:
            raise ValueError(
                "Parameter integration_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "integrationId", integration_id
            )
        )
        if not linked_user_id:
            raise ValueError(
                "Parameter linked_user_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "linkedUserId", linked_user_id
            )
        )
        if remote_data:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "remote_data", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return AddContactResponseModel(**res)
        return res

    def update_contact(self, id: str):
        url_endpoint = "/crm/contact"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not id:
            raise ValueError("Parameter id is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "id", id))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.patch(final_url, headers, {}, True)
        return res

    def get_contact(self, id: str, remote_data: bool = None) -> GetContactResponseModel:
        """
        Retrive a CRM Contact
        Parameters:
        ----------
            id: str
            remote_data: bool
        """

        url_endpoint = "/crm/contact/{id}"
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
                    "form", False, "remote_data", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetContactResponseModel(**res)
        return res

    def add_contacts(
        self,
        request_input: AddContactsRequestModel,
        linked_user_id: str,
        integration_id: str,
        remote_data: bool = None,
    ) -> AddContactsResponseModel:
        url_endpoint = "/crm/contact/batch"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not integration_id:
            raise ValueError(
                "Parameter integration_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "integrationId", integration_id
            )
        )
        if not linked_user_id:
            raise ValueError(
                "Parameter linked_user_id is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "linkedUserId", linked_user_id
            )
        )
        if remote_data:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "remote_data", remote_data
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return AddContactsResponseModel(**res)
        return res
