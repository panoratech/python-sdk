# Fromremoteid
(*linked_users.fromremoteid*)

### Available Operations

* [remote_id](#remote_id) - Retrieve a Linked User From A Remote Id

## remote_id

Retrieve a Linked User From A Remote Id

### Example Usage

```python
import os
from panora_sdk import Panora

s = Panora(
    api_key=os.getenv("API_KEY", ""),
)


res = s.linked_users.fromremoteid.remote_id(remote_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `remote_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.LinkedUserResponse](../../models/linkeduserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
