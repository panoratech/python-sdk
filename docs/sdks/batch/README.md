# Batch
(*linked_users.batch*)

### Available Operations

* [import_batch](#import_batch) - Add Batch Linked Users

## import_batch

Add Batch Linked Users

### Example Usage

```python
import os
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.linked_users.batch.import_batch(request={
    "linked_user_origin_ids": [
        "<value>",
    ],
    "alias": "<value>",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateBatchLinkedUserDto](../../models/createbatchlinkeduserdto.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
