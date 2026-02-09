import asyncio
import logging
import os
from aiohttp import web
from dotenv import load_dotenv
from bot.bot import MovieBot

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def health_check(request):
    return web.Response(text="Bot is running")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info(f"Health check server started on port {port}")

async def main():
    load_dotenv()
    # Start health check server for Render compatibility
    try:
        await start_web_server()
    except Exception as e:
        logger.error(f"Failed to start health check server: {e}")

    bot = MovieBot()
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
