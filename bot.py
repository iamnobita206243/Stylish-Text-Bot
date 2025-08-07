import time
import datetime
print(f"Current time: {datetime.datetime.now()}")
time.sleep(5)

import pyrogram
import logging
import os
from config import Config
from pyrogram import Client 

# Logging setup
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":
    plugins = dict(root="plugins")
    app = Client(
        "ShowJson",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100,
        sleep_threshold=60
    )
    app.run()
