# PanoraTicketingAttachments
(*ticketing.attachments*)

### Available Operations

* [list](#list) - List  Attachments
* [create](#create) - Create Attachments
* [retrieve](#retrieve) - Retrieve Attachments

## list

List  Attachments

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.attachments.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListTicketingAttachmentsResponse](../../models/listticketingattachmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Attachments in any supported Ticketing software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.attachments.create(x_connection_token="<value>", unified_ticketing_attachment_input={
    "file_name": "features_planning.pdf",
    "file_url": "https://example.com/features_planning.pdf",
    "uploader": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "ticket_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "comment_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "field_mappings": {
        "fav_dish": "broccoli",
        "fav_color": "red",
    },
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
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.attachments.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the attachment you want to retrive.                           | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ticketing software.   | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UnifiedTicketingAttachmentOutput](../../models/unifiedticketingattachmentoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
