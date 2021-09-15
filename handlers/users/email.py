from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from keyboards.default.email_kb import email_kb
from aiogram.dispatcher import filters
from keyboards.default.dop_kb import dop_kb, yandex_dop_kb
from aiogram.dispatcher import FSMContext

from states.states import Email



@dp.message_handler(text="E-mail")
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"Какой почтовый сервис?\n\n"
                         f"▌ Совет\n"
                         f"▌ Поменяй домен в e-mail\n"
                         f"▌ адресе на другой.\n", reply_markup=email_kb)
    await Email.email.set()


@dp.message_handler(text='Определить почтовый сервис', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Как найти к какому домену принадлежит email адрес\n\nНапример вы знаете только <code>somebody@g****.***\n\n</code>1. Установите расширение для браузера Chrome <a href="https://chrome.google.com/webstore/detail/find%2B-regex-find-in-page/fddffkdncgkkdjobemgbpojjeffmmofb">Find+\n</a>2. Откройте следующие списки сайтов\n<a href="https://github.com/Matchistador/threat/blob/64edd837b611b55083d71f5611ced789b542e6ba/free_email_provider_domains.txt">Список1\n<a href="https://github.com/Kixiron/Anti-Phish/blob/513cbc16729bead0ba4c2e17ec705cdbe949b928/Anti-Phish/data/alldomains.json"></a>Список2\n<a href="https://github.com/vidyasagarpanati/opensource-data/blob/0c10f2b764ef8824becb00f5174ab786a22a9e2c/Email%20Domains"></a>Список3\n<a href="https://github.com/gyankos/graphjoin/blob/1d71a2102c2c95a634d61079a8ab3002b2c467a8/usergenerator/src/main/resources/email.txt"></a>Список4\n\n</a>3. Откройте расширение и введите туда регулярное выражение\n<code>X\w{A}\.\w{B}$\n\n</code>Где нужно заменить <code>X</code> на первую известную букву, <code>A</code> на количество звездочек в домене, а <code>B</code> на количество звездочек в домене первого уровня\n\nНапример известен адрес <code>somebody@g****.***</code> и регулярное выражение для него будет таким <code>g\w4\.\w3$</code> (Только с фигурными скобками)\n\n4. Подставив ваше регулярное выражение в поиск от расширения вы найдете сайты которые подходят под маску вашего email адреса')
    # await message.answer('<b>Как найти к какому домену принадлежит email адрес\n\n</b>Например вы знаете только <code>somebody@g****.***\n\n<b></code>1</b>. Установите расширение для браузера Chrome <a href="https://chrome.google.com/webstore/detail/find%2B-regex-find-in-page/fddffkdncgkkdjobemgbpojjeffmmofb">Find+\n</a>2. Откройте следующие списки сайтов\n<a href="https://github.com/Matchistador/threat/blob/64edd837b611b55083d71f5611ced789b542e6ba/free_email_provider_domains.txt">Список1\n<a href="https://github.com/Kixiron/Anti-Phish/blob/513cbc16729bead0ba4c2e17ec705cdbe949b928/Anti-Phish/data/alldomains.json"></a>Список2\n<a href="https://github.com/vidyasagarpanati/opensource-data/blob/0c10f2b764ef8824becb00f5174ab786a22a9e2c/Email%20Domains"></a>Список3\n<a href="https://github.com/gyankos/graphjoin/blob/1d71a2102c2c95a634d61079a8ab3002b2c467a8/usergenerator/src/main/resources/email.txt"></a>Список4\n\n</a>3. Откройте расширение и введите туда регулярное выражение\n<code>X\w{A}\.\w{B}$\n\n</code>Где нужно заменить <code>X</code> на первую известную букву, <code>A</code> на количество звездочек в домене, а <code>B</code> на количество звездочек в домене первого уровня\n\nНапример известен адрес <code>somebody@g****.***</code> и регулярное выражение для него будет таким <code>g\w4\.\w3$</code> (Только с фигурными скобками)\n\n4. Подставив ваше регулярное выражение в поиск от расширения вы найдете сайты которые подходят под маску вашего email адреса')


@dp.message_handler(text='Любой⁣⁣⁣', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по Email адресу любых почтовых сервисов\n\n1. haveibeenpwned.com — проверка почты в слитых базах\n2. emailrep.io — найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту\n3. dehashed.com (r) — проверка почты в слитых базах\n4. intelx.io — многофункциональный поисковик, поиск осуществляется еще и по даркнету\n5. @info_baza_bot — покажет из какой базы слита почта, 2 бесплатных скана\n6. leakedsource.ru — покажет в каких базах слита почта\n7. mostwantedhf.info — найдет аккаунт skype\n8. email2phonenumber (t) — автоматически собирает данные со страниц восстановления аккаунта, и находит номер телефона\n9. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию\n10. @last4mailbot — бот найдет последние 4 цифры номера телефона клиента Сбербанка\n11. searchmy.bio — найдет учетную запись Instagram с электронной почтой в описании\n12. @av100_bot (r) — найдет аккаунт в ВК\n13. account.lampyre.io (t, r) — программа выполняет поиск по аккаунтам  в соц. сетях и мессенджерам и другим источникам\n14. глазбога.рф (r) — найдет фото аккаунта\n15. @StealDetectorBOT — поисковик по базам утечек, найдет пароли, IP, ники и многое другое, в поле поиска введите email: и после e-mail адрес, например email:example@site.com\n16. cyberbackgroundchecks.com — найдет все данные гражданина США, вход на сайт разрешен только с IP адреса США\n17. holehe (t) — инструмент проверяет аккаунты каких сайтов зарегистрированы на искомый email адрес, поиск по 30 источникам\n18. tools.epieos.com — найдет Google ID, даст ссылки на профиль в Google карты, альбомы и календарь, найдет к каким сайтам привязана почта, профиль LinkedIn\n19. ⚡️@UniversalSearchBot — найдет профили на Яндекс, в сервисах Google, утекшие пароли, социальные сети, адрес регистрации, номер телефона, био, Gmail адрес и прочее\n20. grep.app — поиск в репозиториях GitHub\n21. @PasswordSearchBot — выдает пароли\n22. Checker#7610 — Discord бот, найдет пароли, сайты откуда они взяты и где привязана почта\n23. m.ok.ru — показывает часть номера телефона, email, фамилии и полностью город с датой регистрации, используй во вкладке инкогнито\n24. www.avatarapi.com — найдет аватарку из множества источников\n25. @mailExistsBot — найдет к каким сайтам привязана почта, даст данные из форм восстановления пароля\n26. @SEARCHUA_bot — выдает досье на гражданина Украины где есть паспорт, адрес проживания, ФИО, автомобили, родственники, email, номера телефонов и много другого\n27. @SovaAppBot — найдет к каким сайтам привязана почта, результаты могут отличаться от аналогичных инструментов\n28. www.vedbex.com — найдет аккаунт Skype\n29. @smart_search_3_bot — найдет ФИО, дату рождения, адрес, телефон и много другого, дает несколько бесплатных попыток на один аккаунт\n30. tools.whoisxmlapi.com — найдет упоминание в истории вwhois всех сайтов и покажет домены\n31. @gdepochtabot — покажет на каких сайтах утекли пароли\n32. @shi_ver_bot — утекшие пароли\n33. aihitdata.com — найдет компании по всему миру где указан телефон, откройте вкладку “More Fields”\n34. www.skypli.com — выдает аккаунт Skype\n35. effectgroup.io (r) — найдет социальные сети, ФИО, номера телефонов, адрес проживания, компании и прочее, иногда нужен VPN, 1 полный отчет на аккаунт\n36. melissa.com — найдет ФИО, дату рождения, адрес проживания, этнос и прочее гражданина США\n37. leak-lookup.com (r) — покажет на каких сайтах была утечка с искомым email\n\n\nПоиск через URL\n\n1. https://my.mail.ru/SITE/LOGIN — поиск аккаунта на Мой Мир, замените LOGIN на email адрес без @SITE.COM а SITE на тот сайт который указан в email адресе после "@". Например из gelver.maria@web.de в https://my.mail.ru/web.de/gelver.maria/\n2. https://filin.mail.ru/pic?email=LOGIN@site.com — картинка аккаунта на mail.ru, замените LOGIN@site.com на email адрес\n3. https://myspace.com/search/people?q=LOGIN@site.com — аккаунт на MySpace, любой аккаунт может привязать любую почту без подтверждения, замените LOGIN@site.com на email адрес')
    
    await message.answer('<b>Восстановление доступа\n\n</b>1. <a href="https://passport.vivo.com/#/retrievePwdEmailVerify">Vivo\n</a>2. <a href="https://signin.ebay.com/ws/eBayISAPI.dll?SignIn">ebay\n</a>3. <a href="https://www.paypal.com/authflow/password-recovery/">PayPal\n</a>4. <a href="https://account.mail.ru/recovery/">Mail.ru\n</a>5. <a href="https://account.xiaomi.com/pass/retrieve/applyManualRetrieve">Xiaomi\n</a>6. <a href="https://twitter.com/account/begin_password_reset">Twitter\n</a>7. <a href="https://vk.com/restore">VK.com\n</a>8. <a href="https://account.live.com/password/reset">live.com\n</a>9. Ozon.ru\n10. <a href="https://www.facebook.com/login/identify?ctx=recover">Facebook\n</a>11. <a href="https://id8.cloud.huawei.com/AMW/portal/appealSelf/applyChangeAccount.html">Cloud.Huawei.com</a>')



@dp.message_handler(text='Yandex', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f'Поиск по Email от Яндекса\n\n'
                         f'1. YaSeeker (t) — найдет все профили и их данные на Яндексе\n'
                         f'2. /email — список ресурсов для поиска по Email адресу любого почтовогосервиса\n\n\n'
                         f'Поиск через URL\n\n'
                         f'1. https://yandex.ru/collections/user/LOGIN — аккаунт в Яндекс Коллекциях, содержит имя и фото аккаунта. Замените LOGIN на юзернейм из адреса почты БЕЗ @yandex.ru\n'
                         f'2. https://music.yandex.ru/users/LOGIN —  аккаунт в Яндекс Музыке, содержит имя и фото аккаунта. Замените LOGIN на юзернейм из адреса почты БЕЗ @yandex.ru', reply_markup=dop_kb)
    await Email.yandex.set()
    

@dp.message_handler(text='Дополнительныe методы⁣⁣⁣⁣⁣⁣', state=Email.yandex)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Допoлнитeльные мeтоды', reply_markup=yandex_dop_kb)
    


@dp.message_handler(text='Gmail', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email от Gmail\n\n</b>1. <a href="https://github.com/mxrch/GHunt">GHunt</a> (t) — инструмент достанет Google ID, устройства, имя аккаунта, найдет какие сервисы Google используется, данные из отзывов на Google картах\n2. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n<b>Поиск через URL\n\n</b>1. https://calendar.google.com/calendar/u/0/embed?src=LOGIN@gmail.com — календарь с записями, замените <code>LOGIN@gmail.com</code> на email адрес Gmail\n\n\n<b>Восстановление доступа\n\n</b>1. <a href="https://login.aol.com/">Aol\n</a>2. <a href="https://accounts.google.com/signin/v2/identifier">Google</a>')



@dp.message_handler(text='Mail.ru', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email от </b>Mail.ru / inbox.ru / bk.ru / list.ru\n\n1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n<b>Поиск через URL\n\n</b>1. https://love.mail.ru/ru/LOGIN — профиль на сайте знакомств, замените <code>LOGIN</code> на email адрес без @mail.ru')



@dp.message_handler(text='ProtonMail', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по E-mail адресу от ProtonMail\n\n</b>1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n<b>Дополнительный методы\n\n</b>1. Как найти дату создания ProtonMail адреса\n\n[1] Создайте или войдите в аккаунт на old.ProtonMail.com\n[2] Откройте <a href="https://mail.protonmail.com/contacts">контакты</a> и нажмите на добавить контакт \n[3] В поле E-mail введите E-mail адрес ProtonMail\n[4] Возле адреса появится шестеренка на которую нужно нажать')



@dp.message_handler(text='Yahoo', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email от Yahoo</b> \n\n1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n <b>Восстановление доступа\n\n</b>1. <a href="https://login.aol.com/">Aol\n</a>2. <a href="https://login.yahoo.com/?display=login">Yahoo</a>')



@dp.message_handler(text='QQ', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email почтового сервиса </b>QQ.com\n\n1. @coolsgk_bot — находит аккаунт QQ и его ID\n2. @sgk123bot —  находит аккаунт QQ, его ID, имя пользователя и пароль\n3. /email — список ресурсов для поиска по Email адресу любого почтового сервиса')



@dp.message_handler(text='GMX.net', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email адресу от </b>GMX.net\n\n1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n<b>Восстановление доступа\n\n</b>1. <a href="https://passwort.gmx.net/passwordrecovery">GMX</a>')



@dp.message_handler(text='Web.de', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email адресу от </b>Web.de\n\n1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n<b>Восстановление доступа\n\n</b>1. <a href="https://passwort.web.de/passwordrecovery/">Web.de</a>')





@dp.message_handler(text='Rambler', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email с доменами </b>rambler.ru <b>/ </b>lenta.ru <b>/ </b>autorambler.ru <b>/ </b>myrambler.ru <b>/ </b>ro.ru <b>/ </b>rambler.ua\n\n1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n<b>Поиск через URL\n\n</b>1. https://avatars.rambler.ru/get/LOGIN@rambler.ru/default — картинка аккаунта, замените <code>LOGIN@rambler.ru</code> на email адрес')





@dp.message_handler(text='Aol', state=Email.email)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по Email с доменом </b>Aol.com\n\n1. /email — список ресурсов для поиска по Email адресу любого почтового сервиса\n\n\n<b>Восстановление доступа\n\n</b>1. <a href="https://login.aol.com/">Aol</a>')






