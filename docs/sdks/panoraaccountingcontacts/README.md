# PanoraAccountingContacts
(*accounting.contacts*)

### Available Operations

* [list](#list) - List  Contacts
* [create](#create) - Create Contacts
* [retrieve](#retrieve) - Retrieve Contacts

## list

List  Contacts

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.accounting.contacts.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListAccountingContactsResponse](../../models/listaccountingcontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create contacts in any supported Accounting software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.accounting.contacts.create(x_connection_token="<value>", unified_accounting_contact_input={
    "name": "John Doe",
    "is_supplier": True,
    "is_customer": False,
    "email_address": "john.doe@example.com",
    "tax_number": "123456789",
    "status": "Active",
    "currency": "USD",
    "remote_updated_at": "2024-06-15T12:00:00Z",
    "company_info_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
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
| `unified_accounting_contact_input`                                                    | [models.UnifiedAccountingContactInput](../../models/unifiedaccountingcontactinput.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |                                                                                       |
| `remote_data`                                                                         | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Set to true to include data from the original Accounting software.                    | false                                                                                 |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |


### Response

**[models.UnifiedAccountingContactOutput](../../models/unifiedaccountingcontactoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Contacts from any connected Accounting software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.accounting.contacts.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the contact you want to retrieve.                             | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Accounting software.  | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.UnifiedAccountingContactOutput](../../models/unifiedaccountingcontactoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
