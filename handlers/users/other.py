from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from keyboards.default.other_kb import bio_kb,nik_kb,  transport_kb, doc_kb,  fail_kb, wifi_kb, sernum_kb, domen_kb
from aiogram.dispatcher import filters

from keyboards.default.dop_kb import nik_dop_kb, dop_kb, domen_dop_kb, domen_dop2_kb


from aiogram.dispatcher import FSMContext



from states.states import Domen
#Биометрия
@dp.message_handler(text="Биометрия")
async def get_phone_menu(message: Message):
    await message.answer(f"Биометрия чего?", reply_markup=bio_kb)
    
@dp.message_handler(text="Лица")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по фото с лицом\n\n"

f"1. Findclone.ru (r) — найдет профиль VK\n"
f"2. @av100_bot — найдет аккаунты в ВК, просто пришли ему фото с лицом\n"
f"3. pimeyes.com — индексирует фото с сайтов, не точен, ограниченные возможности\n"
f"4. search4faces.com — найдет профиль VK, OK, TikTok и Clubhouse, не точен\n"
f"5. @smart_search_3_bot — находит страницу в ВК, бесплатный период несколько дней после старта бота\n"
f"6. azure.microsoft.com — соотнесение лиц, определит вероятность того, что на двух разных изображениях изображен один и тот же человек, и выдаст оценку достоверности\n"
f"7. @facematch_bot (r) — найдет фото с таким же лицом взятых из сайтов kipyat.com и ppz.kz\n"
f"8. news.myseldon.com — не точен, ищет в фото из СМИ\n"
f"9. vk.watch — находит аккаунты ВКонтакте с похожими лицами, не точен\n\n\n"


f"Поисковики\n\n"

f"1. Yandex\n"
f"2. Google\n"
f"3. Bing\n"
f"4. Mail.ru\n"
f"5. image.baidu.com\n"
f"6. image.so.com\n\n"


f"По видео с лицом\n\n"

f"1. scanner.deepware.ai — выявляет дипфейк"
        
        )




#Адресс
@dp.message_handler(text="Адрес")
async def get_phone_menu(message: Message):
    await message.answer(f"Какой адрес?", reply_markup=adress_kb) 
    
    
    
    
    
#Ник
@dp.message_handler(text="Ник")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по нику\n\n"
    f"1. Maigret (t) — найдет аккаунты с таким же ником среди 2000+ сайтов⚡️\n"
    f"2. Maigrett_osint_bot — найдет аккаунты с таким ником среди 2000+ сайтов, дает самый точный результат\n"
    f"3. namecheckup.com — найдет искомый ник на сайтах\n"
    f"4. instantusername.com — найдет искомый ник на сайтах\n"
    f"5. suip.biz — найдет искомый ник на 300+ сайтах, работает очень медленно, дождитесь ответа\n."
    f"6. namechk.com — найдет искомый ник на сайтах и в доменах\n"
    f"7. sherlock (t) — найдет искомый ник на сайтах\n"
    f"8. whatsmyname.app — найдет искомый ник на сайтах\n"
    f"9. boardreader.com — найдет искомый ник на форумах\n"
    f"10. leakedsource.ru — найдет искомый ник на сайтах\n"
    f"11. yasni.com — автоматический поиск в интернете\n"
    f"12. social-searcher.com — найдет упоминания в соц. сетях и на сайтах\n"
    f"13. socialmention.com — найдет упоминания ника\n"
    f"14. @StealDetectorBOT — покажет часть утекшего пароляником"
 f"15. @SovaAppBot — найдет аккаунты с похожим ником среди 500+ сайтов\n"
 f"16. account.lampyre.io (t) (r) — программа выполняет поиск социальных сетей, паролей и прочих аккаунтов\n"
 f"17. mailcat (t) — перебирает почтовые сервисы чтобы найти действительные email адреса\n\n\n"
 
 f"Восстановление доступа\n\n"
 f"1. Twitter\n"
 f"2. Microsoft\n"
 f"3. Instagram", reply_markup=dop_kb)     
 
 
@dp.message_handler(text='Дополнительныe методы⁣⁣⁣⁣⁣⁣')
async def get_phone_menu(message: Message):
    await message.answer(f"Дополнительные метoды", reply_markup=nik_dop_kb) 
 
  
