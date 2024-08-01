# Define
(*field_mappings.define*)

### Available Operations

* [definitions](#definitions) - Define target Field

## definitions

Define target Field

### Example Usage

```python
from panora_sdk import Panora

s = Panora()


s.field_mappings.define.definitions(request={
    "object_type_owner": "<value>",
    "name": "<value>",
    "description": "Universal heuristic matrices",
    "data_type": "decimal",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DefineTargetFieldDto](../../models/definetargetfielddto.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
