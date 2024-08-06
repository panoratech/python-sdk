# Tickets
(*ticketing.tickets*)

### Available Operations

* [list](#list) - List  Tickets
* [create](#create) - Create Tickets
* [retrieve](#retrieve) - Retrieve Tickets

## list

List  Tickets

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.tickets.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListTicketingTicketResponse](../../models/listticketingticketresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Tickets in any supported Ticketing software

### Example Usage

```python
import dateutil.parser
import panora_sdk
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.tickets.create(x_connection_token="<value>", unified_ticketing_ticket_input={
    "name": "Customer Service Inquiry",
    "description": "Help customer",
    "status": panora_sdk.UnifiedTicketingTicketInputStatus.OPEN,
    "due_date": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "type": panora_sdk.UnifiedTicketingTicketInputType.BUG,
    "parent_ticket": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "collections": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "tags": [
        "my_tag",
        "urgent_tag",
    ],
    "completed_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "priority": panora_sdk.UnifiedTicketingTicketInputPriority.HIGH,
    "assigned_to": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "comment": {
        "body": "Assigned to Eric !",
        "html_body": "<p>Assigned to Eric !</p>",
        "is_private": False,
        "creator_type": panora_sdk.UnifiedTicketingTicketInputCreatorType.USER,
        "ticket_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
        "contact_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
        "user_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
        "attachments": [
            "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
        ],
    },
    "account_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "contact_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "attachments": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "field_mappings": {
        "fav_dish": "broccoli",
        "fav_color": "red",
    },
}, remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `x_connection_token`                                                              | *str*                                                                             | :heavy_check_mark:                                                                | The connection token                                                              |                                                                                   |
| `unified_ticketing_ticket_input`                                                  | [models.UnifiedTicketingTicketInput](../../models/unifiedticketingticketinput.md) | :heavy_check_mark:                                                                | N/A                                                                               |                                                                                   |
| `remote_data`                                                                     | *Optional[bool]*                                                                  | :heavy_minus_sign:                                                                | Set to true to include data from the original Ticketing software.                 | false                                                                             |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |


### Response

**[models.UnifiedTicketingTicketOutput](../../models/unifiedticketingticketoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Tickets from any connected Ticketing software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ticketing.tickets.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the `ticket` you want to retrive.                             | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ticketing software.   | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UnifiedTicketingTicketOutput](../../models/unifiedticketingticketoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
