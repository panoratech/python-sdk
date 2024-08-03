# Map
(*field_mappings.map*)

### Available Operations

* [map](#map) - Map Custom Field

## map

Map Custom Field

### Example Usage

```python
import os
from panora_sdk import Panora

s = Panora(
    api_key=os.getenv("API_KEY", ""),
)


res = s.field_mappings.map.map(request={
    "attribute_id": "<value>",
    "source_custom_field_id": "<value>",
    "source_provider": "<value>",
    "linked_user_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.MapFieldToProviderDto](../../models/mapfieldtoproviderdto.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |


### Response

**[models.CustomFieldResponse](../../models/customfieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
