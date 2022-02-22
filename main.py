# (c) @TheTgRoBots

import os
from pyrogram import Client
from config import Config

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name="GROUP-BOT",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=plugins,
            sleep_threshold=5
        )


Bot.run()
