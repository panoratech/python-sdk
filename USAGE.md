<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from panora_sdk import Panora

s = Panora(
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
import os
from panora_sdk import Panora

async def main():
    s = Panora(
        bearer=os.getenv("BEARER", ""),
    )
    await s.hello_async()
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->