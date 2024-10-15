from aiogram import Router
from aiogram.types import CallbackQuery
from services.product_services import get_airdrops, get_events_calendar, get_ico_calendar

router = Router()

# Обработчик для кнопки "Airdrops"
@router.callback_query(lambda c: c.data == 'airdrops')
async def airdrops_callback_handler(callback: CallbackQuery):
    airdrops_info = get_airdrops()
    await callback.message.answer(airdrops_info)
    await callback.answer()

# Обработчик для кнопки "Календарь мероприятий"
@router.callback_query(lambda c: c.data == 'events_calendar')
async def events_calendar_callback_handler(callback: CallbackQuery):
    events_info = get_events_calendar()
    await callback.message.answer(events_info)
    await callback.answer()

# Обработчик для кнопки "Календарь ICO"
@router.callback_query(lambda c: c.data == 'ico_calendar')
async def ico_calendar_callback_handler(callback: CallbackQuery):
    ico_info = get_ico_calendar()
    await callback.message.answer(ico_info)
    await callback.answer()

