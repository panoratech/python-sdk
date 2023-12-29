from .base import BaseModel

FieldMappings = dict


class UnifiedTicketInput(BaseModel):
    def __init__(self, field_mappings: FieldMappings, **kwargs):
        """
        Initialize UnifiedTicketInput
        Parameters:
        ----------
            field_mappings: FieldMappings
        """
        self.field_mappings = field_mappings
