from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from keyboards.default.menu import phone_countryes
from loader import dp
from keyboards.default.dop_kb import dop_kb
from aiogram.dispatcher import filters

from aiogram.dispatcher import FSMContext


from loader import dp
from states.states import Phone




@dp.message_handler(text="Номер телефона")
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer(f"Номер телефона какой страны?", reply_markup=phone_countryes)
    await Phone.phone.set()


@dp.message_handler(text="Любой⁣⁣⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer(f"Поиск по номеру телефона любой страны\n\n"
                         f"1. @SafeCallsBot — бесплатные анонимные звонки на любой номер телефона с подменой Caller ID\n"
                         f"2. PhoneInfoga — определят тип номера, дает дорки Google, определяет город\n"
                         f"3. numberway.com — найдет телефонный справочник\n"
                         f"4. account.lampyre.io (t) (r) — программа выполняет поиск аккаунтов, паролей и прочее\n"
                         f"5. @usersbox_bot — найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер\n"
                         f"6. @GetFb_bot — находит Facebook\n"
                         f"7. globfone.com — бесплатные анонимные звонки на любой номер телефона\n"
                         f"8. smsc.ru — статус активности телефона\n"
                         f"9. Ignorant (t) — находит к какому сайту привязан номер телефона\n"
                         f"10. @clerkinfobot — показывает как записан номер телефона в контактах, берет данные из приложения get contact"
                         f"11. FuckFacebook — найдет аккаунт Facebook в глобальной утечке\n"
                         f"12. tools.whoisxmlapi.com — выявляет домен зарегистрированный на номер телефона\n"
                         f"13. www.vedbex.com — найдет аккаунт Skype\n"
                         f"14. www.skypli.com — выдает аккаунт Skype\n"
                         f"15. aihitdata.com — найдет компании по всему миру где указан телефон, откройте вкладку More Fields\n"
                         f"16. effectgroup.io (r) — найдет социальные сети, ФИО, email, адрес проживания, компании и прочее, иногда нужен VPN, 1 полный отчет на аккаунт\n"
                         f"17. sync.me (r) — покажет имя из контактов и уровень спама\n\n\n"
                         f"Дополнительный методы\n\n"
                         f"1. Оставьте только цифры у номера телефона и добавьте к нему @yandex.ru а потом используйте методы для Яндекс почты\n\n\n"
                         f"Восстановление доступа\n\n"
                         f"1. ICQ\n"
                         f"2. Yahoo\n"
                         f"3. Adobe\n"
                         f"4. Steam\n"
                         f"5. Xiaomi\n"
                         f"6. Twitter\n"
                         f"7. VK.com\n"
                         f"8. Facebook\n"
                         f"9. Microsoft\n"
                         f"10. Instagram\n"
                         f"11. Cloud.Huawei.com")


@dp.message_handler(text="🇷🇺 России",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"Поиск по номеру телефона России\n\n"
                         f"1. @av100_bot (r) – делает отчет где есть данные из социальных сетей, недвижимости, автомобилей, объявлений и телефонных книжек. Нужно пригласить другой аккаунт для отчета\n"
                         f"2. getcontact.com (r) — выдает информацию о том как записан номер в контактах\n"
                         f"3. @get_kontakt_bot — ищет как записан номер в контактах, большая база контактов\n"
                         f"4. truecaller.com (r) — телефонная книга, ищет имя и оператора телефона\n"
                         f"5. avinfo.guru (r) — проверка телефона владельца авто, иногда нужен VPN\n"
                         f"6. spravnik.com — поиск по городскому номеру телефона, найдет ФИО и адрес\n"
                         f"7. ⚡️@UniversalSearchBot — находит город, первую букву улицы, номера дома или квартиры, аккаунт Skype\n"
                         f"8. @gdepochtabot — покажет на каких сайтах утекли пароли\n"
                         f"9. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито\n"
                         f"10. @smart_search_3_bot — находит ФИО, email, объявemail\n"
                         f"11. @The_New_Get_Contact_Bot — найдет как записан телефон в контактах\n"
                         f"12. @phone_avito_bot — дает ссылку на аккаунт Авито с подробной информацией\n"
                         f"13. www.list-org.com — найдет организацию\n"
                         f"14. /phone — список ресурсов для поиска по номеру телефона любой страны\n")



