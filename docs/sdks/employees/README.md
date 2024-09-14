# Employees
(*hris.employees*)

## Overview

### Available Operations

* [list](#list) - List Employees
* [create](#create) - Create Employees
* [retrieve](#retrieve) - Retrieve Employee

## list

List Employees

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.hris.employees.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListHrisEmployeesResponse](../../models/listhrisemployeesresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create

Create Employees in any supported Hris software

### Example Usage

```python
import dateutil.parser
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.hris.employees.create(x_connection_token="<value>", unified_hris_employee_input={
    "groups": [
        "Group1",
        "Group2",
    ],
    "locations": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "employee_number": "EMP001",
    "company_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "first_name": "John",
    "last_name": "Doe",
    "preferred_name": "Johnny",
    "display_full_name": "John Doe",
    "username": "johndoe",
    "work_email": "john.doe@company.com",
    "personal_email": "john.doe@personal.com",
    "mobile_phone_number": "+1234567890",
    "employments": [
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
        "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    ],
    "ssn": "123-45-6789",
    "gender": "MALE",
    "ethnicity": "AMERICAN_INDIAN_OR_ALASKA_NATIVE",
    "marital_status": "Married",
    "date_of_birth": dateutil.parser.isoparse("1990-01-01"),
    "start_date": dateutil.parser.isoparse("2020-01-01"),
    "employment_status": "ACTIVE",
    "termination_date": dateutil.parser.isoparse("2025-01-01"),
    "avatar_url": "https://example.com/avatar.jpg",
    "manager_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "field_mappings": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `x_connection_token`                                                        | *str*                                                                       | :heavy_check_mark:                                                          | The connection token                                                        |
| `unified_hris_employee_input`                                               | [models.UnifiedHrisEmployeeInput](../../models/unifiedhrisemployeeinput.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `remote_data`                                                               | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Set to true to include data from the original Hris software.                |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.UnifiedHrisEmployeeOutput](../../models/unifiedhrisemployeeoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## retrieve

Retrieve an Employee from any connected Hris software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.hris.employees.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |                                                                     |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the employee you want to retrieve.                            | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Hris software.        | false                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnifiedHrisEmployeeOutput](../../models/unifiedhrisemployeeoutput.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
