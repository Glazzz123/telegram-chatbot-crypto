from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_products_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Airdrops", callback_data='airdrops')],
        [InlineKeyboardButton(text="Календарь мероприятий", callback_data='events_calendar')],
        [InlineKeyboardButton(text="Календарь ICO", callback_data='ico_calendar')]
    ])
    return keyboard
