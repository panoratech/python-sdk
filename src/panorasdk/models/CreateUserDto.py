from .base import BaseModel


class CreateUserDto(BaseModel):
    def __init__(
        self,
        password_hash: str,
        email: str,
        last_name: str,
        first_name: str,
        id_organisation: str = None,
        **kwargs,
    ):
        """
        Initialize CreateUserDto
        Parameters:
        ----------
            password_hash: str
            email: str
            last_name: str
            first_name: str
            id_organisation: str
        """
        self.password_hash = password_hash
        self.email = email
        self.last_name = last_name
        self.first_name = first_name
        if id_organisation is not None:
            self.id_organisation = id_organisation
