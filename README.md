# Movie Leech Bot

A Telegram bot to leech movies.

## Deployment on Render

1. Create a new **Web Service** on Render.
2. Connect your repository.
3. Select **Python** as the runtime.
4. Set the **Start Command** to `python main.py`.
5. Add the following **Environment Variables**:
   - `API_ID`: Your Telegram API ID.
   - `API_HASH`: Your Telegram API Hash.
   - `BOT_TOKEN`: Your Telegram Bot Token.
   - `MONGO_URI`: Your MongoDB connection string.
   - `CHANNEL_ID`: The ID of the channel where movies will be posted.
   - `ADMIN_IDS`: Comma-separated list of admin user IDs.
   - `PORT`: (Optional) Render sets this automatically, bot uses 8080 by default.

## Local Development

1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.sample` to `.env` and fill in your credentials.
3. Run the bot: `python main.py`
