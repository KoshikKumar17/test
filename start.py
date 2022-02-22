# (c) @TheTgRoBots
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
        thetgrobots = await update.reply_text("**Processing...⏸️**")
        await thetgrobots.edit_text(
        text=script.START_TEXT,
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Click Here to Review ✨', url='https://comments.bot/thread/--pwqNLA2')]]),
        disable_web_page_preview = True
    )
