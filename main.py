# (c) @TheTgRoBots

import os
from pyrogram import Client
from config import Config

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name="RENAMEBOT",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.TG_BOT_TOKEN,
            plugins={"root": "root/plugins"},
            sleep_threshold=5
        )


Bot.run()