@dp.message_handler(text='Найти Stackoverflow аккаунт и другое⁣⁣⁣⁣⁣⁣')
async def get_phone_menu(message: Message):
    await message.answer("<b>Как найти Stackoverlow аккаунт</b>\n\n<i>Метод позволяет найти ник, адрес, сайт и описание аккаунта на Stackoverflow\n\n</i>[1] Откройте URL https://data.stackexchange.com/stackoverflow/query/new\n[2] В большом поле для ввода вставьте этот код:\n<code>select Id [User Link], DisplayName, WebsiteUrl, Location, AboutMe\nfrom Users\nwhere DisplayName like 'USERNAME'\norder by CreationDate desc\n</code>[3] В коде измените <code>USERNAME</code> на ник, не удаляя кавычки\n[4] Подтвердите recapcha и нажмите на кнопку Run Query\nЕсли в полученной таблице нет результатов, то такого ника нет, можно попробовать прибавить к нику в конце знак <code>%</code> и запустить еще раз\n\nМожно попробовать еще такой код\n<code>select Id [User Link], DisplayName, WebsiteUrl, Location, AboutMe\nfrom Users\nwhere WebsiteUrl like 'USERNAME'\norder by CreationDate desc\n\n</code>Поиск будет по ссылкам в аккаунтах которые указываются как личный сайт") 
 
 
 
 
 
#Транспорт
@dp.message_handler(text="Транспорт")
async def get_phone_menu(message: Message):
    await message.answer(f"Данные какого транспорта?", reply_markup=transport_kb) 
    
    
 
 #Документы
@dp.message_handler(text="Документы")
async def get_phone_menu(message: Message):
    await message.answer(f"Чьи документы?", reply_markup=doc_kb) 
    
    
 
 #Домен
@dp.message_handler(text="Домен")
async def get_phone_menu(message: Message, state=FSMContext):
    await message.answer(f"Какой домен?", reply_markup=domen_kb)
    await Domen.domen.set()
    
    
