import asyncio
import inspect
import logging
import typing as t

import aiohttp


async def start(  # function is async to ensure that event loop is running
    url: str,
    interval: int = 60,
    *,
    delay: int = 0,
    handle_exception: t.Callable[[Exception], t.Optional[t.Awaitable[None]]] = lambda e: logging.getLogger(
        "apykuma"
    ).exception(e),
) -> asyncio.Task[None]:
    return asyncio.create_task(_loop(url, interval, delay, handle_exception))


async def _loop(
    url: str, interval: int, delay: int, handle_exception: t.Callable[[Exception], t.Optional[t.Awaitable[None]]]
) -> None:
    await asyncio.sleep(delay)
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await ping(session, url)
            except Exception as e:
                handler = handle_exception(e)
                if inspect.iscoroutine(handler):
                    await handler

            await asyncio.sleep(interval)


async def ping(session: aiohttp.ClientSession, url: str) -> aiohttp.ClientResponse:
    async with session.get(url) as response:
        return response
