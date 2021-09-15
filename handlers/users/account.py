from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from keyboards.default.account_kb import account_kb_1, account_kb_2, vk_kb
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from states.states import Account


@dp.message_handler(text="Аккаунт")
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"Аккаунт где?", reply_markup=account_kb_1)
    await Account.Q1.set()
    

@dp.message_handler(text='Еще ⁣➜', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"Аккаунт где\n\n"
                         f"Страница 2", reply_markup=account_kb_2)
    await Account.Q2.set()
    
  


@dp.message_handler(text='Lolzteam', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ID аккаунта на Lolzteam\n\n</b>1<b>. </b>@LZTbot <b>— </b>даст email, часовой пояс, ник и возможно номер телефона')

@dp.message_handler(text='LinkedIn', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту LinkedIn\n\n</b>1. <a href="https://search.google.com/test/mobile-friendly">search.google.com</a> — анонимный просмотр аккаунта, впишите ссылку на аккаунт в поле ввода\n2. icwatch.wikileaks.org — поиск по имени аккаунта США, находит утекшую информацию, телефоны, почту \n3. <a href="https://rocketreach.co/person">rocketreach.co</a> (r) — введите URL адрес в строку поиска и сервис даст соц сети, телефоны и другие данные\n\n\n<b>Парсеры\n\n</b>1. <a href="https://phantombuster.com/automations/linkedin/3112/linkedin-profile-scraper">phantombuster.com</a> (r) — скачает всю публичную информацию аккаунта\n2. <a href="https://github.com/0x09AL/raven">raven</a> (t) — сбор информации о сотрудниках организации из Google\n\n\n<b>Дополнительные методы\n\n</b>1. Почтовый индекс. \n[1] Перейдите на страницу аккаунта\n[2] Откройте исходный код страницы (Ctrl+U)\n[3] Найдите (Ctrl+F) там строку с <code>postalCode\n</code>цифры после и есть почтовый индекс')

@dp.message_handler(text='Kik', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по аккаунту Kik\n\nТут пока ничего нет\n\n\nЧерез URL\n\n1. https://ws2.kik.com/user/username — дата изменения изображения аккаунта и ссылка на него, замените <code>username</code> на имя пользователя\n\n\nВосстановление доступа\n\n1. <a href="https://ws.kik.com/p">Kik</a>')

@dp.message_handler(text='Keybase', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Для аккаунта Keybase\n\nЗдесь пока ничего нет.\nЗнаете ресурс? Тогда напишите автору через бота.\n\n\nДополнительные методы\n\n1. Узнать Email адрес\n[1] Поменяйте USERNAME в ссылке на username аккаунта\nhttps://keybase.io/USERNAME/pgp_keys.asc\n[2] Если перейдя по новой ссылке PGP ключ есть, то скопируйте весь текст с сайта и вставьте его\nсюда peegeepee.com')

@dp.message_handler(text='ICQ', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ID аккаунта ICQ\n\nпока тут ничего нет\n\n\nВосстановление доступа\n\n1. <a href="https://icq.com/password/">icq.com</a>')


@dp.message_handler(text='Huawei', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по аккаунту Huawei\n\nТут пока ничего нет\n\n\nВосстановление доступа\n\n1. <a href="https://uniportal.huawei.com/uniportal/modifyInfo.do?actionFlag=toGetPassword">huawei.com\n</a>2. <a href="https://id8.cloud.huawei.com/AMW/portal/appealSelf/applyChangeAccount.html">cloud.huawei.com</a>')


@dp.message_handler(text='habr', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту habr\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID')


@dp.message_handler(text='GitLab', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта GitLab\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID\n\n\n<b>Через URL\n\n</b>1. https://gitlab.com/USERNAME.keys — найдет ssh ключи, замените <code>USERNAME</code>')

@dp.message_handler(text='Flickr', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Flickr\n\n</b>1. <a href="https://www.webfx.com/tools/idgettr/">www.webfx.com</a> — находит ID аккаунта')


@dp.message_handler(text='eBay', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по аккаунту eBay\n\nПока тут ничего нет\n\n\nПоиск через URL\n\n1. https://www.ebay.com/sch/ebayadvsearch/?_ec=104&_sofindtype=25&_userid=USERNAME — замените <code>USERNAME</code> на имя пользователя, отображает непонятно что\n\n2. https://www.ebay.com/fdbk/feedback_profile/USERNAME — замените <code>USERNAME</code> на имя пользователя, отображает отзывы пользователя\n\n3. https://www.ebay.com/usr/USERNAME замените <code>USERNAME</code> на имя пользователя, отображает дату создания аккаунта и страну заказчика\n\n\nВосстановление доступа\n\n1. <a href="https://signin.ebay.com/ws/eBayISAPI.dll?SignIn">ebay</a>')


@dp.message_handler(text='Eyeem', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Eyeem\n\n\nДополнительные методы\n\n</b>1. Как найти аккаунт на Facebook\n\n[1] Откройте профиль пользователя в браузере\n[2] Перейдите в исходный код страницы\n[3] Найдите там фразу <code>graph.facebook.com</code> и скопируйте длинное число после этого фрагмента\n[4] Подставьте это число в ссылку вместо <code>USERID</code> и перейдите по ней\n<code>https://www.facebook.com/profile.php?id=USERID</code>')

@dp.message_handler(text='Discord', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Discord\n\n</b>1. discord.id — показывает дату создания и фото\n2. <a href="https://discordhub.com/user/search">discordhub.com</a> — находит сервера\n3. <a href="https://discordleaks.unicornriot.ninja/discord/users">discordleaks.unicornriot.ninja</a> — находит сервера и сообщения\n4. <a href="https://hugo.moe/discord/discord-id-creation-date.html">hugo.moe</a> — показывает дату создания аккаунта\n\n\nПоиск по названию сервера\n\n1. discordservers.com — дает ссылку на вступление\n2. discord.center — дает ссылку на вступление, в базе 36К серверов\n3. disboard.org — дает ссылку на вступление, в базе 700К+ серверов\n4. discord.me — дает ссылку на вступление, в базе 30К+ серверов\n5. discordbee.com — дает ссылку на вступление, в базе 5К+ серверов\n\n\n<b>Парсеры\n\n</b>1. dht.chylex.com — загрузит историю выбранного текстового канала до первого сообщения и позволит вам загрузить его для просмотра в автономном режиме в вашем браузере\n2. <a href="https://exportcomments.com/export-discord-conversation">exportcomments.com</a> — экспортирует весь чат из вашего канала Discord в файл CSV')

@dp.message_handler(text='Clubhouse', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Clubhouse\n\n</b>1. clubhousedb.com — дата регистрации, био, соц. сети, группы, кто пригласил')

@dp.message_handler(text='Blogspot', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Blogspot\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID, qq_uID, fb_uID, Instagram, Twitter, сайт, Facebook\n\n\n<b>Дополнительные методы\n\n</b>1. Найти профиль автора блога\n[1] Откройте исходный код страницы блога (Ctrl+U)\n[2] Найдите там фразу <code>https://www.blogger.com/profile/</code>')
    
    
@dp.message_handler(text='Bitbucket', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Bitbucket\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID, и дату создания аккаунта\n\n\n<b>Поиск через URL\n\n1</b>. https://bitbucket.org/!api/2.0/repositories/USERNAME/REPO-NAME/refs/branches/master — покажет email адрес, замените <code>USERNAME</code> на имя пользователя, а <code>REPO-NAME</code> на имя репозитория который создал этот пользователь')
    
    
@dp.message_handler(text='Behance', state=Account.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Behance\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID')

@dp.message_handler(text='Xbox Live', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Xbox</b> Live\n\n1. <a href="https://www.stratege.ru/site_search">stratege.ru</a> — находит статистику аккаунта, коллекцию игр, профили в других играх\n2. xboxgamertag.com — покажет в какие игры и когда играл пользователь')
    
    
    
@dp.message_handler(text='Xiaomi', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ID аккаунта Xiaomi\n\n</b>1<b>. </b>@UniversalSearchBot <b>— </b>даст дату создания, ник, фото профиля, название школы и много друое\n\n\n<b>Восстановление доступа\n\n</b>1. <a href="https://account.xiaomi.com/pass/retrieve/applyManualRetrieve">Xiaomi</a>')
    
    
@dp.message_handler(text='Weibo', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ID аккаунта Weibo\n\n</b>1. @DATA_007bot — дает номер телефона\n2. @sgk123bot — дает номер телефона')
    
@dp.message_handler(text='vc.ru', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта <b></b>vc</b>.ru\n\n1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID')
    
    
    
@dp.message_handler(text='Twitch', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Twitch\n\n</b>1. archive.org — покажет архивированную версию аккаунта\n2. twitchtracker.com — аналитика активности аккаунта, история трансляций, дата создания аккаунта и многое другое\n3. sullygnome.com — статистика, история стримов, лайки, подписчики и другое\n\n\n<b>Парсеры</b>\n\n1. <a href="https://twitch-tools.rootonline.de/followerlist_viewer.php">twitch-tools.rootonline.de</a> — скачивает всех полписчиков, показывает статистику дат созданий аккаунтов, дает поиск по всему списку\n\n\n<b>Инструменты</b>\n\n1. @AximoBot — мгновенно сохранит новые публикации аккаунта в Telegram')


@dp.message_handler(text='Tumblr', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Tumblr\n\n</b>1. www.tumbex.com — покажет удаленные посты если они есть')


@dp.message_handler(text='Steam', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Steam\n\n</b>1. <a href="https://cyber-hub.net/steam_resolver.php">cyber-hub.net</a> — инструмент, который позволяет вам получить IP пользователя в реальном времени или из базы данных с сохраненными результатами\n2. archive.org — покажет архивированную версию аккаунта\n3. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет Steam ID, даже скрытого аккаунта\n4. steamid.uk — поиск по Steam ID, логину, Steam3, Community ID, найдет историю ников, дату создания, историю аватаров, статистику друзей\n5. rep.tf — агрегирует информацию об аккаунте из разных источников\n6. <a href="https://steamidfinder.com/lookup/">steamidfinder.com</a> — закешированная информация аккаунта\n7. steamid.io — найдет все ID, старый кастомный URL, имя и локацию\n8. findsteamid.com — найдет все ID, картинку аккаунта и дату его создания\n9. steamdb.info — найдет все ID, операционную систему и другое')
    
    
@dp.message_handler(text='Stackoverflow', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Stackoverflow\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID и stack_exchange_uid\n2. <a href="https://cse.google.com/cse?cx=partner-pub-7396620608505330:xjbbr6-w0cu">cse.google.com</a> — найдет упоминания на сайте Stackoverflow')
    
    
    
@dp.message_handler(text='Snapchat', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Snapchat\n\n</b>1. snapdex.com — подробная информация о аккаунте, у сайта своя база\n2. somesnapcode.com — аналогичен snapdex, но урезан\n3. archive.org — покажет архивированную версию аккаунта')
    
    
@dp.message_handler(text='Skype', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по аккаунту Skype\n\n1. <a href="http://mostwantedhf.info/skype2email.php">mostwantedhf.info</a> — найдет почту\n2. webresolver.nl — найдет IP\n3. @usersbox_bot — бот найдет аккаунты в ВК у которых в поле skype  указан искомый логин, введите в боте  skype: логин\n4. <a href="https://github.com/cyberhubarchive/archive">cyberhubarchive</a> — архив утекших данных, в нем есть IP адреса пользователей\n5. @smart_search_3_bot — находит email, номер телефона и другое\n6. <a href="https://www.vedbex.com/tools/skype_resolver">vedbex.com</a> — найдет IP\n\n\nПоиск через URL\n\n1. https://avatar.skype.com/v1/avatars/USERNAME/public — фото аккаунта. Замените <code>USERNAME</code> на логин аккаунта\n\n\nВосстановление доступа\n\n<a href="https://go.skype.com/reset.password.skype">go.skype.com</a>')
    
    
@dp.message_handler(text='SoundCloud', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту SoundCloud\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID')
    
@dp.message_handler(text='Q⁣Q⁣', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ID аккаунта QQ\n\n1. @boluosgkbot — дает номер телефона\n2. @DATA_007bot — дает номер телефона\n3. @sgk123bot — дает номер телефона, пароль, email')
    
    
    
@dp.message_handler(text='Playstation', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Playstation\n\n</b>1. <a href="https://www.stratege.ru/site_search">stratege.ru</a> — находит статистику аккаунта, коллекцию игр, профили в других играх')
    
    
    
@dp.message_handler(text='Pinterest', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Pinterest\n\n1. archive.org</b> <b>— покажет архивированную версию аккаунта\n</b>\n\n<b>Восстановление доступа\n\n</b>1. <a href="https://www.pinterest.ru/password/reset/">Pinterest</a>')
    
    
@dp.message_handler(text='Patreon', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту на Patreon\n\n</b>1. graphtreon.com — статистика патронов и примерный доход')
    
    
@dp.message_handler(text='Parler', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Parler\n\n</b>1. parler.adatascienti.st — архив всех данных соцсети, найдет посты и комментарии')
    
@dp.message_handler(text='Nintendo', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по аккаунту Nintendo\n\n</b>1. <a href="https://www.stratege.ru/site_search">stratege.ru</a> — находит статистику аккаунта, коллекцию игр, профили в других играх')
    
    
@dp.message_handler(text='Medium', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Medium\n\n</b>1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID, Twitter username, Facebook ID аккаунта')

@dp.message_handler(text='mail.ru', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для аккаунта Mail</b>.Ru\n\n1. <a href="https://github.com/soxoj/socid_extractor">socid_extractor</a> (t) — найдет user ID')

@dp.message_handler(text='Другой ресурс', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по профилям других сервисов\n\n<i>Если на сайте можно войти через Facebook, то в профиле может остаться ID аккаунта Facebook через который был вход\n\n\n</i>Как найти аккаунт на Facebook\n\n[1] Откройте профиль пользователя в браузере\n[2] Перейдите в исходный код страницы\n[3] Найдите там фразу <code>graph.facebook.com</code> и скопируйте длинное число после этого фрагмента\n[4] Подставьте это число в ссылку вместо <code>USERID</code> и перейдите по ней\n<code>https://www.facebook.com/profile.php?id=USERID</code>')


@dp.message_handler(text='ВК', state=Account.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Что именно?', reply_markup=vk_kb)




   
 

