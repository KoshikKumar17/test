# (c) @TheTgRoBots

import os
from Script import script
from Buttons import buttons
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "start":
        await update.message.edit_text(
            text=script.START_TEXT,
            disable_web_page_preview=True,
            reply_markup=buttons.START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=script.HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=buttons.HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=script.ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=buttons.ABOUT_BUTTONS
        )
    elif update.data == "close":
        await update.message.delete()
