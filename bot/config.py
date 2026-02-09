import os

class Config:
    API_ID = 0  # Replace with your API ID (integer)
    API_HASH = ""  # Replace with your API Hash
    BOT_TOKEN = ""  # Replace with your Bot Token
    MONGO_URI = "mongodb://localhost:27017"
    CHANNEL_ID = -1001234567890  # Replace with your Channel ID
    ADMIN_IDS = [123456789]  # Replace with your Telegram User ID(s)
    CHECK_INTERVAL = 600
    CONCURRENCY_LIMIT = 3
    SITES_CONFIG = {"HDHub4u": True, "Bolly4u": True, "VegaMovies": True}
    MAX_RETRIES = 3
    RETRY_DELAY = 5
