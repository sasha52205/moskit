from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#биометрия
bio_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лица")
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)





#Адресс




#Ник
nik_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Дополнительные метoды")
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)


#Транспонт
transport_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Автомобиля"),
        ],
        [
            KeyboardButton(text="Самолета"),
        ],
        [
            KeyboardButton(text="Поезда"),
        ],
        [
            KeyboardButton(text="Судна"),
        ],
        [
            KeyboardButton(text="Грузового контейнера"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)

#Документы
doc_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Юр. лица"),
        ],
        [
          KeyboardButton(text="Физ. лица")
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)

#Домен
domen_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text="Любой"),
        ],
        [
          KeyboardButton(text=".onion")
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)



#Файл
fail_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Определить расширение файла"),
        ],
        [
            KeyboardButton(text="Изображение"),
          KeyboardButton(text="Документ")
        ],
        [
            KeyboardButton(text="DS_STORE"),
          KeyboardButton(text="HAR")
        ],
        [
            KeyboardButton(text="Другое"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)


#wi-fi
wifi_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="SSID — Имя точки доступа"),
        ],
        [
          KeyboardButton(text="BSSID — MAC-адрес")
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)


#серийный номер
sernum_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Техника"),
        ],
        [
            KeyboardButton(text="🔙 Назад"),
            KeyboardButton(text="🔝 Главное Меню"),
        ],
    ],
    resize_keyboard=True
)






