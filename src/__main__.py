import asyncio

from loguru import logger

from src import utils
from src.config import Config


async def main() -> None:
    utils.setup_logging()
    logger.info("Hello World!")

    Config()
    # start app here


if __name__ == "__main__":
    asyncio.run(main())
