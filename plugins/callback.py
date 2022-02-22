# (c) @TheTgRoBots

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "start":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT.format((await bot.get_me()).username),
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    elif update.data == "close":
        await update.message.delete()
