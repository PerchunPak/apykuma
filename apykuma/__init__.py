import asyncio

import aiohttp


async def start(  # function is async to ensure that event loop is running
    url: str,
    interval: int = 60,
) -> asyncio.Task[None]:
    return asyncio.create_task(_loop(url, interval))


async def _loop(url: str, interval: int = 60) -> None:
    async with aiohttp.ClientSession() as session:
        while True:
            await ping(session, url)
            await asyncio.sleep(interval)


async def ping(session: aiohttp.ClientSession, url: str) -> aiohttp.ClientResponse:
    async with session.get(url) as response:
        return response
