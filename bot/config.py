import os

class Config:
    API_ID = 25286584  # Replace with your API ID (integer)
    API_HASH = "0b02bf8fc3250ad0b37bd339e29b1983"  # Replace with your API Hash
    BOT_TOKEN = "8198028348:AAHCkggoS55DAP0fQ9wHQ1UXbUWkL8KE2Bw"  # Replace with your Bot Token
    MONGO_URI = "mongodb://localhost:27017"
    CHANNEL_ID = -1001234567890  # Replace with your Channel ID
    ADMIN_IDS = [7597291420]  # Replace with your Telegram User ID(s)
    CHECK_INTERVAL = 600
    CONCURRENCY_LIMIT = 3
    SITES_CONFIG = {"HDHub4u": True, "Bolly4u": True, "VegaMovies": True}
    MAX_RETRIES = 3
    RETRY_DELAY = 5
