# (c) @TheTgRoBots
import os
from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
        thetgrobots = await update.reply_text("**Processing...⏸️**")
        await thetgrobots.edit_text(
        text=script.START_TEXT,
        reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton('🤔 Help 🤔', callback_data='help'),
                 InlineKeyboardButton('😇 About 😇', callback_data='about')
                 ],[
                 InlineKeyboardButton('↗️ Channel ↗️', url='https://t.me/thetgrobots'),
                 InlineKeyboardButton('⭕ GitHub', url='https://github.com/The-TG-RoBots)
                 ],[
                 InlineKeyboardButton('❌ Close ❌', callback_data='close')
        ]])
       disable_web_page_preview = True
    )
