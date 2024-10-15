from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# Главное меню
def create_main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Криптовалюты", callback_data='cryptocurrencies')],
        [InlineKeyboardButton(text="Биржи", callback_data='exchanges')],
        [InlineKeyboardButton(text="Сообщество", callback_data='community')],
        [InlineKeyboardButton(text="Продукты", callback_data='products')],
        [InlineKeyboardButton(text="Новости", callback_data='news')]
    ])
    return keyboard




