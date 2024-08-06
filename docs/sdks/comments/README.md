# Comments
(*ticketing.comments*)

### Available Operations

* [list](#list) - List Comments
* [create](#create) - Create Comments
* [retrieve](#retrieve) - Retrieve Comment

## list

List Comments

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.comments.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original software.             | true                                                                |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Set to get the number of records.                                   | 10                                                                  |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Set to get the number of records after this cursor.                 | 1b8b05bb-5273-4012-b520-8657b0b90874                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.ListTicketingCommentsResponse](../../models/listticketingcommentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Comments in any supported Ticketing software

### Example Usage

```python
import panora_sdk
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.comments.create(x_connection_token="<value>", unified_ticketing_comment_input={
    "body": "Assigned to Eric !",
    "html_body": "<p>Assigned to Eric !</p>",
    "is_private": False,
    "creator_type": panora_sdk.UnifiedTicketingCommentInputCreatorType.USER,
    "ticket_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "contact_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "user_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "attachments": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
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

Retrieve a Comment from any connected Ticketing software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
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
