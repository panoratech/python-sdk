from .base import BaseModel


class ApiKeyDto(BaseModel):
    def __init__(self, keyName: str, userId: str, projectId: str, **kwargs):
        """
        Initialize ApiKeyDto
        Parameters:
        ----------
            keyName: str
            userId: str
            projectId: str
        """
        self.keyName = keyName
        self.userId = userId
        self.projectId = projectId
