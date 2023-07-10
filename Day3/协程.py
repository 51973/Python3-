# import asyncio
#
# async def execute(x):
#     print('Number:', x)
#
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('调用执行后')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('调用循环后')




# import asyncio
#
# async def execute(x):
#     print('Number:', x)
#     return x
#
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('调用执行后')
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('调用循环后')



import asyncio
import requests
import time
import aiohttp

start = time.time()

async def get(url):
    session = aiohttp.ClientSession()
    resp = await  session.get(url)
    await resp.text()
    await session.close()
    return resp

async def request():
    url = "https://www.httpbin.org/delay/5"
    print('Waiting for',url)
    resp = await get(url)
    print('Get response from',url,'resp',resp)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('Cost time:',end - start)












