# import aiohttp
# import asyncio
#
# async def fetch(session,url):
#     async with session.get(url) as resp:
#         return await resp.text(),resp.status
#
# async def main():
#     async with aiohttp.ClientSession()as session:
#         html,status = await fetch(session,'https://cuiqingcai.com')
#         print(f'html: {html[:100]}...')
#         print(f'status: {status}')
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())




import asyncio
import aiohttp

async def main():
    params = {'name':'germay' ,'age':25}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.httpbin.org/get',params=params) as resp:
            print(await resp.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())