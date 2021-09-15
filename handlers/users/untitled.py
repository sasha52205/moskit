from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from keyboards.default.geo_kb import geo_kb_1, geo_kb_2, geo_kb
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from states.states import Geo




@dp.message_handler(text="Адрес")
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"Какой адрес?", reply_markup=geo_kb)
    await Geo.Q1.set()

@dp.message_handler(text="IP адрес⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по IP адресу\n\n</b>1. <a href="https://github.com/SpiderLabs/HostHunter">HostHunter</a> (t) — обнаружение и извлечение имен хостов из набора целевых IP-адресов\n2. censys.io — находит какие серверы и устройства выставлены в сети\n3. <a href="https://github.com/cyberhubarchive/archive">cyberhubarchive</a> — архив утекших данных, в нем есть IP адреса аккаунтов Skype\n4. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, нужно использовать в облаке если пройти регистрацию\n5. <a href="http://iknowwhatyoudownload.com/">iknowwhatyoudownload</a> — покажет что скачивают в интернете\n6. <a href="https://check.torproject.org/cgi-bin/TorBulkExitList.py">check.torproject.org</a> — найдет список всех выходных узлов Tor за последние 16 часов, которые мог связаться с IP\n7. <a href="https://dnslytics.com/reverse-ip">dnslytics.com</a> — найдет домены\n8. @iptools_robot — бот для быстрого поиска информации о ip адресе, найдет whois, настоящий IP за Cloudflare, порты и многое другое\n9. <a href="https://metrics.torproject.org/exonerator.html">metrics.torproject.org</a> — проверяет использовался ли IP-адрес в качестве узла для передачи трафика в Tor, требуется указать дату\n10. <a href="http://ipinfo.io/map">ipinfo.io</a> — найдет любое число IP адресов на карте\n11. talosintelligence.com — покажет сколько писем было отправлено с адреса и его репутацию\n12. intelx.io — найдет упоминание в файлах из утечек\n13. ⚡️@UniversalSearchBot — даст прямые ссылки на 20+ ресурсов где можно найти историю Whois, домены, адрес и еще 20+ видов данных\n14. <a href="https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%96%D1%83%D1%80%D0%BD%D0%B0%D0%BB%D1%8B?type=&user=&page=%D0%A3%D1%87%D0%B0%D1%81%D1%82%D0%BD%D0%B8%D0%BA%3A1.1.1.1&wpdate=&tagfilter=&wpfilters%5B%5D=newusers">wikipedia.org</a> — поиск в журнале правок, банов, регистрации участников wikipedia, замените <code>1.1.1.1</code> в поле цель\n15. <a href="https://leak-lookup.com/search">leak-lookup.com</a> (r) — покажет на каких сайтах была утечка искомым IP\n\n\n<b>Через URL\n\n</b>https://en.wikipedia.org/wiki/Special:Contributions/IP — найдет пользователя, замените <code>IP</code>, используйте похожую ссылку только на других языках, так как аккаунт на этом может не найтись\nhttps://en.wikipedia.org/wiki/User_talk:/IP — найдет пользователя, замените <code>IP</code>, используйте похожую ссылку только на других языках, так как аккаунт на этом может не найтись')

@dp.message_handler(text="MAC адрес⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по MAC адресу\n\n</b>1. <a href="https://xinit.ru/wifi/">xinit.ru</a> — покажет местоположение Wi-Fi\n2. <a href="https://alexell.ru/network/mac-geo/">alexell.ru</a> — тоже покажет местоположение\n3. @iptools_robot — бот найдет адрес и компанию\n4. <a href="http://wigle.net/search">wigle.net</a> (r) — находит Wi-Fi точку, ее физический адрес и название\n\n\n<b>Поиск через URL\n\n</b>1. https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=00:CC:00:CC:00:CC — найдет координаты точки на карте, замените <code>00:CC:00:CC:00:CC</code> на MAC-адрес')

@dp.message_handler(text="Любой⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по физическому адресу любой страны\n\n1. 3wifi — найдет wifi точки с паролями\n2. kamerka (t) — найдет на карте камеры, устройства интернета вещей, принтеры, твитты, Instagram фото, Flickr и другие открытые устройства\n3. wigle.net — покажет SSID и BSSID Wi-Fi точки\n4. osintcombine.com — найдет Facebook страницы организаций\n5. trendsmap.com — карта трендов в Twitter\n6. omnisci.com — покажет твитты на карте\n7. mattw.io — находит видео на YouTube\n8. windy.com — множество камер с функцией поиска по истории, есть карта\n9. sanstv.ru — найдет фото и твиты, есть фильтр по дате\n10. opencellid.org — вышки сотовой связи, найдет MCC, MNC, LAC, CID\n11. strava.com — сайт показывает где бегают спортсмены\n12. map.snapchat.com — найдет недавние видео из Snapchat\n13. doogal.co.uk — данные из Strava, показывает имена пользователей\n14. udeuschle.de — составит панораму гор\n15. www.whopostedwhat.com — находит фото в Instagram с фильтром по дате\n16. onemilliontweetmap.com — покажет твиты за последние сутки на карте\n17. SnapMap-OSINT (t) — скачает все фото и видео из Snapchat в указанном на карте радиусе\n18. Telegram-Trilateration (t) — показывает точное местоположение пользователей Telegram включивших функцию "люди рядом"\n19. flickr.com — найдет снимки пользователей на карте, выберите место поиска, нажмите "search the map" а потом "go"\n20. pastvu.com — исторические снимки места с 1826 по 2000 годы\n21. photo-map.ru (r) — найдет фото из VK, радиус поиска от 10 метров\n22. app.skylens.io (r) — найдет на карте фото Instagram, YouTube видео, твиты, фото из ВК, минимальный радиус поиска 1 км.\n23. openaltimetry.org — показывает точный рельеф, подберите дату чтобы полоса точек попала на нужное место, выделите область "select region" и сервис даст точки отображающие выбранный рельеф\n24. account.lampyre.io (t) (r) — программа находит координаты групп и пользователей Telegram, фото из VK, Instagram, Flickr, Foursquare, посты из Twitter\n\n\nСпутниковые снимки\n\n1. wikimapia.org — спутниковые снимки Google, Yandex, Bing и Yahoo, есть фильтр зданий по году постройки, по категориям, обозначение объектов которых нету на других картах\n2. livingatlas.arcgis.com — покажет исторические снимки\n3. satellites.pro — есть карты Apple, MapBox, Yandex, Esri и Google\n4. apps.sentinel-hub.com (r) — база почти ежедневных снимков со спутника, можно делать таймлапс\n5. zoom.earth — есть высококачественные изображения для этого выберите базовую карту, есть пожары, штормы, ветер и история этих данных по дате\n6. orbtwz.users.earthengine.app — найдет и отметит изменения на спутниковых снимках в указанную дату\n\n\nВидеонаблюдение\n\n1. windy.com — есть история записей\n2. world-cam.ru — камеры в реальном времени \n\n\nТранспорт\n\n1. www.vesselfinder.com — покажет все судна на карте\n2. globe.adsbexchange.com — самолеты и вертолеты с историей передвижений\n\n\nПросмотр улиц\n\n1. Google — просмотр в 360 градусов почти во все странах\n2. Mapillary — данные загружаются пользователями, не всегда есть обзор в 360 градусов\n3. kartaview.org — данные загружаются пользователями, нету панорам\n4. railcabrides.com — видео из кабины поезда, нет крупных городов\n5. 360cities.net — панорамы\n\n\nИнструменты\n\n1. app.measuremaponline.com (r) — вычисляет площадь и периметр нужной области на карте')
    
    
@dp.message_handler(text="🇷🇺 России⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    

    
@dp.message_handler(text="🇺🇦 Украины⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по физическому адресу Украины\n\n</b>1. spravnik.com — найдет номер телефона, ФИО\n2. liveuamap.com — отмечены места из новостей с происшествиями, преступностью, катаклизмами и еще 40 видов событий\n3. /physical_address — список ресурсов для поиска по физическому адресу любой страны\n\n\n<b>Транспорт\n\n</b>1. www.eway.in.ua — общественный транспорт на карте в реальном времени\n\n\n<b>Просмотр улиц\n\n</b>1. <a href="http://yandex.ru/maps/">Yandex</a> —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей')


@dp.message_handler(text="🇧🇾 Бeларусь",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по физическому адресу Беларуси\n\n1</b>. belarus.liveuamap.com — отмечены места из новостей с происшествиями, преступностью, катаклизмами и еще 40 видов событий\n2. /physical_address — список ресурсов для поиска по физическому адресу любой страны\n\n\n<b>Просмотр улиц\n\n</b>1. <a href="http://yandex.ru/maps/">Yandex</a> —  просмотр в 360 градусов, есть доступ к истории снимков, дополнительные снимки от пользователей')
    
@dp.message_handler(text="🇧🇷 Брaзилии",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇧🇪 Бельгии⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇧🇬 Болгарии⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇬🇧 Великобритании⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇭🇺 Венгрии",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇩🇪 Гeрмании",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇬🇷 Греции",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇩🇰 Дании⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇮🇳 Индии⁣⁣⁣⁣⁣⁣⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇮🇪 Ирландии⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇮🇸 Исландии",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇮🇹 Италии⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇨🇦 Канады",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇨🇾 Кипра⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇰🇬 Kиргизии",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇨🇳 Китaя",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇱🇻 Лaтвии⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇱🇹 Литвы⁣",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇱🇺 Люксeмбурга",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇲🇹 Мальты",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

    
@dp.message_handler(text="Еще ➜",state=Geo.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>ФИО гражданина какой страны?\n</b>\nСтр. 2 из 2')
    await Geo.Q2.set()
    
@dp.message_handler(text="🇲🇩 Молдовы⁣⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇳🇱 Нидерлaндов",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

    
@dp.message_handler(text="🇳🇴 Норвегии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇳🇿 Новой Зеландии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇵🇱 Польши⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇵🇹 Португалии",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇷🇴 Румынии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇸🇰 Словакии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇸🇮 Словении⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇺🇸 США⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇹🇷 Турции",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇹🇯 Таджикистанa",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇺🇿 Узбекистана",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇫🇷 Франции⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')
    
@dp.message_handler(text="🇫🇮 Финляндии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="🇭🇷 Хорватии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="🇨🇿 Чехии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="🇨🇭 Швейцарии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="🇸🇪 Швеции⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="🇪🇪 Эстoнии⁣",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="🇰🇷 Южнoй Кореи",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

@dp.message_handler(text="🇯🇵 Японии",state=Geo.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('')