@dp.message_handler(text='Любой', state=Domen.domen)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"Поиск по любому домену\n\n1. xinit.ru — найдет whois, DNS-записи, даст ссылки на поисковые ресурсы\n2. hunter.io — дает email адреса\n3. @WhoisDomBot — узнайте базовую информацию о домене\n4. riskiq.com (r) — автоматизированный поиск по всем фронтам\n5. Knock Subdomain Scan (t) — находит под домены и FTP\n6. builtwith.com — технологический профиль сайта, взаимосвязи между сайтами\n7. crimeflare.org — определяет настоящий IP адрес сайта скрытый за CloudFlare\n8. cyber-hub.net — распознаватель cloudflare, статус DNS, перебор под доменов и многое другое\n9. suip.biz — найдет поддомены\n10. urlscan.io — сервис для сканирования и анализа сайтов\n11. dnsdumpster.com — обнаруживает хосты связанные с доменом\n12. censys.io — находит какие серверы и устройства выставлены в сети\n13. virustotal.com — служба пассивного DNS, поиск под доменов, найдет whois и историю сертификатов SSL\n14. atsameip.intercode.ca — одинаковые IP у сайта, можно узнать под домены\n15. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию\n16. dirhunt (t) — поиск директорий сайта без брута\n17. Amass (t) — сетевое картирование поверхностей атаки и обнаружение внешних ресурсов с использованием методов сбора информации с открытым исходным кодом и активных методов разведки\n18. Photon (t) — найдет на сайте файлы, секретные ключи, JS файлы, URL с параметрами \n19. spyse.com — поиск поддоменов \n20. www.cookieserve.com — анализ cookies сайта, покажет какому сайту принадлежат\n21. dnslytics.com — вытаскивает трекеры из сайта\n22. domainwat.ch — может искать информацию такую как имя регистранта, адрес, номер телефона, адрес электронной почты из информации WHOIS и историю изменений\n23. findomain (t) — найдет под домены\n24. shodan.io — найдет IP адреса и сайты с упоминанием искомого сайта\n25. phonebook.cz — найдет email, под домены, директории сайта\n26. visualsitemapper.com — визуализация карты сайта одним графиком\n27. @iptools_robot — найдет whois, настоящий IP за Cloudflare, порты и многое другое\n28. dorks.faisalahmed.me — составляет дорки для Google и Яндекс\n29. synapsint.com — хорошо ищет поддомены \n30. analyzeid.com — находит на странице идентификаторы аналитики и по ним ищет другие сайты\n31. FavFreak (t) — находит все сайты схожим favicon\n32. completedns.com — история DNS\n33. pidrila (t) — находит директории сайта\n34. osint.sh — поддомены, история DNS, сканер NMAP и много другого\n35. mmhdan.herokuapp.com — вычислит хеш значка сайта и даст ссылки на ресурсы где можно найти похожие сайты с одинаковыми значками\n36. o365chk (t) — проверит наличие у сайта Microsoft Office365, выдаст email, облачное имя и ссылку для в хода в офис\n37. pagexray.fouanalytics.com — найдет к каким сайтам делаются запросы для трекинга и аналитики, делает скриншот сайта\n38. metagoofil (t) — найдет метаданные во всех документах на сайте\n39. www.email-format.com — даст email, дату их обнаружения и источник\n40. tools.whoisxmlapi.com — найдет всю историю изменений whois домена\n41. www.link-assistant.com — найдет источники упоминания домена и их анализ\n42. talosintelligence.com — покажет сколько писем было отправлено с домена и его репутацию\n43. account.lampyre.io (t) (r) — программа выполняет поиск малварей, под доменов, файлов, компании и их работников, whois, email адреса\n44. leak-lookup.com (r) — покажет на каких сайтах была утечка с искомым доменом\n45. ⚡️@UniversalSearchBot — даст прямые ссылки на 50+ ресурсов где есть история Whois, IP, DNS, Nameserver, сертификаты, трекеры, похожие домены, контакты, архивы, дорки и прочее", reply_markup=dop_kb) 
    await message.answer('<b>Поиск через URL\n\n</b>1. https://www.reddit.com/search?q=site:example.com&restrict_sr=&sort=relevance&t=all#date=0472111827&h=1 — покажет где на reddit был упомянут сайт, замените <code>example.com\n</code>2. api.hackertarget.com/pagelinks/?q=http://example.com — все ссылки на странице сайта, замените <code>example.com\n</code>3. https://psbdmp.ws/api/search/domain/example.com — упоминания в утечках на Pastebin, замените <code>example.com\n</code>4. https://web.archive.org/web/*/example.com/* — замените <code>example.com</code> на домен или URL чтобы узнать все ссылки что сохранил архив Wayback Machine\n\n\n<b>Архив\n\n</b>1. web.archive.org — показывает сохранённые копии страниц, исходный код, все директории сайта, статистику и много другого\n2. cachedview.com — найдет копию сайта из кэша Google\n3. oldweb.today —  найдет исторические версии сайтов, можно выбрать вид браузера и дату\n4. arquivo.pt — есть расширенный поиск по сайту\n5. archive.md — помимо HTML версии архивирует скриншот сайта\n6. <a href="https://trove.nla.gov.au/search/category/websites">trove.nla.gov.au</a> — найдет копию страницы, откройте расширенный поиск и укажите домен, можно искать в архиве страниц по ключевому слову\n\n\n<b>Парсеры\n\n</b>1. <a href="https://github.com/jsvine/waybackpack">waybackpack</a> (t) — загружает весь архив Wayback Machine\n2. <a href="https://archivarix.com/en/">archivarix.com</a> — восстонавливает полную копию сайта из веб-архива на определенную дату, до 200 файлов бесплатно')
    await Domen.any.set()
    
    
