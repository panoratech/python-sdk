from .base import BaseModel


class Phone(BaseModel):
    def __init__(
        self, phone_type: str, phone_number: str, owner_type: str = None, **kwargs
    ):
        """
        Initialize Phone
        Parameters:
        ----------
            phone_type: str
                The phone type of a contact
            phone_number: str
                The phone number of a contact
            owner_type: str
        """
        self.phone_type = phone_type
        self.phone_number = phone_number
        if owner_type is not None:
            self.owner_type = owner_type
