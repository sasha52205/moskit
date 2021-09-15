from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

global_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Номер телефона"),
            KeyboardButton(text="Аккаунт"),
            KeyboardButton(text="E-mail"),
        ],
        [
            KeyboardButton(text="ФИО"),
            KeyboardButton(text="Биометрия"),
            KeyboardButton(text="Ник"),
            #KeyboardButton(text="Адрес"),
        ],
        #[
            #KeyboardButton(text="Ник"),
            #KeyboardButton(text="Транспорт"),
            #KeyboardButton(text="Документы"),
        #],
        [
            KeyboardButton(text="Домен"),
            KeyboardButton(text="Файл"),
            KeyboardButton(text="Номер кошелька"),
        ],
        [
            KeyboardButton(text="Пароль"),
            KeyboardButton(text="Текст"),
            KeyboardButton(text="Трекер"),
        ],
        [
            KeyboardButton(text="Wi-Fi"),
            KeyboardButton(text="Серийный номер"),
            KeyboardButton(text="IMEI"),
        ],
      #  [
        #    KeyboardButton(text="🔍 Поисковики")
       # ],
        [
            KeyboardButton(text="🗄 Базы данных"),
            KeyboardButton(text="🛠 Инструменты"),
        ],
      #  [
        #    KeyboardButton(text="❔ Помощь"),
       #     KeyboardButton(text="📩 Контакты"),
       # ],
    ],
    resize_keyboard=True
)


###phone

phone_countryes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Любой⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="🇷🇺 России"),
            KeyboardButton(text="🇺🇦 Украины⁣⁣⁣⁣⁣⁣"),
            KeyboardButton(text="🇰🇿 Казaхстана"),
        ],
        [
            KeyboardButton(text="🇧🇾 Белоруссии"),
            KeyboardButton(text="🇦🇺 Австрaлии"),
            KeyboardButton(text="🇺🇸 США⁣⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="🇦🇲 Армении⁣⁣"),
            KeyboardButton(text="🇦🇿 Азербайдж⁣ан⁣а"),
            KeyboardButton(text="🇭🇺 Вeнгрии"),
        ],
        [
            KeyboardButton(text="🇻🇳 Вьетнама⁣⁣"),
            KeyboardButton(text="🇩🇪 Германии⁣⁣"),
            KeyboardButton(text="🇩🇰 Дaнии"),
        ],
        [
            KeyboardButton(text="🇮🇹 Итaлии‏"),
            KeyboardButton(text="🇮🇸 Ислaндии"),
            KeyboardButton(text="🇮🇳 Индии"),
        ],
        [
            KeyboardButton(text="🇨🇦 Канады⁣"),
            KeyboardButton(text="🇰🇬 Kиpгизии"),
            KeyboardButton(text="🇨🇳 К⁣⁣ита⁣⁣я⁣"),
        ],
        [
            KeyboardButton(text="🇱🇻 Лaтвии⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣"),
            KeyboardButton(text="🇲🇩 Молдавия"),
            KeyboardButton(text="🇳🇱 Нидерла⁣нды⁣⁣"),
        ],
        [
            KeyboardButton(text="🇳🇴 Нoрвегии⁣"),
            KeyboardButton(text="🇫🇷 Франции⁣⁣⁣⁣⁣⁣"),
            KeyboardButton(text="🇸🇪 Швeции⁣"),
        ],
        [
            KeyboardButton(text="🇨🇭 Швейцарии⁣⁣⁣"),
            KeyboardButton(text="🇪🇪 Эстонии⁣⁣⁣"),
            KeyboardButton(text="🇰🇷 Южной Кореи"),
        ],
        [
            KeyboardButton(text="🇯🇵 Японии⁣⁣⁣⁣⁣⁣⁣"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)





