from __future__ import annotations
from .base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ContactResponse import ContactResponse


class AddContactsResponse(BaseModel):
    def __init__(
        self,
        statusCode: float,
        message: str = None,
        error: str = None,
        data: ContactResponse = None,
        **kwargs,
    ):
        """
        Initialize AddContactsResponse
        Parameters:
        ----------
            statusCode: float
            message: str
            error: str
            data: ContactResponse
        """
        self.statusCode = statusCode
        if message is not None:
            self.message = message
        if error is not None:
            self.error = error
        if data is not None:
            self.data = data
