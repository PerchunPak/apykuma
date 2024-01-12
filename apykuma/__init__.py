import aiohttp
import asyncio


def start(
    url: str,
    interval: int = 60,
) -> asyncio.Task:
    return asyncio.create_task(_loop(url, interval))


async def _loop(
    url: str,
    interval: int = 60
) -> None:
    async with aiohttp.ClientSession() as session:
        while True:
            await ping(session, url)
            await asyncio.sleep(interval)


async def ping(session: aiohttp.ClientSession, url: str) -> aiohttp.ClientResponse:
    async with session.get(url) as response:
        return response
