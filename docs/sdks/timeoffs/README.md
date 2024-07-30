# Timeoffs
(*hris.timeoffs*)

### Available Operations

* [list](#list) - List  Timeoffs
* [create](#create) - Create Timeoffs
* [retrieve](#retrieve) - Retrieve Timeoffs

## list

List  Timeoffs

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.hris.timeoffs.list(x_connection_token="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original software.             |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Set to get the number of records.                                   |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Set to get the number of records after this cursor.                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.ListHrisTimeoffsResponseBody](../../models/listhristimeoffsresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Timeoffs in any supported Hris software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.hris.timeoffs.create(x_connection_token="<value>", unified_hris_timeoff_input={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `x_connection_token`                                                      | *str*                                                                     | :heavy_check_mark:                                                        | The connection token                                                      |
| `unified_hris_timeoff_input`                                              | [models.UnifiedHrisTimeoffInput](../../models/unifiedhristimeoffinput.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `remote_data`                                                             | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Set to true to include data from the original Hris software.              |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |


### Response

**[models.UnifiedHrisTimeoffOutput](../../models/unifiedhristimeoffoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Timeoffs from any connected Hris software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.hris.timeoffs.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the timeoff you want to retrieve.                             |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Hris software.        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UnifiedHrisTimeoffOutput](../../models/unifiedhristimeoffoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
