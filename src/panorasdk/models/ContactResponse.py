from .base import BaseModel
from typing import List

RemoteData = dict


class ContactResponse(BaseModel):
    def __init__(self, remote_data: RemoteData, contacts: List[list], **kwargs):
        """
        Initialize ContactResponse
        Parameters:
        ----------
            remote_data: RemoteData
            contacts: list of ContactResponseContacts
        """
        self.remote_data = remote_data
        self.contacts = contacts
