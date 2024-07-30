# Templates
(*marketingautomation.templates*)

### Available Operations

* [list](#list) - List  Templates
* [create](#create) - Create Template
* [retrieve](#retrieve) - Retrieve Templates

## list

List  Templates

### Example Usage

```python
import os
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


res = s.marketingautomation.templates.list(x_connection_token="<value>")

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

**[models.ListMarketingautomationTemplatesResponseBody](../../models/listmarketingautomationtemplatesresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create a template in any supported Marketingautomation software

### Example Usage

```python
import os
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


res = s.marketingautomation.templates.create(x_connection_token="<value>", unified_marketingautomation_template_input={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                                      | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The connection token                                                                                      |
| `unified_marketingautomation_template_input`                                                              | [models.UnifiedMarketingautomationTemplateInput](../../models/unifiedmarketingautomationtemplateinput.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `remote_data`                                                                                             | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Set to true to include data from the original Marketingautomation software.                               |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |


### Response

**[models.UnifiedMarketingautomationTemplateOutput](../../models/unifiedmarketingautomationtemplateoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Templates from any connected Marketingautomation software

### Example Usage

```python
import os
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


res = s.marketingautomation.templates.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the template you want to retrieve.                                    |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |


### Response

**[models.UnifiedMarketingautomationTemplateOutput](../../models/unifiedmarketingautomationtemplateoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
