# Passthrough
(*passthrough*)

### Available Operations

* [request](#request) - Make a passthrough request

## request

Make a passthrough request

### Example Usage

```python
import os
import panora
from panora import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


res = s.passthrough.request(integration_id="<value>", linked_user_id="<value>", vertical="<value>", pass_through_request_dto={
    "method": panora.Method.GET,
    "path": "/dev",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `integration_id`                                                      | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `linked_user_id`                                                      | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `vertical`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `pass_through_request_dto`                                            | [models.PassThroughRequestDto](../../models/passthroughrequestdto.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.PassThroughResponse](../../models/passthroughresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
