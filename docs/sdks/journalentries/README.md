# Journalentries
(*accounting.journalentries*)

### Available Operations

* [list](#list) - List  JournalEntrys
* [create](#create) - Create Journal Entries
* [retrieve](#retrieve) - Retrieve Journal Entries

## list

List  JournalEntrys

### Example Usage

```python
from panora_sdk import Panora

s = Panora()


res = s.accounting.journalentries.list(x_connection_token="<value>")

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

**[models.ListAccountingJournalEntryResponseBody](../../models/listaccountingjournalentryresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Journal Entries in any supported Accounting software

### Example Usage

```python
from panora_sdk import Panora

s = Panora()


res = s.accounting.journalentries.create(x_connection_token="<value>", unified_accounting_journalentry_input={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                            | *str*                                                                                           | :heavy_check_mark:                                                                              | The connection token                                                                            |
| `unified_accounting_journalentry_input`                                                         | [models.UnifiedAccountingJournalentryInput](../../models/unifiedaccountingjournalentryinput.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `remote_data`                                                                                   | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Set to true to include data from the original Accounting software.                              |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |


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

s = Panora()


res = s.accounting.journalentries.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the journalentry you want to retrieve.                        |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Accounting software.  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UnifiedAccountingJournalentryOutput](../../models/unifiedaccountingjournalentryoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
