from .base import BaseModel


class ApiKeyDto(BaseModel):
    def __init__(self, userId: str, projectId: str, keyName: str = None, **kwargs):
        """
        Initialize ApiKeyDto
        Parameters:
        ----------
            userId: str
            projectId: str
            keyName: str
        """
        self.userId = userId
        self.projectId = projectId
        if keyName is not None:
            self.keyName = keyName
