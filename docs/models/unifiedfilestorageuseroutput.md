# UnifiedFilestorageUserOutput


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `name`                                                                        | *Nullable[str]*                                                               | :heavy_check_mark:                                                            | The name of the user                                                          | Joe Doe                                                                       |
| `email`                                                                       | *Nullable[str]*                                                               | :heavy_check_mark:                                                            | The email of the user                                                         | joe.doe@gmail.com                                                             |
| `is_me`                                                                       | *Nullable[bool]*                                                              | :heavy_check_mark:                                                            | Whether the user is the one who linked this account.                          | true                                                                          |
| `field_mappings`                                                              | Dict[str, *Any*]                                                              | :heavy_minus_sign:                                                            | The custom field mappings of the object between the remote 3rd party & Panora | {<br/>"fav_dish": "broccoli",<br/>"fav_color": "red"<br/>}                    |
| `id`                                                                          | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | The UUID of the user                                                          | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                          |
| `remote_id`                                                                   | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | The id of the user in the context of the 3rd Party                            | id_1                                                                          |
| `remote_data`                                                                 | Dict[str, *Any*]                                                              | :heavy_minus_sign:                                                            | The remote data of the user in the context of the 3rd Party                   | {<br/>"fav_dish": "broccoli",<br/>"fav_color": "red"<br/>}                    |
| `created_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_minus_sign:                                                            | The created date of the object                                                | 2024-10-01T12:00:00Z                                                          |
| `modified_at`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_minus_sign:                                                            | The modified date of the object                                               | 2024-10-01T12:00:00Z                                                          |