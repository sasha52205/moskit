from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tools_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Виртуальный номер телефона"),
        ],
        [
            KeyboardButton(text="Бесплатные почтовые адреса⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="Визуализация данных"),
        ],
        [
            KeyboardButton(text="Расширения"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)






