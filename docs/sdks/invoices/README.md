# Invoices
(*accounting.invoices*)

### Available Operations

* [list](#list) - List  Invoices
* [create](#create) - Create Invoices
* [retrieve](#retrieve) - Retrieve Invoices

## list

List  Invoices

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.accounting.invoices.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListAccountingInvoiceResponse](../../models/listaccountinginvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create invoices in any supported Accounting software

### Example Usage

```python
import dateutil.parser
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.accounting.invoices.create(x_connection_token="<value>", unified_accounting_invoice_input={
    "type": "Sales",
    "number": "INV-001",
    "issue_date": dateutil.parser.isoparse("2024-06-15T12:00:00Z"),
    "due_date": dateutil.parser.isoparse("2024-07-15T12:00:00Z"),
    "paid_on_date": dateutil.parser.isoparse("2024-07-10T12:00:00Z"),
    "memo": "Payment for services rendered",
    "currency": "USD",
    "exchange_rate": "1.2",
    "total_discount": 1000,
    "sub_total": 10000,
    "status": "Paid",
    "total_tax_amount": 1000,
    "total_amount": 11000,
    "balance": 0,
    "contact_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "accounting_period_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "tracking_categories": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
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

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | The connection token                                                                  |                                                                                       |
| `unified_accounting_invoice_input`                                                    | [models.UnifiedAccountingInvoiceInput](../../models/unifiedaccountinginvoiceinput.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |                                                                                       |
| `remote_data`                                                                         | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Set to true to include data from the original Accounting software.                    | false                                                                                 |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |


### Response

**[models.UnifiedAccountingInvoiceOutput](../../models/unifiedaccountinginvoiceoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Invoices from any connected Accounting software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.accounting.invoices.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the invoice you want to retrieve.                             | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Accounting software.  | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UnifiedAccountingInvoiceOutput](../../models/unifiedaccountinginvoiceoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
