from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

email_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Определить почтовый сервис"),
        ],
        [
            KeyboardButton(text="Любой⁣⁣⁣"),
        ],
        [
            # KeyboardButton(text="Yandex"),
            KeyboardButton(text="Gmail"),
            KeyboardButton(text="Mail.ru"),
        ],
        [
            KeyboardButton(text="ProtonMail"),
            KeyboardButton(text="Yahoo"),
            KeyboardButton(text="QQ"),
        ],
        [
            KeyboardButton(text="GMX.net"),
            KeyboardButton(text="Web.de"),
            KeyboardButton(text="Rambler"),
        ],
        [
            KeyboardButton(text="Aol"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)