@dp.message_handler(text='Дополнительныe методы⁣⁣⁣⁣⁣⁣', state=Domen.any)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"Дополни⁣тельные⁣ методы", reply_markup=domen_dop_kb) 
    
    
@dp.message_handler(text='До⁣рки⁣⁣⁣⁣⁣⁣⁣',state='*')
async def get_phone_menu(message: Message):
    await message.answer('<b>Поисковые операторы для поиска по домену\n\n</b>Операторы поиска Google и Яндекс — это символы и слова, с помощью которых можно уточнить и сузить поиск. Они бывают простыми и сложными и могут комбинироваться друг с другом. Некоторые поисковые операторы Google совпадают с теми, что используются в Яндекс, а некоторые работают только для конкретного поисковика\n\n\n<b>Дорки для Google\n\n</b>Замените <code>site.com</code> на домен\n\n1. <code>site:*.site.com\n\n</code>2. <code>cache:site.com\n\n</code>3. <code>inurl:site.com\n\n</code>4. <code>site:site.com ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv\n\n</code>5. <code>site:site.com intitle:index.of\n\n</code>6. <code>site:site.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env\n\n</code>7. <code>site:site.com ext:sql | ext:dbf | ext:mdb\n\n</code>8. <code>site:site.com ext:log\n\n</code>9. <code>site:site.com ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup\n\n</code>10. <code>site:site.com inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth\n\n</code>11. <code>site:site.com intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"\n\n</code>12. <code>site:site.com "PHP Parse error" | "PHP Warning" | "PHP Error"\n\n</code>13. <code>site:site.com ext:php intitle:phpinfo "published by the PHP Group"\n\n</code>14. <code>site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com "site.com"\n\n</code>15. <code>site:github.com | site:gitlab.com "site.com"\n\n</code>16. <code>site:site.com inurl:signup | inurl:register | intitle:Signup</code>') 
    
    
 
#Домен
@dp.message_handler(text='.onion', state=Domen.domen)
async def get_phone_menu(message: Message, state=FSMContext):
    await message.answer('<b>Поиск по домену с .onion\n\n</b>1. darktracer.io — находит настоящий IP адрес\n2. <a href="https://github.com/enemy-submarine/pidrila">pidrila</a> (t) — выявляет директории сайта\n3. torwhois.com — показывает открытые порты, директории, PGP ключи, файлы в директориях и многое другое\n\n\n<b>Поиск через URL\n\n</b>1. https://osint.party/api/onion/DOMAIN — найдет метаданные сайта, замените <code>DOMAIN</code> на адрес сайта без .onion', reply_markup=domen_dop2_kb)
    await Domen.any.set()
    

    
@dp.message_handler(text='Найти сервера в клирнете⁣⁣⁣⁣⁣⁣', state=Domen.any)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer("<b>Как найти сервер сайта на onion\n\n</b>https://chaos.institute/content/images/2021/03/flow.svg — схема с методами поиска") 
    

    
    



#Файл
@dp.message_handler(text="Файл")
async def get_phone_menu(message: Message):
    await message.answer(f"К какому формату относится расширение файла?", reply_markup=fail_kb)
    
@dp.message_handler(text="Определить расширение файла")
async def get_phone_menu(message: Message):
    await message.answer(f"Инструменты определяющие расширение файла\n\n\n"
                         f"1. toolsley.com — определяет тип файла\n"
                         f"2. www.aconvert.com — определяет тип файла")

@dp.message_handler(text="Изображение")
async def get_phone_menu(message: Message):
    await message.answer(f"Для файла формата изображение\n\n\n"
                         f"1. metapicz.com — покажет EXIF\n"
                         f"2. stolencamerafinder.com — определит EXIF и по этим данным найдет какие еще фото были сделаны этим устройством\n"
                         f"3. exif.regex.info — извлекает META-данные\n"
                         f"4. cameratrace.com — определит EXIF и по этим данным найдет какие еще фото были сделаны этим устройством\n"
                         f"5. @mediainforobot — извлекает EXIF\n"
                         f"6. 29a.ch —  фото-форензика, анализ изображения на изменения\n"
                         f"7. stylesuxx.github.io — декодирует скрытое сообщение в изображении\n"
                         f"8. Depix (t) — депикселизирует текст на картинке\n"
                         f"9. www.focusmagic.com (t) — восстановит детали и резкость размытых фотографий\n"
                         f"10. www.forensicdots.de — ищет на скане документа желтые точки являющиеся уникальным идентификатором принтера\n"
                         f"11. diffchecker.com — помогает найти различия двух картинок\n"
                         f"12. compress-or-die.com — показывает ICC_Profile, в нем можно по скриншоту на Mac узнать дату последнего обновления системы, есть exif и таблица квантования яркости\n"
                         f"Поиск по картинке\n"
                         f"1. Yandex\n"
                         f"2. Google — открывать на ПК\n"
                         f"3. Bing\n"
                         f"4. Mail.ru\n"
                         f"5. searchbyimage.app — находит товары в многих интернет-магазинах\n"
                         f"6. thieve.co — находит товары в Aliexpress\n"
                         f"7. aliseeks.com— находит товары в Aliexpress и eBay\n"
                         f"8. labs.tib.eu — найдет примерное место съемки фото\n"
                         f"9. image.baidu.com\n"
                         f"10. image.so.com\n"
                         )

