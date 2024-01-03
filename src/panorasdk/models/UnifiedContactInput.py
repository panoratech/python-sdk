from __future__ import annotations
from .base import BaseModel
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Email import Email
    from .Phone import Phone
FieldMappings = dict


class UnifiedContactInput(BaseModel):
    def __init__(
        self,
        field_mappings: FieldMappings,
        phone_numbers: List[Phone],
        email_addresses: List[Email],
        last_name: str,
        first_name: str,
        **kwargs,
    ):
        """
        Initialize UnifiedContactInput
        Parameters:
        ----------
            field_mappings: FieldMappings
            phone_numbers: list of Phone
            email_addresses: list of Email
            last_name: str
                The last name of the contact
            first_name: str
                The first name of the contact
        """
        self.field_mappings = field_mappings
        self.phone_numbers = phone_numbers
        self.email_addresses = email_addresses
        self.last_name = last_name
        self.first_name = first_name
