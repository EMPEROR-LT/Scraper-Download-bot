import asyncio
import logging
from bot.bot import MovieBot

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def main():
    bot = MovieBot()
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
