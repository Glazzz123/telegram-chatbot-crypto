from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from services.exchanges_services import get_exchanges_list

router = Router()

# Обработчик для кнопки "Биржи"
@router.callback_query(lambda c: c.data == 'exchanges')
async def exchanges_callback_handler(callback: CallbackQuery):
    exchanges = get_exchanges_list()

    # Создание клавиатуры с биржами и кнопками "Зарегистрироваться"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"Зарегистрироваться на {exchange['name']}", url=exchange['url'])]
        for exchange in exchanges
    ])

    await callback.message.answer("Выберите биржу для регистрации:", reply_markup=keyboard)
    await callback.answer()



