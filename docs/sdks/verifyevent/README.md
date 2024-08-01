# Verifyevent
(*webhooks.verifyevent*)

### Available Operations

* [verify_event](#verify_event) - Verify payload signature of the webhook

## verify_event

Verify payload signature of the webhook

### Example Usage

```python
from panora_sdk import Panora

s = Panora()


res = s.webhooks.verifyevent.verify_event(request={
    "payload": {},
    "signature": "<value>",
    "secret": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.SignatureVerificationDto](../../models/signatureverificationdto.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |


### Response

**[models.EventPayload](../../models/eventpayload.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
