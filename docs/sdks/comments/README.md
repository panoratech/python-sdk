# Comments
(*ticketing.comments*)

### Available Operations

* [list](#list) - List  Comments
* [create](#create) - Create Comments
* [retrieve](#retrieve) - Retrieve Comments

## list

List  Comments

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.ticketing.comments.list(x_connection_token="<value>")

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

**[models.ListTicketingCommentsResponseBody](../../models/listticketingcommentsresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Comments in any supported Ticketing software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.ticketing.comments.create(x_connection_token="<value>", unified_ticketing_comment_input={
    "body": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `x_connection_token`                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The connection token                                                                |
| `unified_ticketing_comment_input`                                                   | [models.UnifiedTicketingCommentInput](../../models/unifiedticketingcommentinput.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `remote_data`                                                                       | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Set to true to include data from the original Ticketing software.                   |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |


### Response

**[models.UnifiedTicketingCommentOutput](../../models/unifiedticketingcommentoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Comments from any connected Ticketing software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.ticketing.comments.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the `comment` you want to retrive.                            |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ticketing software.   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.RetrieveTicketingCommentResponseBody](../../models/retrieveticketingcommentresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
