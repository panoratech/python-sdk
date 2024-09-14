# Retryid
(*passthrough.retryid*)

## Overview

### Available Operations

* [get_retried_request_response](#get_retried_request_response) - Retrieve response of a failed passthrough request due to rate limits

## get_retried_request_response

Retrieve response of a failed passthrough request due to rate limits

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

s.passthrough.retryid.get_retried_request_response(retry_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `retry_id`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | id of the retryJob returned when you initiated a passthrough request. |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
