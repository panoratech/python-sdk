"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from panora.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class UnifiedTicketingAccountOutputFieldMappingsTypedDict(TypedDict):
    pass
    

class UnifiedTicketingAccountOutputFieldMappings(BaseModel):
    pass
    

class UnifiedTicketingAccountOutputRemoteDataTypedDict(TypedDict):
    pass
    

class UnifiedTicketingAccountOutputRemoteData(BaseModel):
    pass
    

class UnifiedTicketingAccountOutputCreatedAtTypedDict(TypedDict):
    pass
    

class UnifiedTicketingAccountOutputCreatedAt(BaseModel):
    pass
    

class UnifiedTicketingAccountOutputModifiedAtTypedDict(TypedDict):
    pass
    

class UnifiedTicketingAccountOutputModifiedAt(BaseModel):
    pass
    

class UnifiedTicketingAccountOutputTypedDict(TypedDict):
    name: str
    r"""The name of the account"""
    field_mappings: UnifiedTicketingAccountOutputFieldMappingsTypedDict
    remote_data: UnifiedTicketingAccountOutputRemoteDataTypedDict
    created_at: UnifiedTicketingAccountOutputCreatedAtTypedDict
    modified_at: UnifiedTicketingAccountOutputModifiedAtTypedDict
    domains: NotRequired[List[str]]
    r"""The domains of the account"""
    id: NotRequired[str]
    r"""The UUID of the account"""
    remote_id: NotRequired[str]
    r"""The id of the account in the context of the 3rd Party"""
    

class UnifiedTicketingAccountOutput(BaseModel):
    name: str
    r"""The name of the account"""
    field_mappings: UnifiedTicketingAccountOutputFieldMappings
    remote_data: UnifiedTicketingAccountOutputRemoteData
    created_at: UnifiedTicketingAccountOutputCreatedAt
    modified_at: UnifiedTicketingAccountOutputModifiedAt
    domains: Optional[List[str]] = None
    r"""The domains of the account"""
    id: Optional[str] = None
    r"""The UUID of the account"""
    remote_id: Optional[str] = None
    r"""The id of the account in the context of the 3rd Party"""
    
