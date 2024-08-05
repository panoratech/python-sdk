# ProjectResponse


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `id_project`                                 | *str*                                        | :heavy_check_mark:                           | Unique identifier for the project            | 123e4567-e89b-12d3-a456-426614174000         |
| `name`                                       | *str*                                        | :heavy_check_mark:                           | Name of the project                          | My Project                                   |
| `sync_mode`                                  | *str*                                        | :heavy_check_mark:                           | Synchronization mode of the project          | automatic                                    |
| `pull_frequency`                             | *float*                                      | :heavy_check_mark:                           | Frequency of pulling data in seconds         | 3600                                         |
| `redirect_url`                               | *str*                                        | :heavy_check_mark:                           | Redirect URL for the project                 | https://example.com/redirect                 |
| `id_user`                                    | *str*                                        | :heavy_check_mark:                           | User ID associated with the project          | 123e4567-e89b-12d3-a456-426614174001         |
| `id_connector_set`                           | *str*                                        | :heavy_check_mark:                           | Connector set ID associated with the project | 123e4567-e89b-12d3-a456-426614174002         |