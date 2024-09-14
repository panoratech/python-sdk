"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from jsonpath import JSONPath
from panora_sdk import models, utils
from panora_sdk._hooks import HookContext
from panora_sdk.types import OptionalNullable, UNSET
from typing import Any, Dict, Optional


class Contacts(BaseSDK):
    def list(
        self,
        *,
        x_connection_token: str,
        remote_data: Optional[bool] = None,
        limit: Optional[float] = 50,
        cursor: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ListTicketingContactsResponse]:
        r"""List Contacts

        :param x_connection_token: The connection token
        :param remote_data: Set to true to include data from the original software.
        :param limit: Set to get the number of records.
        :param cursor: Set to get the number of records after this cursor.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListTicketingContactsRequest(
            x_connection_token=x_connection_token,
            remote_data=remote_data,
            limit=limit,
            cursor=cursor,
        )

        req = self.build_request(
            method="GET",
            path="/ticketing/contacts",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="listTicketingContacts",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.ListTicketingContactsResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            next_cursor = JSONPath("$.next_cursor").parse(body)

            if len(next_cursor) == 0:
                return None
            next_cursor = next_cursor[0]

            return self.list(
                x_connection_token=x_connection_token,
                remote_data=remote_data,
                limit=limit,
                cursor=next_cursor,
                retries=retries,
            )

        if utils.match_response(http_res, "200", "application/json"):
            return models.ListTicketingContactsResponse(
                result=utils.unmarshal_json(
                    http_res.text, Optional[models.ListTicketingContactsResponseBody]
                ),
                next=next_func,
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def list_async(
        self,
        *,
        x_connection_token: str,
        remote_data: Optional[bool] = None,
        limit: Optional[float] = 50,
        cursor: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ListTicketingContactsResponse]:
        r"""List Contacts

        :param x_connection_token: The connection token
        :param remote_data: Set to true to include data from the original software.
        :param limit: Set to get the number of records.
        :param cursor: Set to get the number of records after this cursor.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListTicketingContactsRequest(
            x_connection_token=x_connection_token,
            remote_data=remote_data,
            limit=limit,
            cursor=cursor,
        )

        req = self.build_request_async(
            method="GET",
            path="/ticketing/contacts",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="listTicketingContacts",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.ListTicketingContactsResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            next_cursor = JSONPath("$.next_cursor").parse(body)

            if len(next_cursor) == 0:
                return None
            next_cursor = next_cursor[0]

            return self.list(
                x_connection_token=x_connection_token,
                remote_data=remote_data,
                limit=limit,
                cursor=next_cursor,
                retries=retries,
            )

        if utils.match_response(http_res, "200", "application/json"):
            return models.ListTicketingContactsResponse(
                result=utils.unmarshal_json(
                    http_res.text, Optional[models.ListTicketingContactsResponseBody]
                ),
                next=next_func,
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def retrieve(
        self,
        *,
        x_connection_token: str,
        id: str,
        remote_data: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.RetrieveTicketingContactResponseBody]:
        r"""Retrieve Contact

        Retrieve a Contact from any connected Ticketing software

        :param x_connection_token: The connection token
        :param id: id of the contact you want to retrieve.
        :param remote_data: Set to true to include data from the original Ticketing software.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.RetrieveTicketingContactRequest(
            x_connection_token=x_connection_token,
            id=id,
            remote_data=remote_data,
        )

        req = self.build_request(
            method="GET",
            path="/ticketing/contacts/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="retrieveTicketingContact",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[models.RetrieveTicketingContactResponseBody]
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def retrieve_async(
        self,
        *,
        x_connection_token: str,
        id: str,
        remote_data: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.RetrieveTicketingContactResponseBody]:
        r"""Retrieve Contact

        Retrieve a Contact from any connected Ticketing software

        :param x_connection_token: The connection token
        :param id: id of the contact you want to retrieve.
        :param remote_data: Set to true to include data from the original Ticketing software.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.RetrieveTicketingContactRequest(
            x_connection_token=x_connection_token,
            id=id,
            remote_data=remote_data,
        )

        req = self.build_request_async(
            method="GET",
            path="/ticketing/contacts/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="retrieveTicketingContact",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[models.RetrieveTicketingContactResponseBody]
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )
