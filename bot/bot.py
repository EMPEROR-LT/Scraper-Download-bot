from pyrogram import Client, filters
from bot.config import Config
import logging
import asyncio

logger = logging.getLogger(__name__)

class MovieBot:
    def __init__(self):
        self.app = Client("movie_leech_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
        self.setup_handlers()

    def setup_handlers(self):
        @self.app.on_message(filters.command("start") & filters.user(Config.ADMIN_IDS))
        async def start_cmd(client, message):
            await message.reply_text("Welcome to Movie Leech Bot!")

        @self.app.on_message(filters.command("status") & filters.user(Config.ADMIN_IDS))
        async def status_cmd(client, message):
            status = "\n".join([f"- {s}: {'✅' if e else '❌'}" for s, e in Config.SITES_CONFIG.items()])
            await message.reply_text(f"Bot Status:\n{status}")

        @self.app.on_message(filters.command("toggle") & filters.user(Config.ADMIN_IDS))
        async def toggle_cmd(client, message):
            site = message.text.split()[1] if len(message.text.split()) > 1 else ""
            found = next((s for s in Config.SITES_CONFIG if s.lower() == site.lower()), None)
            if found:
                Config.SITES_CONFIG[found] = not Config.SITES_CONFIG[found]
                await message.reply_text(f"{found} is now {'Enabled' if Config.SITES_CONFIG[found] else 'Disabled'}")

        @self.app.on_message(filters.command("scrape") & filters.user(Config.ADMIN_IDS))
        async def scrape_cmd(client, message):
            from bot.orchestrator import run_scrape_once
            asyncio.create_task(run_scrape_once(client))
            await message.reply_text("Scrape started!")

    async def start(self):
        await self.app.start()
        from bot.scheduler import setup_scheduler
        setup_scheduler(self.app)
        await asyncio.Event().wait()
