# Products
(*ecommerce.products*)

## Overview

### Available Operations

* [list](#list) - List Products
* [create](#create) - Create Products
* [retrieve](#retrieve) - Retrieve Products

## list

List Products

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ecommerce.products.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListEcommerceProductsResponse](../../models/listecommerceproductsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create

Create Products in any supported Ecommerce software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ecommerce.products.create(x_connection_token="<value>", unified_ecommerce_product_input={
    "product_url": "https://product_url/tee",
    "product_type": "teeshirt",
    "product_status": "ACTIVE",
    "images_urls": [
        "https://myproduct/image",
    ],
    "description": "best tee ever",
    "vendor": "vendor_extern",
    "variants": [
        {},
    ],
    "tags": [
        "tag_1",
    ],
    "field_mappings": {},
}, remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `x_connection_token`                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The connection token                                                                |                                                                                     |
| `unified_ecommerce_product_input`                                                   | [models.UnifiedEcommerceProductInput](../../models/unifiedecommerceproductinput.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |                                                                                     |
| `remote_data`                                                                       | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Set to true to include data from the original Accounting software.                  | false                                                                               |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.UnifiedEcommerceProductOutput](../../models/unifiedecommerceproductoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## retrieve

Retrieve products from any connected Ats software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.ecommerce.products.retrieve(x_connection_token="<value>", id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the product you want to retrieve.                             |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ats software.         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UnifiedEcommerceProductOutput](../../models/unifiedecommerceproductoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |