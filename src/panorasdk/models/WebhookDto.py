from .base import BaseModel
from typing import List


class WebhookDto(BaseModel):
    def __init__(
        self,
        scope: List[str],
        id_project: str,
        url: str,
        description: str = None,
        **kwargs,
    ):
        """
        Initialize WebhookDto
        Parameters:
        ----------
            scope: list of WebhookDtoScope
            id_project: str
            url: str
            description: str
        """
        self.scope = scope
        self.id_project = id_project
        self.url = url
        if description is not None:
            self.description = description
