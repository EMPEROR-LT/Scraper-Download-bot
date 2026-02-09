import os

class Config:
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    MONGO_URI = os.environ.get("MONGO_URI", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", 0))
    # Expect ADMIN_IDS as a comma-separated string, e.g., "123456789,987654321"
    ADMIN_IDS = [int(x.strip()) for x in os.environ.get("ADMIN_IDS", "").split(",") if x.strip()]
    CHECK_INTERVAL = int(os.environ.get("CHECK_INTERVAL", 600))
    CONCURRENCY_LIMIT = int(os.environ.get("CONCURRENCY_LIMIT", 3))
    SITES_CONFIG = {
        "HDHub4u": os.environ.get("ENABLE_HDHUB4U", "True").lower() == "true",
        "Bolly4u": os.environ.get("ENABLE_BOLLY4U", "True").lower() == "true",
        "VegaMovies": os.environ.get("ENABLE_VEGAMOVIES", "True").lower() == "true"
    }
    MAX_RETRIES = int(os.environ.get("MAX_RETRIES", 3))
    RETRY_DELAY = int(os.environ.get("RETRY_DELAY", 5))
