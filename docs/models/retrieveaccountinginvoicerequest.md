# RetrieveAccountingInvoiceRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `x_connection_token`                                               | *str*                                                              | :heavy_check_mark:                                                 | The connection token                                               |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | id of the invoice you want to retrieve.                            |
| `remote_data`                                                      | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Set to true to include data from the original Accounting software. |