# Login
(*auth.login*)

## Overview

### Available Operations

* [sign_in](#sign_in) - Log In

## sign_in

Log In

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

s.auth.login.sign_in(request={
    "email": "Oda.Treutel97@hotmail.com",
    "password_hash": "<value>",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LoginDto](../../models/logindto.md)                         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
