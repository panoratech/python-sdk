# Single
(*linked_users.single*)

### Available Operations

* [retrieve](#retrieve) - Retrieve Linked Users

## retrieve

Retrieve Linked Users

### Example Usage

```python
import os
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.linked_users.single.retrieve(id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
