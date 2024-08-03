# PassThroughRequestDto


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `method`                                           | [models.Method](../models/method.md)               | :heavy_check_mark:                                 | N/A                                                |
| `path`                                             | *Nullable[str]*                                    | :heavy_check_mark:                                 | N/A                                                |
| `data`                                             | [OptionalNullable[models.Data]](../models/data.md) | :heavy_minus_sign:                                 | N/A                                                |
| `headers`                                          | Dict[str, *Any*]                                   | :heavy_minus_sign:                                 | N/A                                                |