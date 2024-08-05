# RetrieveCrmUserRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `x_connection_token`                                        | *str*                                                       | :heavy_check_mark:                                          | The connection token                                        |                                                             |
| `id`                                                        | *str*                                                       | :heavy_check_mark:                                          | id of the user you want to retrieve.                        | b008e199-eda9-4629-bd41-a01b6195864a                        |
| `remote_data`                                               | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Set to true to include data from the original Crm software. | true                                                        |