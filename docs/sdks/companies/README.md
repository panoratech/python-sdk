# Companies
(*crm.companies*)

### Available Operations

* [list](#list) - List Companies
* [create](#create) - Create Companies
* [retrieve](#retrieve) - Retrieve Companies

## list

List Companies

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.crm.companies.list(x_connection_token="<value>")

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

**[models.ListCrmCompanyResponseBody](../../models/listcrmcompanyresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Companies in any supported CRM software

### Example Usage

```python
import panora_sdk
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.crm.companies.create(x_connection_token="<value>", unified_crm_company_input={
    "name": "Acme",
    "industry": panora_sdk.UnifiedCrmCompanyInputIndustry.ACCOUNTING,
    "number_of_employees": 10,
    "user_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "email_addresses": [
        {
            "email_address": "acme@gmail.com",
            "email_address_type": panora_sdk.EmailAddressType.WORK,
        },
    ],
    "addresses": [
        {
            "street_1": "5th Avenue",
            "street_2": "<value>",
            "city": "New York",
            "state": "NY",
            "postal_code": "46842",
            "country": "USA",
            "address_type": panora_sdk.AddressType.WORK,
            "owner_type": "<value>",
        },
    ],
    "phone_numbers": [
        {
            "phone_number": "+33660606067",
            "phone_type": panora_sdk.PhoneType.WORK,
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

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `x_connection_token`                                                    | *str*                                                                   | :heavy_check_mark:                                                      | The connection token                                                    |                                                                         |
| `unified_crm_company_input`                                             | [models.UnifiedCrmCompanyInput](../../models/unifiedcrmcompanyinput.md) | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `remote_data`                                                           | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Set to true to include data from the original CRM software.             | false                                                                   |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |


### Response

**[models.UnifiedCrmCompanyOutput](../../models/unifiedcrmcompanyoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Companies from any connected Crm software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.crm.companies.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the company you want to retrieve.                             | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Crm software.         | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UnifiedCrmCompanyOutput](../../models/unifiedcrmcompanyoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
