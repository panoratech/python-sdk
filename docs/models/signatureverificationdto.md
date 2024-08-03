# SignatureVerificationDto


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `payload`                         | Dict[str, *Any*]                  | :heavy_check_mark:                | The payload event of the webhook. |
| `signature`                       | *Nullable[str]*                   | :heavy_check_mark:                | The signature of the webhook.     |
| `secret`                          | *Nullable[str]*                   | :heavy_check_mark:                | The secret of the webhook.        |