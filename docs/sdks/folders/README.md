# Folders
(*filestorage.folders*)

### Available Operations

* [list](#list) - List  Folders
* [create](#create) - Create Folders
* [retrieve](#retrieve) - Retrieve Folders

## list

List  Folders

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.filestorage.folders.list(x_connection_token="<value>", remote_data=True, limit=10, cursor="1b8b05bb-5273-4012-b520-8657b0b90874")

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

**[models.ListFilestorageFolderResponse](../../models/listfilestoragefolderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Folders in any supported Filestorage software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.filestorage.folders.create(x_connection_token="<value>", remote_data=False, unified_filestorage_folder_input={
    "name": "school",
    "size": "2048",
    "folder_url": "https://example.com/school",
    "description": "All things school related",
    "drive_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "parent_folder_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "shared_link": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "permission": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "field_mappings": {
        "fav_dish": "broccoli",
        "fav_color": "red",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `x_connection_token`                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | The connection token                                                                  |
| `remote_data`                                                                         | *bool*                                                                                | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `unified_filestorage_folder_input`                                                    | [models.UnifiedFilestorageFolderInput](../../models/unifiedfilestoragefolderinput.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |


### Response

**[models.UnifiedFilestorageFolderOutput](../../models/unifiedfilestoragefolderoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## retrieve

Retrieve Folders from any connected Filestorage software

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.filestorage.folders.retrieve(x_connection_token="<value>", id="801f9ede-c698-4e66-a7fc-48d19eebaa4f", remote_data=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `x_connection_token`                                                 | *str*                                                                | :heavy_check_mark:                                                   | The connection token                                                 |                                                                      |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | id of the folder you want to retrieve.                               | 801f9ede-c698-4e66-a7fc-48d19eebaa4f                                 |
| `remote_data`                                                        | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Set to true to include data from the original File Storage software. | false                                                                |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |


### Response

**[models.UnifiedFilestorageFolderOutput](../../models/unifiedfilestoragefolderoutput.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
