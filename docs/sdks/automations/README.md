# Automations
(*marketingautomation.automations*)

### Available Operations

* [list](#list) - List Automations
* [create](#create) - Create Automation
* [retrieve](#retrieve) - Retrieve Automation

## list

List Automations

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.marketingautomation.automations.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListMarketingautomationAutomationsResponse](../../models/listmarketingautomationautomationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create a automation in any supported Marketingautomation software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.marketingautomation.automations.create(x_connection_token="<value>", unified_marketingautomation_automation_input={}, remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                                          | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The connection token                                                                                          |                                                                                                               |
| `unified_marketingautomation_automation_input`                                                                | [models.UnifiedMarketingautomationAutomationInput](../../models/unifiedmarketingautomationautomationinput.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `remote_data`                                                                                                 | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Set to true to include data from the original Marketingautomation software.                                   | false                                                                                                         |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |


### Response

**[models.UnifiedMarketingautomationAutomationOutput](../../models/unifiedmarketingautomationautomationoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve an Automation from any connected Marketingautomation software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.marketingautomation.automations.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |                                                                             |
| `id`                                                                        | *str*                                                                       | :heavy_check_mark:                                                          | id of the automation you want to retrieve.                                  | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                        |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Marketingautomation software. | false                                                                       |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |


### Response

**[models.UnifiedMarketingautomationAutomationOutput](../../models/unifiedmarketingautomationautomationoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
