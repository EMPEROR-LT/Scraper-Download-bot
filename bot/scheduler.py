from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.config import Config
import logging

logger = logging.getLogger(__name__)

def setup_scheduler(client):
    from bot.orchestrator import run_scrape_once
    scheduler = AsyncIOScheduler()
    # Adding the job to run at the specified interval
    scheduler.add_job(run_scrape_once, "interval", seconds=Config.CHECK_INTERVAL, args=[client])
    scheduler.start()
    logger.info(f"Scheduler started with interval: {Config.CHECK_INTERVAL} seconds.")
