# Files
(*filestorage.files*)

### Available Operations

* [list](#list) - List  Files
* [create](#create) - Create Files
* [retrieve](#retrieve) - Retrieve Files

## list

List  Files

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.filestorage.files.list(x_connection_token="<value>")

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

**[models.ListFilestorageFileResponseBody](../../models/listfilestoragefileresponsebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Files in any supported Filestorage software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.filestorage.files.create(x_connection_token="<value>", remote_data=False, unified_filestorage_file_input={
    "name": "<value>",
    "file_url": "<value>",
    "mime_type": "<value>",
    "size": "<value>",
    "folder_id": "<value>",
    "permission": "<value>",
    "shared_link": "<value>",
    "field_mappings": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `x_connection_token`                                                              | *str*                                                                             | :heavy_check_mark:                                                                | The connection token                                                              |
| `remote_data`                                                                     | *bool*                                                                            | :heavy_check_mark:                                                                | N/A                                                                               |
| `unified_filestorage_file_input`                                                  | [models.UnifiedFilestorageFileInput](../../models/unifiedfilestoragefileinput.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |


### Response

**[models.UnifiedFilestorageFileOutput](../../models/unifiedfilestoragefileoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Files from any connected Filestorage software

### Example Usage

```python
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


res = s.filestorage.files.retrieve(x_connection_token="<value>", id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `x_connection_token`                                                 | *str*                                                                | :heavy_check_mark:                                                   | The connection token                                                 |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | id of the file you want to retrieve.                                 |
| `remote_data`                                                        | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Set to true to include data from the original File Storage software. |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |


### Response

**[models.UnifiedFilestorageFileOutput](../../models/unifiedfilestoragefileoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
