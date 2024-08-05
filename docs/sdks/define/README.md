# Define
(*field_mappings.define*)

### Available Operations

* [definitions](#definitions) - Define target Field

## definitions

Define target Field

### Example Usage

```python
import panora_sdk
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.field_mappings.define.definitions(request={
    "object_type_owner": panora_sdk.ObjectTypeOwner.COMPANY,
    "name": "fav_dish",
    "description": "My favorite dish",
    "data_type": panora_sdk.DataType.STRING,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DefineTargetFieldDto](../../models/definetargetfielddto.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CustomFieldResponse](../../models/customfieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
