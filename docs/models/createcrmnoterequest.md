# CreateCrmNoteRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `x_connection_token`                                           | *str*                                                          | :heavy_check_mark:                                             | The connection token                                           |
| `unified_crm_note_input`                                       | [models.UnifiedCrmNoteInput](../models/unifiedcrmnoteinput.md) | :heavy_check_mark:                                             | N/A                                                            |
| `remote_data`                                                  | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Set to true to include data from the original Crm software.    |