# Journalentries
(*accounting.journalentries*)

## Overview

### Available Operations

* [list](#list) - List  JournalEntrys
* [create](#create) - Create Journal Entries
* [retrieve](#retrieve) - Retrieve Journal Entries

## list

List  JournalEntrys

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.accounting.journalentries.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListAccountingJournalEntryResponse](../../models/listaccountingjournalentryresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create

Create Journal Entries in any supported Accounting software

### Example Usage

```python
import dateutil.parser
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.accounting.journalentries.create(x_connection_token="<value>", unified_accounting_journalentry_input={
    "transaction_date": dateutil.parser.isoparse("2024-06-15T12:00:00Z"),
    "payments": [
        "payment1",
        "payment2",
    ],
    "applied_payments": [
        "appliedPayment1",
        "appliedPayment2",
    ],
    "memo": "Monthly expense journal entry",
    "currency": "USD",
    "exchange_rate": "1.2",
    "id_acc_company_info": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "journal_number": "JE-001",
    "tracking_categories": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "id_acc_accounting_period": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "posting_status": "Posted",
    "line_items": [
        {
            "name": "Net Income",
            "value": 100000,
            "type": "Operating Activities",
            "parent_item": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
            "remote_id": "report_item_1234",
            "remote_generated_at": dateutil.parser.isoparse("2024-07-01T12:00:00Z"),
            "company_info_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
            "created_at": dateutil.parser.isoparse("2024-06-15T12:00:00Z"),
            "modified_at": dateutil.parser.isoparse("2024-06-15T12:00:00Z"),
        },
    ],
    "field_mappings": {},
}, remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                            | *str*                                                                                           | :heavy_check_mark:                                                                              | The connection token                                                                            |                                                                                                 |
| `unified_accounting_journalentry_input`                                                         | [models.UnifiedAccountingJournalentryInput](../../models/unifiedaccountingjournalentryinput.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |                                                                                                 |
| `remote_data`                                                                                   | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Set to true to include data from the original Accounting software.                              | false                                                                                           |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |

### Response

**[models.UnifiedAccountingJournalentryOutput](../../models/unifiedaccountingjournalentryoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## retrieve

Retrieve Journal Entries from any connected Accounting software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.accounting.journalentries.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the journalentry you want to retrieve.                        | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Accounting software.  | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnifiedAccountingJournalentryOutput](../../models/unifiedaccountingjournalentryoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