@dp.message_handler(text="🇺🇦 Украины⁣⁣⁣⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer(f"Поиск по номеру телефона Украины\\\n"
                         f"1. @info_baza_bot — поиск в базе данных\n"
                         f"2. @get_kontakt_bot — найдет как записан номер в контактах\n"
                         f"3. spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес\n"
                         f"4. @SEARCH1UA_bot — как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки\n"
                         f"5. @Quick_OSINT_bot — найдет оператора, email, адрес, как записан в контактах и многое другое\n"
                         f"6. searchyellowdirectory.com — определит к какой области Украины принадлежит номер телефона\n"
                         f"7. @Info_in_bot — найдет ФИО, доступ дает не каждому, меняйте аккаунты\n"
                         f"8. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито\n"
                         f"9. @smart_search_3_bot — находит ФИО, email, объявления\n"
                         f"10. @SEARCHUA_bot — выдает досье где есть паспорт, адрес проживания, ФИО, автомобили, родственники, email, номера телефонов и много другого\n"
                         f"11. rol-x.ru — найдет объявления на Olx\n"
                         f"12. @The_New_Get_Contact_Bot — найдет как записан телефон в контактах\n"
                         f"13. @gdepochtabot — покажет на каких сайтах утекли пароли\n"
                         f"14. /phone — список ресурсов для поиска по номеру телефона любой страны\n")



