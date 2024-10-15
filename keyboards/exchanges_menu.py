from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Функция для создания кнопки биржи
def create_exchange_button(name, url):
    return InlineKeyboardButton(text=name, url=url)


# Меню бирж с реферальными ссылками
def create_exchanges_menu():
    exchanges = [
        {"name": "Binance", "url": "https://www.binance.com/activity/referral-entry/CPA?ref=CPA_001X35VF6W"},
        {"name": "OKX", "url": "https://okx.com/join/12274862"},
        {"name": "Bybit", "url": "https://www.bybit.com/invite?ref=RR6PAP"},
        {"name": "Kucoin", "url": "https://www.kucoin.com/r/rf/QBS4J7BH"},
        {"name": "Bitget", "url": "https://www.bgportable.com/ru/referral/register?clacCode=PP4LHBAN"}
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [create_exchange_button(exchange['name'], exchange['url'])] for exchange in exchanges
    ])

    return keyboard

