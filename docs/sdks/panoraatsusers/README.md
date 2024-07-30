# PanoraAtsUsers
(*ats.users*)

### Available Operations

* [list](#list) - List  Users
* [retrieve](#retrieve) - Retrieve Users

## list

List  Users

### Example Usage

```python
import os
from panora import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


res = s.ats.users.list(x_connection_token="<value>")

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

**[models.ListAtsUsersResponseBody](../../models/listatsusersresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Users from any connected Ats software

### Example Usage

```python
import os
from panora import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


res = s.ats.users.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `x_connection_token`                                                | *str*                                                               | :heavy_check_mark:                                                  | The connection token                                                |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | id of the user you want to retrieve.                                |
| `remote_data`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Set to true to include data from the original Ats software.         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.UnifiedAtsUserOutput](../../models/unifiedatsuseroutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
