# Applications
(*ats.applications*)

### Available Operations

* [list](#list) - List  Applications
* [create](#create) - Create Applications
* [retrieve](#retrieve) - Retrieve Applications

## list

List  Applications

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ats.applications.list(x_connection_token="<value>")

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

**[models.ListAtsApplicationResponseBody](../../models/listatsapplicationresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Applications in any supported Ats software

### Example Usage

```python
import dateutil.parser
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ats.applications.create(x_connection_token="<value>", unified_ats_application_input={
    "applied_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "rejected_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "offers": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
        "12345678-1234-1234-1234-123456789012",
    ],
    "source": "Source Name",
    "credited_to": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "current_stage": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "reject_reason": "Candidate not experienced enough",
    "candidate_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "job_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
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

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `x_connection_token`                                                            | *str*                                                                           | :heavy_check_mark:                                                              | The connection token                                                            |                                                                                 |
| `unified_ats_application_input`                                                 | [models.UnifiedAtsApplicationInput](../../models/unifiedatsapplicationinput.md) | :heavy_check_mark:                                                              | N/A                                                                             |                                                                                 |
| `remote_data`                                                                   | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Set to true to include data from the original Ats software.                     | false                                                                           |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |


### Response

**[models.UnifiedAtsApplicationOutput](../../models/unifiedatsapplicationoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Applications from any connected Ats software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.ats.applications.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the application you want to retrieve.                         | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ats software.         | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UnifiedAtsApplicationOutput](../../models/unifiedatsapplicationoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
