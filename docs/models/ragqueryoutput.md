# RagQueryOutput


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `chunk`                                                                                                        | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The chunk which matches the embed query                                                                        | Date : 06/07/2023                                                                                              |
| `metadata`                                                                                                     | Dict[str, *Any*]                                                                                               | :heavy_check_mark:                                                                                             | The metadata tied to the chunk                                                                                 | {<br/>"blobType": "",<br/>"text": "ATTESTATION"<br/>}                                                          |
| `score`                                                                                                        | *Nullable[float]*                                                                                              | :heavy_check_mark:                                                                                             | The score                                                                                                      | 0.87                                                                                                           |
| `embedding`                                                                                                    | List[*float*]                                                                                                  | :heavy_check_mark:                                                                                             | The embedding of the relevant chunk                                                                            | [<br/>-0.00442447886,<br/>-0.00116857514,<br/>0.00869117491,<br/>-0.0361584462,<br/>-0.00220073434,<br/>0.00946036354,<br/>-0.0101112155<br/>] |