@dp.message_handler(text="🇰🇿 Казaхстана",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer("Для номера телефона Казахстана\n\n1. @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact\n2. truecaller.com (r) — телефонная книга, найдет имя и оператора телефона\n3. fa-fa.kz — найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд\n4. spravochnik109.link — поиск по городскому номеру телефона, найдет ФИО и адрес\n5. @get_kolesa_bot — найдет объявления на колеса.кз\n6. account.lampyre.io (t) (r) — программа выполняет поиск аккаунтов, паролей и многих других данных\n7. @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail\n8. @Quick_OSINT_bot — найдет оператора, email, адрес, как записан в контактах и многое другое\n9. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито\n10. @smart_search_3_bot — находит ФИО, email, объявления\n11. @The_New_Get_Contact_Bot — найдет как записан телефон в контактах\n12. /phone — список ресурсов для поиска по номеру телефона любой страны")


@dp.message_handler(text="🇧🇾 Белоруссии",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Белоруссии\n\n</b>1. @get_kontakt_bot — найдет как записан номер в контактах, дает результаты что и getcontact\n2. <a href="https://spravochnik109.link/byelarus">spravochnik109.link</a> — поиск по городскому номеру телефона, найдет ФИО и адрес\n3. @get_caller_bot — поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail\n4. @Quick_OSINT_bot — найдет оператора, email, адрес, как записан в контактах и многое другое\n5. <a href="https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm">m.ok.ru</a> — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито\n6. @smart_search_3_bot — находит ФИО, email, объявления\n7. /phone — список ресурсов для поиска по номеру телефона любой страны')


@dp.message_handler(text="🇦🇺 Австрaлии",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer("<b>Для номера телефона Австралии\n\n</b>1. personlookup.com.au — найдет имя и адрес\n2. /phone — список ресурсов для поиска по номеру телефона любой страны")



@dp.message_handler(text="🇺🇸 США⁣⁣⁣⁣⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message,state: FSMContext):
    await message.answer("Номер телефона США известен полностью?")


@dp.message_handler(text="🇦🇲 Армении⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Армении\n\n</b>1. @The_New_Get_Contact_Bot — найдет как записан телефон в контактах\n2. @ArcNET_osint_bot — найдет как записан телефон в контактах, полное имя, паспорт, адрес прописки\n3. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
@dp.message_handler(text="🇦🇿 Азербайдж⁣ан⁣а",state=Phone.phone)
async def get_phone_menu1(message: Message, state: FSMContext):
    
    await message.answer('Поиск по номеру телефона\n\n1. @The_New_Get_Contact_Bot — найдет как записан телефон в контактах\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
@dp.message_handler(text="🇭🇺 Вeнгрии",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Венгрии\n\n</b>1. <a href="https://www.telekom.hu/lakossagi/tudakozo">telekom.hu</a> — найдет ФИО и адрес проживания\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')
    

@dp.message_handler(text="🇻🇳 Вьетнама⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Вьетнама\n\n</b>1. /phone — список ресурсов для поиска по номеру телефона любой страны\n\n\n<b>Дополнительный методы\n\n</b>1. Установите приложение <a href="https://play.google.com/store/apps/details?id=com.zing.zalo">zalo</a> и через восстановление пароля найдется имя и фото аккаунта')
    
    
@dp.message_handler(text="🇩🇪 Германии⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Германии\n\n</b>1. <a href="https://www.herold.at/telefonbuch/">www.herold.at</a> — найдет ФИО и адрес владельца \n2. www.telefonabc.at — выдаст ФИО\n3. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
@dp.message_handler(text="🇩🇰 Дaнии",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Дании\n\n</b>1. <a href="https://statstidende.dk/messages">statstidende.dk</a> — поиск в юридических документах, найдет данные о смене жительства, некрологи много всего полезного\n2. <a href="https://datacvr.virk.dk/data/">datacvr.virk.dk</a> — поиск в сведениях о зарегистрированных предпринимателях и компаниях\n3. <a href="https://www.krak.dk/">krak.dk</a> —найдет ФИО, местоположение на карте и фото дома.\n4. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
    
@dp.message_handler(text="🇮🇹 Итaлии‏",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Италии\n\n</b>1. <a href="https://www.paginebianche.it/">paginebianche.it</a> — найдет ФИО и адрес\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')
    

@dp.message_handler(text="🇮🇸 Ислaндии",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Исландии\n\n</b>1. ja.is — найдет данные людей и компаний\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
    
@dp.message_handler(text="🇮🇳 Индии",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Индии\n\n</b>1. <a href="https://play.google.com/store/apps/details?id=com.app.airit">Mi Airit</a> (a) — популярное Android приложении в Индии, после \n2. <a href="http://www.indiaonapage.com/mobilenumbertrace">indiaonapage.com</a> — покажет оператора связи и возможный город\n3. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
@dp.message_handler(text="🇨🇦 Канады⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Канады\n\n</b>1. <a href="https://www.canada411.ca/search/">www.canada411.ca</a> — возраст, ФИО, адрес проживания и другое\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')
    

@dp.message_handler(text="🇰🇬 Kиpгизии",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Киргизии\n\n</b>1. <a href="https://m.ok.ru/dk?st.cmd=accountRecoverFeedbackForm">m.ok.ru</a> — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
    
@dp.message_handler(text="🇨🇳 К⁣⁣ита⁣⁣я⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Китая\n\n1</b>. @boluosgkbot — находит ID аккаунта QQ\n2. @coolsgk_bot — дает ID аккаунта QQ, Weibo\n3. @sgk123bot — ищет ID аккаунта QQ, Weibo\n4. /phone — список ресурсов для поиска по номеру телефона любой страны')
    
@dp.message_handler(text="🇱🇻 Лaтвии⁣⁣⁣⁣⁣⁣⁣⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Латвии\n\n</b>1. <a href="https://spravochnik109.link/latviya">spravochnik109.link</a> — поиск по городскому номеру телефона, найдет ФИО и адрес\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇲🇩 Молдавия",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Молдавии\n\n</b>1. <a href="https://spravochnik109.link/moldova">spravochnik109.link</a> — поиск по городскому номеру телефона, найдет ФИО и адрес\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇳🇱 Нидерла⁣нды⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру Нидерландов\n\n</b>1. <a href="https://crdc.be/crdcNLI/BrowserDefault.aspx?tabid=265">crdc.be</a> — найдет текущего оператора связи\n2. <a href="https://www.acm.nl/nl/onderwerpen/telecommunicatie/telefoonnummers/nummers-doorzoeken">acm.nl</a> — дает название компании владеющая номером\n3. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇳🇴 Нoрвегии⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Норвегии\n\n</b>1. gulesider.no — даст ФИО, местоположение на карте и фото дома\n2. <a href="https://datacvr.virk.dk/data/">datacvr.virk.dk</a> — поиск в сведениях о зарегистрированных предпринимателях и компаниях\n3. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇫🇷 Франции⁣⁣⁣⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Франции\n\n</b>1. <a href="https://www.118712.fr/annuaire-inverse-gratuit.html">www.118712.fr</a> — имя и адрес владельца номера телефона\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇸🇪 Швeции⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Швеции\n\n</b>1. <a href="https://www.eniro.se/">eniro.se</a> — найдет ФИО, местоположение на карте и фото дома\n2. <a href="https://datacvr.virk.dk/data/">datacvr.virk.dk</a> — поиск в сведениях о зарегистрированных предпринимателях и компаниях\n3. <a href="https://www.upplysning.se/">upplysning.se</a> — контактные данные людей и компаний\n4. mrkoll.se — найдет дату рождения, адрес, ФИО, соседей, номер социального страхования, номера телефонов, корпоративное участие, примерный доход, история изменений ФИО\n5. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇨🇭 Швейцарии⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Швейцарии</b>⁣⁣\n\n1. <a href="https://www.local.ch/en/tel">www.local.ch</a> — поиск в реестре бизнесов, найдет сайт, адрес, фото\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇪🇪 Эстонии⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона</b> <b>Эстонии\n\n</b>1. <a href="https://www.teatmik.ee/en/advancedsearch/contact">teatmik.ee</a> — поиск в базе организаций, ищет номер в контактах\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇰🇷 Южной Кореи",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Южной Кореи\n\n</b>1. 114.co.kr — покажет адрес компании\n2. kakaocorp.com (r) — создайте контакт и найдёте аккаунт в приложении\n3. /phone — список ресурсов для поиска по номеру телефона любой страны')

@dp.message_handler(text="🇯🇵 Японии⁣⁣⁣⁣⁣⁣⁣",state=Phone.phone)
async def get_phone_menu(message: Message, state: FSMContext ):
    await message.answer('<b>Поиск по номеру телефона Японии\n\n</b>1. www.jpnumber.com — найдет отзывы, провайдера, область, возможно ФИО владельца\n2. /phone — список ресурсов для поиска по номеру телефона любой страны')

