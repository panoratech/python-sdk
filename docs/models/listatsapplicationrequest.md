# ListAtsApplicationRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `x_connection_token`                                    | *str*                                                   | :heavy_check_mark:                                      | The connection token                                    |                                                         |
| `remote_data`                                           | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Set to true to include data from the original software. | true                                                    |
| `limit`                                                 | *Optional[float]*                                       | :heavy_minus_sign:                                      | Set to get the number of records.                       | 10                                                      |
| `cursor`                                                | *Optional[str]*                                         | :heavy_minus_sign:                                      | Set to get the number of records after this cursor.     | 1b8b05bb-5273-4012-b520-8657b0b90874                    |