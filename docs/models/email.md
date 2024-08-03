# Email


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `email_address`                                                        | *Nullable[str]*                                                        | :heavy_check_mark:                                                     | The email address                                                      |
| `email_address_type`                                                   | *Nullable[str]*                                                        | :heavy_check_mark:                                                     | The email address type. Authorized values are either PERSONAL or WORK. |
| `owner_type`                                                           | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The owner type of an email                                             |