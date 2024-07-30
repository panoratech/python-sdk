# FieldMappings
(*field_mappings*)

### Available Operations

* [define](#define) - Define target Field
* [create](#create) - Create Custom Field
* [map](#map) - Map Custom Field

## define

Define target Field

### Example Usage

```python
import os
from panora import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.field_mappings.define(request={
    "object_type_owner": "<value>",
    "name": "<value>",
    "description": "Optimized object-oriented emulation",
    "data_type": "float",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DefineTargetFieldDto](../../models/definetargetfielddto.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create

Create Custom Field

### Example Usage

```python
import os
from panora import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.field_mappings.create(request={
    "object_type_owner": "<value>",
    "name": "<value>",
    "description": "Multi-tiered human-resource model",
    "data_type": "enum",
    "source_custom_field_id": "<value>",
    "source_provider": "<value>",
    "linked_user_id": "<value>",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CustomFieldCreateDto](../../models/customfieldcreatedto.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## map

Map Custom Field

### Example Usage

```python
import os
from panora import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.field_mappings.map(request={
    "attribute_id": "<value>",
    "source_custom_field_id": "<value>",
    "source_provider": "<value>",
    "linked_user_id": "<value>",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.MapFieldToProviderDto](../../models/mapfieldtoproviderdto.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
