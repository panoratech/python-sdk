"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from panora import models
from panora._hooks import HookContext
from panora.types import BaseModel, OptionalNullable, UNSET
import panora.utils as utils
from typing import Optional, Union

class Passthrough(BaseSDK):
    
    
    def request(
        self, *,
        integration_id: str,
        linked_user_id: str,
        vertical: str,
        pass_through_request_dto: Union[models.PassThroughRequestDto, models.PassThroughRequestDtoTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.PassThroughResponse]:
        r"""Make a passthrough request

        :param integration_id: 
        :param linked_user_id: 
        :param vertical: 
        :param pass_through_request_dto: 
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
        
        request = models.RequestRequest(
            integration_id=integration_id,
            linked_user_id=linked_user_id,
            vertical=vertical,
            pass_through_request_dto=utils.unmarshal(pass_through_request_dto, models.PassThroughRequestDto) if not isinstance(pass_through_request_dto, BaseModel) else pass_through_request_dto,
        )
        
        req = self.build_request(
            method="POST",
            path="/passthrough",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.pass_through_request_dto, False, False, "json", models.PassThroughRequestDto),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="request", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.PassThroughResponse])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def request_async(
        self, *,
        integration_id: str,
        linked_user_id: str,
        vertical: str,
        pass_through_request_dto: Union[models.PassThroughRequestDto, models.PassThroughRequestDtoTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.PassThroughResponse]:
        r"""Make a passthrough request

        :param integration_id: 
        :param linked_user_id: 
        :param vertical: 
        :param pass_through_request_dto: 
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
        
        request = models.RequestRequest(
            integration_id=integration_id,
            linked_user_id=linked_user_id,
            vertical=vertical,
            pass_through_request_dto=utils.unmarshal(pass_through_request_dto, models.PassThroughRequestDto) if not isinstance(pass_through_request_dto, BaseModel) else pass_through_request_dto,
        )
        
        req = self.build_request(
            method="POST",
            path="/passthrough",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.pass_through_request_dto, False, False, "json", models.PassThroughRequestDto),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="request", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.PassThroughResponse])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
