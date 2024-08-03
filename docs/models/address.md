# Address


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `street_1`                                                       | *Nullable[str]*                                                  | :heavy_check_mark:                                               | The street                                                       |
| `street_2`                                                       | *Nullable[str]*                                                  | :heavy_check_mark:                                               | More information about the street                                |
| `city`                                                           | *Nullable[str]*                                                  | :heavy_check_mark:                                               | The city                                                         |
| `state`                                                          | *Nullable[str]*                                                  | :heavy_check_mark:                                               | The state                                                        |
| `postal_code`                                                    | *Nullable[str]*                                                  | :heavy_check_mark:                                               | The postal code                                                  |
| `country`                                                        | *Nullable[str]*                                                  | :heavy_check_mark:                                               | The country                                                      |
| `address_type`                                                   | *Nullable[str]*                                                  | :heavy_check_mark:                                               | The address type. Authorized values are either PERSONAL or WORK. |
| `owner_type`                                                     | *Nullable[str]*                                                  | :heavy_check_mark:                                               | The owner type of the address                                    |