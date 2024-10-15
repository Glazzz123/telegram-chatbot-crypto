from aiogram import Router, types
from aiogram.filters import Command  # Новый фильтр для команд
from aiogram.types import Message, CallbackQuery
from models import save_user_action, get_user_history
from lexicon.lexicon import LEXICON_RESPONSES  # Ваши сообщения приветствия
from keyboards.main_menu import create_main_menu
from keyboards.cryptocurrencies_menu import create_cryptocurrencies_menu
from keyboards.exchanges_menu import create_exchanges_menu
from keyboards.products_menu import create_products_menu

router = Router()


# Обработчик для команды /help
@router.message(Command('help'))
async def send_help(message: types.Message):
    help_text = """
    Доступные команды:
    /help — получить справку о доступных командах
    /history — получить последние 10 запросов
    /start — начало работы с ботом
    """
    await message.reply(help_text)


# Обработчик для команды /history
@router.message(Command('history'))
async def send_history(message: types.Message):
    save_user_action(message.from_user.id, '/history')

    user_id = message.from_user.id
    history = get_user_history(user_id)

    if history:
        history_text = "\n".join([f"{entry.command} - {entry.timestamp}" for entry in history])
    else:
        history_text = "История пуста."

    await message.reply(history_text)


# Обработчик команды /start
@router.message(Command('start'))
async def cmd_start(message: Message):
    save_user_action(message.from_user.id, '/start')
    await message.answer(LEXICON_RESPONSES['welcome'], reply_markup=create_main_menu())


# Обработчики для кнопок меню
@router.callback_query(lambda c: c.data == 'cryptocurrencies')
async def cryptocurrencies_callback_handler(callback: CallbackQuery):
    save_user_action(callback.from_user.id, 'cryptocurrencies')
    await callback.message.answer("Вы выбрали раздел 'Криптовалюты'", reply_markup=create_cryptocurrencies_menu())
    await callback.answer()


@router.callback_query(lambda c: c.data == 'exchanges')
async def exchanges_callback_handler(callback: CallbackQuery):
    save_user_action(callback.from_user.id, 'exchanges')
    await callback.message.answer("Вы выбрали раздел 'Биржи'", reply_markup=create_exchanges_menu())
    await callback.answer()


@router.callback_query(lambda c: c.data == 'products')
async def products_callback_handler(callback: CallbackQuery):
    save_user_action(callback.from_user.id, 'products')
    await callback.message.answer("Вы выбрали раздел 'Продукты'", reply_markup=create_products_menu())
    await callback.answer()


@router.callback_query(lambda c: c.data == 'news')
async def news_callback_handler(callback: CallbackQuery):
    save_user_action(callback.from_user.id, 'news')
    await callback.message.answer("Вы выбрали раздел 'Новости'")
    await callback.answer()


@router.callback_query(lambda c: c.data == 'community')
async def community_callback_handler(callback: CallbackQuery):
    save_user_action(callback.from_user.id, 'community')
    await callback.message.answer("Вы выбрали раздел 'Сообщество'")
    await callback.answer()













