# Candidates
(*ats.candidates*)

## Overview

### Available Operations

* [list](#list) - List  Candidates
* [create](#create) - Create Candidates
* [retrieve](#retrieve) - Retrieve Candidates

## list

List  Candidates

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ats.candidates.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListAtsCandidateResponse](../../models/listatscandidateresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create

Create Candidates in any supported Ats software

### Example Usage

```python
import dateutil.parser
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ats.candidates.create(x_connection_token="<value>", unified_ats_candidate_input={
    "first_name": "Joe",
    "last_name": "Doe",
    "company": "Acme",
    "title": "Analyst",
    "locations": "New York",
    "is_private": False,
    "email_reachable": True,
    "remote_created_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "remote_modified_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "last_interaction_at": dateutil.parser.isoparse("2024-10-01T12:00:00Z"),
    "attachments": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "applications": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "tags": [
        "tag_1",
        "tag_2",
    ],
    "urls": [
        {
            "url": "mywebsite.com",
            "url_type": "WEBSITE",
        },
    ],
    "phone_numbers": [
        {
            "phone_number": "+33660688899",
            "phone_type": "WORK",
        },
    ],
    "email_addresses": [
        {
            "email_address": "joedoe@gmail.com",
            "email_address_type": "WORK",
        },
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

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |                                                                             |
| `unified_ats_candidate_input`                                               | [models.UnifiedAtsCandidateInput](../../models/unifiedatscandidateinput.md) | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Ats software.                 | false                                                                       |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.UnifiedAtsCandidateOutput](../../models/unifiedatscandidateoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## retrieve

Retrieve Candidates from any connected Ats software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ats.candidates.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the candidate you want to retrieve.                           | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ats software.         | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnifiedAtsCandidateOutput](../../models/unifiedatscandidateoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
