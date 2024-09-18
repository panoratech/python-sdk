# SignatureVerificationDto


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `payload`                                        | [Nullable[models.Payload]](../models/payload.md) | :heavy_check_mark:                               | The payload event of the webhook.                |
| `signature`                                      | *Nullable[str]*                                  | :heavy_check_mark:                               | The signature of the webhook.                    |
| `secret`                                         | *Nullable[str]*                                  | :heavy_check_mark:                               | The secret of the webhook.                       |