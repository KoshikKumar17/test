# (c) @TheTgRoBots
class buttons(object):
START_BUTTONS = """InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤔 Help 🤔', callback_data='help'),
        InlineKeyboardButton('😇 About 😇', callback_data='about')
        ],[
        InlineKeyboardButton('↗️ Channel ↗️', url='https://t.me/thetgrobots'),
        InlineKeyboardButton('⭕ GitHub', url='https://github.com/The-TG-RoBots')
        ],[
        InlineKeyboardButton('❌ Close ❌', callback_data='close')
        ]]
    )"""
HELP_BUTTONS = """InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️ Back', callback_data='start')
        ]]
    )"""
ABOUT_BUTTONS = """InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️ Back', callback_data='start')
        ]]
    )"""
