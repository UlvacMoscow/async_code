from time import sleep
from time import time
import asyncio

start = time()

async def spider(name):
    for page in range(1, 4):
        await asyncio.sleep(1)
        print(name, page)

spiders = [
    asyncio.ensure_future(spider('Blog_1')),
    asyncio.ensure_future(spider('Blog_2')),
    asyncio.ensure_future(spider('Blog_3'))
]

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*spiders))
event_loop.close()


print("{:.2F}".format(time() - start))


