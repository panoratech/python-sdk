from .base import BaseModel


class DefineTargetFieldDto(BaseModel):
    def __init__(
        self,
        data_type: str,
        description: str,
        name: str,
        object_type_owner: str,
        **kwargs,
    ):
        """
        Initialize DefineTargetFieldDto
        Parameters:
        ----------
            data_type: str
            description: str
            name: str
            object_type_owner: str
        """
        self.data_type = data_type
        self.description = description
        self.name = name
        self.object_type_owner = object_type_owner
