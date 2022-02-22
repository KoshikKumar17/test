# (c) @TheTgRoBots

import os
from pyrogram import Client
from info import SESSION, APP_ID, API_HASH, BOT_TOKEN

plugins = dict(root="plugins")
Bot = Client(
    session_name=SESSION,
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    plugins=plugins
)


Bot.run()
