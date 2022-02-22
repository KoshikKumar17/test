# (c) @TheTgRoBots
import os
from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
        thetgrobots = await update.reply_text("**Processing...⏸️**")
        await thetgrobots.edit_text(
        text=script.REVIEW_TXT,
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Channel ✨', url='https://t.me/thetgrobots')]]),
        disable_web_page_preview = True
    )
