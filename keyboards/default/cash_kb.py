from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




cash_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Криптокошельки⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="Платёжные системы⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="Номер банковской карты⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)


cripto_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BTC⁣⁣⁣⁣⁣⁣"),
            KeyboardButton(text="ETH⁣⁣⁣⁣⁣⁣"),
            KeyboardButton(text="DASH⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="DOGE⁣⁣⁣⁣⁣⁣"),
            KeyboardButton(text="LTC⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="Другой⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)

cash2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Webmoney⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="Venmo⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)

cash3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Любого⁣⁣⁣⁣⁣⁣"),
        ],
        # [
        #     KeyboardButton(text="🇺🇦 Украины⁣⁣⁣⁣⁣⁣"),
        # ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)

cash4_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти номер телефона или логин⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="Найти ФИО⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)