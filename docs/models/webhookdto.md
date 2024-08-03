# WebhookDto


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `url`                                  | *Nullable[str]*                        | :heavy_check_mark:                     | The endpoint url of the webhook.       |
| `scope`                                | List[*str*]                            | :heavy_check_mark:                     | The events that the webhook listen to. |
| `description`                          | *OptionalNullable[str]*                | :heavy_minus_sign:                     | The description of the webhook.        |