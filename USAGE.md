<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from openapi import SDK
import os

s = SDK(
    bearer=os.getenv("BEARER", ""),
)


s.hello()

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from openapi import SDK
import os

async def main():
    s = SDK(
        bearer=os.getenv("BEARER", ""),
    )
    await s.hello_async()
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->