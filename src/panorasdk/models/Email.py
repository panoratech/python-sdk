from .base import BaseModel


class Email(BaseModel):
    def __init__(
        self,
        email_address_type: str,
        email_address: str,
        owner_type: str = None,
        **kwargs,
    ):
        """
        Initialize Email
        Parameters:
        ----------
            email_address_type: str
                The email address type of a contact
            email_address: str
                The email address of a contact
            owner_type: str
        """
        self.email_address_type = email_address_type
        self.email_address = email_address
        if owner_type is not None:
            self.owner_type = owner_type
