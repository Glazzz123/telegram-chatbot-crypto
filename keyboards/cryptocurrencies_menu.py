from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_cryptocurrencies_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Рейтинг", callback_data='ranking')],
        [InlineKeyboardButton(text="Рост и падение", callback_data='growth_decline')],
        [InlineKeyboardButton(text="В тренде", callback_data='trending')],
        [InlineKeyboardButton(text="Предстоящее", callback_data='upcoming')]
    ])
    return keyboard
