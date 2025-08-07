import time
import logging
import os

from config import Config
from pyrogram import Client

# Wait to sync time with Telegram servers
time.sleep(5)

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":
    plugins = dict(root="plugins")

    app = Client(
        "Showyson",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100,
        sleep_threshold=60
    )

    app.run()
