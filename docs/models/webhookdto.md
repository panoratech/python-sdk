# WebhookDto


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `url`                                  | *Nullable[str]*                        | :heavy_check_mark:                     | The endpoint url of the webhook.       | https://acme.com/webhook_receiver      |
| `description`                          | *Nullable[str]*                        | :heavy_check_mark:                     | The description of the webhook.        | Webhook to receive connection events   |
| `scope`                                | List[*str*]                            | :heavy_check_mark:                     | The events that the webhook listen to. | [<br/>"connection.created"<br/>]       |