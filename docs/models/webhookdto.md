# WebhookDto


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `url`                                  | *str*                                  | :heavy_check_mark:                     | The endpoint url of the webhook.       |
| `description`                          | *str*                                  | :heavy_check_mark:                     | The description of the webhook.        |
| `scope`                                | List[*str*]                            | :heavy_check_mark:                     | The events that the webhook listen to. |