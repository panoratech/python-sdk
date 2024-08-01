# Automations
(*marketingautomation.automations*)

### Available Operations

* [list](#list) - List  Automations
* [create](#create) - Create Automation
* [retrieve](#retrieve) - Retrieve Automations

## list

List  Automations

### Example Usage

```python
from panora_sdk import Panora

s = Panora()


res = s.marketingautomation.automations.list(x_connection_token="<value>")

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

**[models.ListMarketingautomationAutomationResponseBody](../../models/listmarketingautomationautomationresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create a automation in any supported Marketingautomation software

### Example Usage

```python
from panora_sdk import Panora

s = Panora()


res = s.marketingautomation.automations.create(x_connection_token="<value>", unified_marketingautomation_automation_input={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                                          | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The connection token                                                                                          |
| `unified_marketingautomation_automation_input`                                                                | [models.UnifiedMarketingautomationAutomationInput](../../models/unifiedmarketingautomationautomationinput.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `remote_data`                                                                                                 | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Set to true to include data from the original Marketingautomation software.                                   |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |


### Response

**[models.UnifiedMarketingautomationAutomationOutput](../../models/unifiedmarketingautomationautomationoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Automations from any connected Marketingautomation software

### Example Usage

```python
from panora_sdk import Panora

s = Panora()


res = s.marketingautomation.automations.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the automation you want to retrieve.                                  |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |


### Response

**[models.UnifiedMarketingautomationAutomationOutput](../../models/unifiedmarketingautomationautomationoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
