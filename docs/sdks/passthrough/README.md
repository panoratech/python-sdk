# Passthrough
(*passthrough*)

### Available Operations

* [request](#request) - Make a passthrough request

## request

Make a passthrough request

### Example Usage

```python
import panora_sdk
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.passthrough.request(x_connection_token="<value>", pass_through_request_dto={
    "method": panora_sdk.PassThroughRequestDtoMethod.GET,
    "path": "/dev",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `x_connection_token`                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `pass_through_request_dto`                                            | [models.PassThroughRequestDto](../../models/passthroughrequestdto.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.RequestResponse](../../models/requestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
