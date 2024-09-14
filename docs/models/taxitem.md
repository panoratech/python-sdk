# TaxItem


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `name`                               | *OptionalNullable[str]*              | :heavy_minus_sign:                   | The name of the tax                  | Federal Income Tax                   |
| `amount`                             | *OptionalNullable[float]*            | :heavy_minus_sign:                   | The amount of the tax                | 250                                  |
| `employer_tax`                       | *OptionalNullable[bool]*             | :heavy_minus_sign:                   | Indicates if this is an employer tax | true                                 |