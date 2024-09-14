# Orders
(*ecommerce.orders*)

## Overview

### Available Operations

* [list](#list) - List Orders
* [create](#create) - Create Orders
* [retrieve](#retrieve) - Retrieve Orders

## list

List Orders

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ecommerce.orders.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListEcommerceOrdersResponse](../../models/listecommerceordersresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create

Create Orders in any supported Ecommerce software

### Example Usage

```python
import dateutil.parser
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ecommerce.orders.create(x_connection_token="<value>", unified_ecommerce_order_input={
    "order_status": "UNSHIPPED",
    "order_number": "19823838833",
    "payment_status": "SUCCESS",
    "currency": "AUD",
    "total_price": 300,
    "total_discount": 10,
    "total_shipping": 120,
    "total_tax": 120,
    "fulfillment_status": "PENDING",
    "customer_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "items": [
        {
            "name": "Net Income",
            "value": 100000,
            "type": "Operating Activities",
            "parent_item": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
            "remote_id": "12345",
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

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `x_connection_token`                                                            | *str*                                                                           | :heavy_check_mark:                                                              | The connection token                                                            |                                                                                 |
| `unified_ecommerce_order_input`                                                 | [models.UnifiedEcommerceOrderInput](../../models/unifiedecommerceorderinput.md) | :heavy_check_mark:                                                              | N/A                                                                             |                                                                                 |
| `remote_data`                                                                   | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Set to true to include data from the original Accounting software.              | false                                                                           |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.UnifiedEcommerceOrderOutput](../../models/unifiedecommerceorderoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## retrieve

Retrieve orders from any connected Ats software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ecommerce.orders.retrieve(x_connection_token="<value>", id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the order you want to retrieve.                               |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ats software.         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnifiedEcommerceOrderOutput](../../models/unifiedecommerceorderoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