@dp.message_handler(text="Документ")
async def get_phone_menu(message: Message):
    await message.answer(f"Для файла формата документ\n\n\n"
                         f"1. exif.regex.info — извлекает META-данные\n"
                         f"2. @mediainforobot — извлекает EXIF\n"
                         f"3. www.forensicdots.de — ищет на скане документа желтые точки являющиеся уникальным идентификатором принтера\n\n\n"
                         f"Инструменты\n\n"
                         f"1. draftable.com — сравнивает два документа показывает разницу\n"
                         f"2. www.diffchecker.com — сравнивает таблицы Excel и показывает отличия\n"
                         )

@dp.message_handler(text="DS_STORE")
async def get_phone_menu(message: Message):
    await message.answer(f"Для файла формата DS_STORE\n\n\n"
                         f"1. intelx.io — узнайте имена файлов скрытые в файле"
                         )

    
@dp.message_handler(text="HAR")
async def get_phone_menu(message: Message):
    await message.answer(f"Для файла формата HAR\n\n\n"
                         f"1. stevesie.com — покажет содержимое файла в удобном виде\n"
                         f"2. googleapps.com — покажет содержимое файла в удобном виде"
                         )


@dp.message_handler(text="Другое")
async def get_phone_menu(message: Message):
    await message.answer(f"Для файлов других расширений\n\n"
                         f"1. exif.regex.info — извлекает META-данные\n"
                         f"2. www.get-metadata.com — извлекает META-данные"
                         )
    

    
    
 #Wi-Fi
@dp.message_handler(text="Wi-Fi")
async def get_phone_menu(message: Message):
    await message.answer(f"Что именно известно о Wi-Fi?", reply_markup=wifi_kb) 
    
    
@dp.message_handler(text="SSID — Имя точки доступа")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по SSID / ESSID / Имя точки доступа\n\n"
                         f"1. wigle.net (r) — находит Wi-Fi точку, ее физический адрес и BSSID", reply_markup=wifi_kb) 
    
     
@dp.message_handler(text="BSSID — MAC-адрес")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по BSSID / MAC-адресу\n\n"
                         f"1. xinit.ru — покажет местоположение Wi-Fi\n"
                         f"2. alexell.ru — тоже покажет местоположение\n"
                         f"3. @iptools_robot — бот найдет адрес и компанию\n"
                         f"4. wigle.net (r) — находит Wi-Fi точку, ее физический адрес и название\n\n\n"
                         f"Поиск через URL\n\n"
                         f"1. https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=00:CC:00:CC:00:CC — найдет координаты точки на карте, замените 00:CC:00:CC:00:CC на MAC-адрес", reply_markup=wifi_kb) 
    
    
    
 #Серийный номер
@dp.message_handler(text="Серийный номер")
async def get_phone_menu(message: Message):
    await message.answer(f"Серийный номер чего?", reply_markup=sernum_kb) 
    
@dp.message_handler(text="Техника")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по серийному номеру техники\\n"

f"1. warrantycheck.epson.eu — техника бренда Epson, даст номер модели, номер материала\n"
f"2. dysonseriallookup.com — техника бренда Dyson, даст дату поставки и продавца\n"
f"3. wwwp.medtronic.com — техника бренда Medtronic, выдает модель и тип медицинского оборудования\n"
f"4. www.bobswatches.com — по серийному номеру часов Rolex выдает год производства\n"
f"5. pcsupport.lenovo.com — техника бренда Lenovo, выдает модель, а если залогиниться то и информацию о гарантии\n"
f"6. www.imei.info — техника бренда Apple, выдет модель, цвет, объем накопителя, время изготовления, место производства\n"
f"7. www.vega.com — техника бренда Vega, различные датчики и системы контроля систем водоснабжения, отопления и прочего связанного с ЖКХ, даст подробную информацию о модели, дате поставки и дате тестирования"
    
    ) 
    
    
    
#IMEI
@dp.message_handler(text="IMEI")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по IMEI\n\n"
                         f"1. www.checkmi.info — показывает страну регистрации Mi-аккаунта, часть номера телефона для восстановления и часть email-адреса\n"
                         f"2. www.imei.info — характеристики устройства\n"
                         f"3. xinit.ru — характеристики устройства\n"
                         f"4. account.lampyre.io (t) (r) — программа находит марку телефона)\n")
                         
                         


