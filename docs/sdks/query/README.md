# Query
(*rag.query*)

## Overview

### Available Operations

* [rag_controller_query_embeddings](#rag_controller_query_embeddings)

## rag_controller_query_embeddings

### Example Usage

```python
from panora_sdk import Panora

s = Panora(
    api_key="<YOUR_API_KEY_HERE>",
)

res = s.rag.query.rag_controller_query_embeddings()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RagControllerQueryEmbeddingsResponseBody](../../models/ragcontrollerqueryembeddingsresponsebody.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
