from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from keyboards.default.tools_kb import tools_kb
from aiogram.dispatcher import filters



@dp.message_handler(text="🛠 Инструменты")
async def get_phone_menu(message: Message):
    await message.answer(f"🛠 Инструменты", reply_markup=tools_kb)
    

@dp.message_handler(text="Виртуальный номер телефона")
async def get_phone_menu(message: Message):
    await message.answer(f"Бесплатные телефонные номера\n\n\n"
                         f"Приложения\\n"
                         f"1. SafeUM (r) — android, дает номер Литвы, не принимает СМС\n"
                         f"2. TextNow (r) — дает номер телефона США, принимает СМС и голосовую почту, для регистрации принимает только голосовую почту, подтверждайте почту до получения номера телефона\n\n"
                         f"Сайты\n\n"
                         f"1. onlinesim.ru — возможно получить СМС и зарегистрировать аккаунт\n"
                         f"2. www.z-sms.com — возможно получить СМС на номера стран Азии и Европы\n"
                         f"3. www.zusms.com — возможно получить СМС на номера Китая и Гонконга\n"
                         f"4. receive-smss.com — показывает СМС, дает номера СНГ и США\n"
                         )
    
    

@dp.message_handler(text="Бесплатные почтовые адреса⁣⁣⁣")
async def get_phone_menu(message: Message):
    await message.answer(f"Анонимные и бесплатные почтовые адреса\n\n\n"
                         f"1. @etlgr_bot — прием писем, без регистрации, можно зарезервировать более 100 адресов\n"
                         f"2. @TempGMailBot — прием почты с адресом gmail.com\n"
                         f"3. emkei.cz — отправляет письма с заданного вами email адреса\n"
                         f"4. gmailnator.com — прием почты, дает email gmail.com")
    

@dp.message_handler(text="Визуализация данных")
async def get_phone_menu(message: Message):
    await message.answer(f"Программы для визуализации найденных данных\n\n\n"
                         f"1. mindomo.com (r) — онлайн составление карты взаимодействия данных между собой в виде гкарты\n"
                         f"2. time.graphics — таймлаин, можно связать файл, ссылку, текст с временем")
    



@dp.message_handler(text="Расширения")
async def get_phone_menu(message: Message):
    await message.answer(f"Расширения для браузера\n\n\n"
                         f"1. gobackintime — позволяет просматривать кэшированную версию веб-страницы через разные сервисы\n"
                         f"2. mitaka — поиск/сканирование сайта через контекстное меню\n"
                         f"3. IP Whois — whois, сколько посетителей посещают, отзывы о репутации, проверка на вирусы, Alexa\n"
                         f"4. Wayback Machine — быстро сохраняйте веб-страницы в интернет архиве\n"
                         f"5. Sputnik — быстрый и простой поиск IP-адресов, доменов, файловых хешей и URL-адресов\n"
                         f"6. invid — анализ видео на хостингах\n"
                         f"7. HackerTarget — Быстрый доступ к IP, DNS и сетевым инструментам. Проверьте DNS, Whois, ASN, Traceroute, Ping и многое другое. Инструменты для технических операторов.\n"
                         f"8. reveye — реверс поиск фото по 5 сайтам\n"
                         f"9. Web Archives — заархивированные и кэшированные версии веб-страниц в более чем 10 поисковых системах, таких как Wayback Machine, Archive.is и Google\n"
                         f"10. Map Switcher — быстрое переключение между онлайн-картографическими сервисами\n"
                         f"11. Instant Data Scraper — парсит любую страницу в CSV и Excel\n")
    