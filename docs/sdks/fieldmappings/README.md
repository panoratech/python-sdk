# FieldMappings
(*field_mappings*)

### Available Operations

* [get_field_mapping_values](#get_field_mapping_values) - Retrieve field mappings values
* [get_field_mappings_entities](#get_field_mappings_entities) - Retrieve field mapping entities
* [get_field_mappings](#get_field_mappings) - Retrieve field mappings
* [definitions](#definitions) - Define target Field
* [define_custom_field](#define_custom_field) - Create Custom Field
* [map](#map) - Map Custom Field

## get_field_mapping_values

Retrieve field mappings values

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


s.field_mappings.get_field_mapping_values()

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_field_mappings_entities

Retrieve field mapping entities

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


s.field_mappings.get_field_mappings_entities()

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_field_mappings

Retrieve field mappings

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


s.field_mappings.get_field_mappings()

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## definitions

Define target Field

### Example Usage

```python
import panora_sdk
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.field_mappings.definitions(request={
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

## map

Map Custom Field

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.field_mappings.map(request={
    "attribute_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
    "source_custom_field_id": "id_1",
    "source_provider": "hubspot",
    "linked_user_id": "801f9ede-c698-4e66-a7fc-48d19eebaa4f",
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