#Трекер
@dp.message_handler(text="Трекер")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по номеру трекера\\n"

f"Трекеры это инструмент сбора данных о пользователях для аналитики. Используются на сайтах и в приложениях. Каждый трекер имеет свой уникальный номер который укзан в исходном коде веб страницы.\n"
f"Пример: UA-123456789 — трекер Google Analytics.\n"

f"1. shodan.io — найдет IP адреса и сайты с упоминанием кода трекера\n"
f"2. spyonweb.com — найдет сайты с искомым трекером UA. pub\n"
f"3. intelx.io — найдет сайты с искомым трекером UA, 6 источников поиска\n"
f"4. analyzeid.com — принимает трекеры pub, UA, ищет другие сайты\n"
f"5. osint.sh — найдет сайты с искомым трекером UA\n"
f"6. osint.sh — найдет сайты с искомым трекером pub\n\n\n"


f"Поиск через URL\\n"

f"1. https://www.shodan.io/search?query=http.html%3AUA-12345678-1 — найдет сайты с таким же трекером, замените UA-12345678-1 на свой код трекера\n"
f"2. https://host.io/api/domains/googleanalytics/UA-2345678?limit=5&token=TOKEN (r) — найдет сайты с таким же трекером, замените UA-12345678-1 на свой код трекера, замените TOKEN на API токен который вы получите после регистрации\n"
f"3. https://metrika.yandex.ru/dashboard?id=12345678 — покажет возраст, директории сайта, примерное место нахождения пользователей, можно выявить админа как первого посетителя. Требуется вход в свой аккаунт. Замените 12345678 на ID Яндекс Метрики, аналитика может быть закрыта")
                         
                         
                         
                         
#Текст
@dp.message_handler(text="Текст")
async def get_phone_menu(message: Message):
    await message.answer(f"Для текста\n\n\n"

f"1. istio.com — семантический анализ текста, выявит ошибки, частотность слов и количество символов\n"
f"2. miratext.ru — семантический анализ текста, количество повторений словосочетаний и слов\n"
f"3. voyant-tools.org — анализирует текст, показывает частые взаимосвязи слов, повторения фраз и много другого, можно загружать огромные тексты\n"
f"4. JGAAP (t) — анализа текста, категоризации текста и атрибуции авторства, стилометрия и текстометрия\n\n\n"


f"Инструменты\\n"

f"1. copyscape.com — сравнит 2 текста и покажет разницу")



#Пароль
@dp.message_handler(text="Пароль")
async def get_phone_menu(message: Message):
    await message.answer(f"Поиск по паролю\n\n\n"
                        f"1. @sgk123bot — найдет аккаунты QQ и email адреса. поиск по китайской базе утечек\n"
                        f"2. leakpeek.com — найдет часть имени пользователя, email и название утечки\n"
                        f"3. eog.pw (r) — найдет часть номера телефона и email\n"
                        f"4. haveibeenpwned.com — даст знать утекал ли пароль\n"
                        f"5. leak-lookup.com (r) — покажет на каких сайтах была утечка с искомым паролем"
                        )

#Базы данных

@dp.message_handler(text="🗄 Базы данных")
async def get_phone_menu(message: Message):
    await message.answer(f"Базы данных\n\n\n"

f"1. databases.today — архив баз банков, сайтов, приложений\n"
f"2. raidforums.com (r) — ссылки на скачивание разных баз с 1995 года\n"
f"3. @basetelega — утечки, компании, парсинг открытых источников\n"
f"4. ebaza.pro (r) — есть email, телефонные номера, физ. лица, предприятия, базы доменов и другие\n"
f"5. xss.is — список баз, 3,5B записей, 52 базы\n"
f"6. hub.opengovdata.ru — Российские базы статистики, росстата, архивы сайтов, финансы, индикаторы, федеральные органы власти, суды и т.д\n"
f"7. @freedomf0x — утечки сайтов, приложений, гос. структур\n"
f"8. @leaks_db — агрегатор публичных утечек\n"
f"9. @BreachedData — утечки сайтов, приложений, соц. сетей, форумов и т.д.\n"
f"10. @opendataleaks — дампы сайтов школ, судов, институтов, форумов по всему миру\n")

