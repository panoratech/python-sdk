# SDKTicketingAttachments
(*ticketing.attachments*)

### Available Operations

* [list](#list) - List  Attachments
* [create](#create) - Create Attachments
* [retrieve](#retrieve) - Retrieve Attachments

## list

List  Attachments

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.ticketing.attachments.list(x_connection_token="<value>")

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

**[models.ListTicketingAttachmentsResponseBody](../../models/listticketingattachmentsresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Attachments in any supported Ticketing software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.ticketing.attachments.create(x_connection_token="<value>", unified_ticketing_attachment_input={
    "file_name": "your_file_here",
    "file_url": "<value>",
    "uploader": "<value>",
    "field_mappings": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                      | *str*                                                                                     | :heavy_check_mark:                                                                        | The connection token                                                                      |
| `unified_ticketing_attachment_input`                                                      | [models.UnifiedTicketingAttachmentInput](../../models/unifiedticketingattachmentinput.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `remote_data`                                                                             | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | Set to true to include data from the original Ticketing software.                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |


### Response

**[models.UnifiedTicketingAttachmentOutput](../../models/unifiedticketingattachmentoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Attachments from any connected Ticketing software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.ticketing.attachments.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the attachment you want to retrive.                           |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ticketing software.   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UnifiedTicketingAttachmentOutput](../../models/unifiedticketingattachmentoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
