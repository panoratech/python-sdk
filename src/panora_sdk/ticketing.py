"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from panora_sdk.accounts import Accounts
from panora_sdk.collections import Collections
from panora_sdk.comments import Comments
from panora_sdk.contacts import Contacts
from panora_sdk.panora_ticketing_attachments import PanoraTicketingAttachments
from panora_sdk.tags import Tags
from panora_sdk.teams import Teams
from panora_sdk.tickets import Tickets
from panora_sdk.users import Users

class Ticketing(BaseSDK):
    tickets: Tickets
    users: Users
    accounts: Accounts
    contacts: Contacts
    collections: Collections
    comments: Comments
    tags: Tags
    teams: Teams
    attachments: PanoraTicketingAttachments
    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.tickets = Tickets(self.sdk_configuration)
        self.users = Users(self.sdk_configuration)
        self.accounts = Accounts(self.sdk_configuration)
        self.contacts = Contacts(self.sdk_configuration)
        self.collections = Collections(self.sdk_configuration)
        self.comments = Comments(self.sdk_configuration)
        self.tags = Tags(self.sdk_configuration)
        self.teams = Teams(self.sdk_configuration)
        self.attachments = PanoraTicketingAttachments(self.sdk_configuration)
    