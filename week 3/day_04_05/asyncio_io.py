# import asyncio # asynchronous input output 
# import aiohttp
# from program_timer import timer 
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# URL = "https://httpbin.org/uuid"

# async def fetch_uuid(session, url):
#     async with session.get(url) as response:
#         json_data = await response.json()
#         print(json_data['uuid'])


# async def func():
#     async with aiohttp.Clientsession() as session:
#         tasks = [fetch_uuid(session, URL) for _ in range(100)]
#         await asyncio.gather(*tasks)

# @timer(1, 1)
# async def main():
#     asyncio.run(func())

import asyncio
import aiohttp


from program_timer import timer

URL = "https://httpbin.org/uuid"

async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response["uuid"])

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)

@timer(1, 1)
def func():
    asyncio.run(main())

