<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from panora_sdk import Panora

s = Panora()


res = s.hello()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from panora_sdk import Panora

async def main():
    s = Panora()
    res = await s.hello_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->