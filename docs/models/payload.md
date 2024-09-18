# Payload

The payload event of the webhook.


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `id_event`                             | *Nullable[str]*                        | :heavy_check_mark:                     | The id of the event.                   | 801f9ede-c698-4e66-a7fc-48d19eebaa4f   |
| `type`                                 | *Nullable[str]*                        | :heavy_check_mark:                     | The type of the event.                 | connection.created                     |
| `data`                                 | Dict[str, *Any*]                       | :heavy_check_mark:                     | The data payload event of the webhook. |                                        |