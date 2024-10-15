from aiogram import Router
from aiogram.types import CallbackQuery
from services import get_top_50_cryptos, get_growth_decline, get_trending_cryptos

router = Router()

# Обработчик для кнопки "Рейтинг"
@router.callback_query(lambda c: c.data == 'ranking')
async def ranking_callback_handler(callback: CallbackQuery):
    ranking_data = get_top_50_cryptos()  # Убираем передачу api_key, он загружается автоматически из .env
    await callback.message.answer(ranking_data)
    await callback.answer()

# Обработчик для кнопки "Рост и падение"
@router.callback_query(lambda c: c.data == 'growth_decline')
async def growth_decline_callback_handler(callback: CallbackQuery):
    growth_decline_data = get_growth_decline()  # Убираем передачу api_key
    await callback.message.answer(growth_decline_data)
    await callback.answer()

# Обработчик для кнопки "В тренде"
@router.callback_query(lambda c: c.data == 'trending')
async def trending_callback_handler(callback: CallbackQuery):
    trending_data = get_trending_cryptos()  # Убираем передачу api_key
    await callback.message.answer(trending_data)
    await callback.answer()



