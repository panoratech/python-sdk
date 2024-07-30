"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from panora_sdk.drives import Drives
from panora_sdk.files import Files
from panora_sdk.folders import Folders
from panora_sdk.panora_filestorage_users import PanoraFilestorageUsers
from panora_sdk.panora_groups import PanoraGroups

class Filestorage(BaseSDK):
    drives: Drives
    files: Files
    folders: Folders
    groups: PanoraGroups
    users: PanoraFilestorageUsers
    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.drives = Drives(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.folders = Folders(self.sdk_configuration)
        self.groups = PanoraGroups(self.sdk_configuration)
        self.users = PanoraFilestorageUsers(self.sdk_configuration)
    