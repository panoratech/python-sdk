# Payments
(*accounting.payments*)

### Available Operations

* [list](#list) - List  Payments
* [create](#create) - Create Payments
* [retrieve](#retrieve) - Retrieve Payments

## list

List  Payments

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.accounting.payments.list(x_connection_token="<value>")

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

**[models.ListAccountingPaymentResponseBody](../../models/listaccountingpaymentresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Payments in any supported Accounting software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.accounting.payments.create(x_connection_token="<value>", unified_accounting_payment_input={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | The connection token                                                                  |
| `unified_accounting_payment_input`                                                    | [models.UnifiedAccountingPaymentInput](../../models/unifiedaccountingpaymentinput.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `remote_data`                                                                         | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Set to true to include data from the original Accounting software.                    |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |


### Response

**[models.UnifiedAccountingPaymentOutput](../../models/unifiedaccountingpaymentoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Payments from any connected Accounting software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.accounting.payments.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the payment you want to retrieve.                             |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Accounting software.  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UnifiedAccountingPaymentOutput](../../models/unifiedaccountingpaymentoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
