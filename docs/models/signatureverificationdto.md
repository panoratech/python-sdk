# SignatureVerificationDto


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `payload`                              | [models.Payload](../models/payload.md) | :heavy_check_mark:                     | The payload event of the webhook.      |
| `signature`                            | *str*                                  | :heavy_check_mark:                     | The signature of the webhook.          |
| `secret`                               | *str*                                  | :heavy_check_mark:                     | The secret of the webhook.             |