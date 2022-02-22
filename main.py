# (c) @TheTgRoBots

import os
from pyrogram import Client
from info import SESSION, APP_ID, API_HASH, BOT_TOKEN

Bot = Client(
    session_name=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins,
)


Bot.run()
