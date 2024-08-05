# FieldMappings
(*field_mappings*)

### Available Operations

* [define_custom_field](#define_custom_field) - Create Custom Field

## define_custom_field

Create Custom Field

### Example Usage

```python
import panora_sdk
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.field_mappings.define_custom_field(request={
    "object_type_owner": panora_sdk.CustomFieldCreateDtoObjectTypeOwner.COMPANY,
    "name": "my_favorite_dish",
    "description": "Favorite Dish",
    "data_type": panora_sdk.CustomFieldCreateDtoDataType.STRING,
    "source_custom_field_id": "id_1",
    "source_provider": "hubspot",
    "linked_user_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CustomFieldCreateDto](../../models/customfieldcreatedto.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[models.CustomFieldResponse](../../models/customfieldresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
