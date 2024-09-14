# Interviews
(*ats.interviews*)

## Overview

### Available Operations

* [list](#list) - List  Interviews
* [create](#create) - Create Interviews
* [retrieve](#retrieve) - Retrieve Interviews

## list

List  Interviews

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ats.interviews.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

if res is not None:
    while True:
        # handle items

        res = res.next()
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

**[models.ListAtsInterviewResponse](../../models/listatsinterviewresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create

Create Interviews in any supported Ats software

### Example Usage

```python
import dateutil.parser
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ats.interviews.create(x_connection_token="<value>", unified_ats_interview_input={
    "status": "SCHEDULED",
    "application_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "job_interview_stage_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "organized_by": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "interviewers": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "location": "San Francisco",
    "start_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "end_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "remote_created_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "remote_updated_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
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

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |                                                                             |
| `unified_ats_interview_input`                                               | [models.UnifiedAtsInterviewInput](../../models/unifiedatsinterviewinput.md) | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Ats software.                 | false                                                                       |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.UnifiedAtsInterviewOutput](../../models/unifiedatsinterviewoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## retrieve

Retrieve Interviews from any connected Ats software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ats.interviews.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the interview you want to retrieve.                           | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ats software.         | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnifiedAtsInterviewOutput](../../models/unifiedatsinterviewoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
