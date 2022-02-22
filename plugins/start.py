# (c) @TheTgRoBots
import os
from Script import script
from Buttons import buttons
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
        thetgrobots = await update.reply_text("**Processing...⏸️**")
        await thetgrobots.edit_text(
        text=script.START_TEXT,
        reply_markup=buttons.START_BUTTONS,
       disable_web_page_preview=True
    )
