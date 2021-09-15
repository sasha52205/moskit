from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from keyboards.default.fio_kb import fio_kb_1, fio_kb_2
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from states.states import Fio



@dp.message_handler(text="ФИО")
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer(f"ФИО гражданина какой страны?", reply_markup=fio_kb_1)
    await Fio.Q1.set()

@dp.message_handler(text="Любо⁣⁣й",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина любой страны\n\n</b>1. aleph.occrp.org — поиск по базам данных, файлам, реестрам компаний, утечкам, и другим источникам\n2. <a href="https://www.locatefamily.com/">locatefamily.com</a> — найдет адрес\n3. infobel.com — найдет номер телефона, адрес и ФИО\n4. rocketreach.co (r) — поиск людей в LinkedIn, Facebook и на других сайтах, находит email\n5. <a href="https://munscanner.com/dbs/">munscanner.com</a> — поиск по реестрам компаний разных стран\n6. world.192.com — каталог сайтов белых и желтых страниц по поиску человека, есть почти все страны\n7. news-explorer.mybluemix.net — поиск в СМИ, найдет ассоциации между компаниями, публикациями и личностями\n8. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США\n9. <a href="https://github.com/WhiteHatInspector/emailGuesser">emailGuesser</a> (t) — подбирает на основе ФИ все возможные комбинации email адреса и верифицирует их\n10. <a href="http://4wbwa6vcpvcr3vvf4qkhppgy56urmjcj2vagu2iqgp3z656xcmfdbiqd.onion.pet/">FuckFacebook</a> — находит аккаунт Facebook с номером телефона в крупной утечке\n11. billiongraves.ru — найдет когда умер и где захоронен\n12. <a href="https://www.findmypast.co.uk/search/historical-records?region=world&page=1&order_direction=desc&order_by=relevance">www.findmypast.co.uk</a> (r) — браки, смерти, рождения до 2006 года, нужно указать страну, нет стран СНГ\n13. webmii.com — упоминания в новостях, профили в социальных сетях, видео, можно добавить ключевое слово для точного результата\n14. aihitdata.com — найдет компании по всему миру где работает человек, откройте вкладку “More Fields” и введите ФИ в кавычках\n15. effectgroup.io (r) — найдет социальные сети, номера телефона, email, адрес проживания, компании и прочее, иногда нужен VPN, 1 полный отчет на аккаунт\n16. xlek.com — найдет какой домен был зарегистрирован на искомое ФИО, поиск в whois, покажет контакты и адреса\n17, <a href="https://my.mail.ru/my/search_people">my.mail.ru</a> (r) — даст аккаунт но Мой Мир, есть фильтры по возрасту, росту, весу, интересам и прочему\n18. <a href="https://leak-lookup.com/search">leak-lookup.com</a> (r) — покажет на каких сайтах была утечка с искомым ФИО\n\n\n<b>Восстановление доступа\n\n1</b>. <a href="https://account.samsung.com/accounts/v1/MBR/findId">Samsung</a> — покажет часть email или телефона, необходимо ввести полную дату рождения')
    
    
@dp.message_handler(text="🇷🇺 России⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина России\n\n</b>1. @egrul_bot — найдет ИП и компании\n2. <a href="https://www.reestr-zalogov.ru/search/index">reestr-zalogov.ru</a> — поиск в реестре залогодателей, даст паспортные данные, место и дату рождения и т.д.\n3. <a href="https://zytely.rosfirm.info/m/">zytely.rosfirm.info</a> — найдет адрес прописки и дату рождения, необходимо знать город\n4. mmnt.ru — найдет упоминания в документах\n5. kad.arbitr.ru — найдет дела арбитражных судов\n6. bankrot.fedresurs.ru — поиск в реестре банкротов, можно узнать ИНН, СНИЛС и адрес\n7. spra.vkaru.net — телефонный справочник по России, Украине, Белоруссии, Казахстану, Литве и Молдове\n8. <a href="http://fssprus.ru/iss/ip/">fssprus.ru</a> — проверка задолженностей, для физ. лица\n9. <a href="https://www.reestr-dover.ru/revocations">reestr-dover.ru</a> — поиск в списке сведений об отмене доверенности\n10. <a href="https://data.notariat.ru/directory/succession/search?last_name=%D0%BF%D0%B5%D1%82%D1%80%D0%B5%D0%BD%D0%BA%D0%BE&first_name=&middle_name=#">notariat.ru</a> — поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дело\n11. глазбога.рф — обратный поиск в GetContact, находит часть номера телефона\n12. <a href="https://service.nalog.ru/inn.do">nalog.ru</a> — найдет ИНН, необходимо указать дату рождения и паспортные данные, дату выдачи не обязательно верно\n13. <a href="https://go.mail.ru/msocial">go.mail.ru</a> — ищет аккаунты в VK, OK и Facebook\n14. <a href="https://bigbookname.com/search#">bigbookname.com</a> — находит древние данные профилей ВК, есть фильтры по дате рождения, по стране и городу\n15. <a href="https://notariat.ru/ru-ru/help/probate-cases/">notariat.ru</a> — если человек умер, то найдет дату смерти, номер наследственного дела, где оно было открыто и каким нотариусом \n16. @av100_bot (r) — дает номер телефона, находит суды и долги\n17. wordstat.yandex.ru — покажет что ищут вместе с ФИ или ФИО в Яндексе\n18. news.myseldon.com — находит упоминания в российских СМИ, строит дерево связей между медийными объектами, которое образуются на основе их совместного упоминания в тексте новости\n19. @The_New_Get_Contact_Bot — найдет номер телефона, можно вводить ФИ или любую другую фразу\n20. nomer-org.website — найдет полный адрес проживания и номер телефона, нужно указать город\n21. spravnik.com — найдет номер телефона, адрес регистрации, необходимо знать город\n22. <a href="https://www.list-org.com/?search=boss">www.list-org.com</a> — найдет организацию в учредителях и руководителях\n23. <a href="https://www.list-org.com/?search=fio">www.list-org.com</a> — найдет предпринимателя, его госзакупки, дерево связей\n24. /se_court_ru — список ресурсов для поиска в судах России\n25. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇰🇿 Казахстана",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Казахстана\n\n</b>1. mmnt.ru — найдет упоминания в документах\n2. spra.vkaru.net — телефонный справочник\n3. zytely.rosfirm.info — найдет адрес прописки и дату рождения\n4. fa-fa.kz — проверка наличия задолженностей, ИП, и ограничения на выезд\n5. @ShtrafKZBot — найдет ИНН, дату рождения и много других данных\n6. <a href="http://kgd.gov.kz/ru/services/taxpayer_search_unreliable">kgd.gov.kz</a> — поиск в базе неблагонадежных налогоплательщиков, найдет ИНН/БИН и РНН\n7. глазбога.рф — обратный поиск по GetContact, находит часть номера телефона\n8. <a href="https://bigbookname.com/search#">bigbookname.com</a> — находит древние данные профилей ВК, есть фильтры по дате рождения, по стране и городу\n9. adata.kz — выдаст ИНН в URL, дату рождения предпринимателя\n10. @The_New_Get_Contact_Bot — найдет номер телефона, можно вводить ФИ или любую другую фразу\n11. nomer-org.website — найдет полный адрес проживания и номер телефона, нужно указать город\n12. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇺🇦 Украины⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Украины\n\n</b>1. <a href="http://erb.minjust.gov.ua/#/search-debtors">minjust.gov.ua</a> — реестр должников, дату рождения, связь с исполнителем, номер ВП, категорию взыскания\n2. <a href="https://usr.minjust.gov.ua/content/free-search">usr.minjust.gov.ua</a> — находит место жительства\n3. mmnt.ru — найдет упоминания в документах\n4. spra.vkaru.net — телефонный справочник\n5. <a href="https://court.opendatabot.ua/#/">court.opendatabot.ua</a> — поиск в судебных решениях\n6. глазбога.рф — обратный поиск по GetContact, находит часть номера телефона, зарегистрированные организации, авто\n7. <a href="https://bigbookname.com/search#">bigbookname.com</a> — находит древние данные профилей ВК, есть фильтры по дате рождения, по стране и городу\n8. @Info_in_bot — найдет номер телефона и ИНН, доступ дает не каждому, меняйте аккаунты\n9. dolg.xyz — находит связанные лица и государственные органы\n10. @SEARCHUA_bot — выдает досье где есть паспорт, адрес проживания, ФИО, автомобили, родственники, email, номера телефонов и много другого\n11. @The_New_Get_Contact_Bot — найдет номер телефона, можно вводить ФИ или любую другую фразу\n12. nomer-org.website — найдет полный адрес проживания и номер телефона, нужно указать город\n13. spravnik.com — найдет номер телефона, адрес регистрации, необходимо знать город\n14. <a href="http://ripsearch.youmust.click/ua/search.html">ripsearch.youmust.click</a> — поиск захороненных в Киеве, найдет дату рождения и смерти\n15. @info_baza_bot — найдет номера телефонов\n16. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text='🇦🇺 Aвстрaлии⁣'  ,state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Австралии\n\n1. personlookup.com.au — найдет адрес, телефон и соседей\n2. <a href="https://www.apps09.revenue.nsw.gov.au/erevenue/ucm/ucm_search.php">revenue.nsw.gov.au</a> — база невостребованных денег Нового Южного Уэльса, дает адрес проживания\n3. <a href="https://form.act.gov.au/smartforms/servlet/SmartForm.html?formCode=1219">form.act.gov.au</a> — база невостребованных денег ACT, дает адрес проживания\n4. <a href="https://www.pt.qld.gov.au/other-services/unclaimed-money/search-unclaimed-money/">pt.qld.gov.au</a>— база невостребованных денег Квинсленда, дает адрес проживания\n5. <a href="https://unclaimedmonies.treasury.wa.gov.au/ums/">wa.gov.au</a> — база невостребованных денег Западной Австралии, дает адрес проживания\n6. <a href="https://www.treasury.sa.gov.au/Our-services/unclaimed-money/search-for-unclaimed-money">sa.gov.au</a> — база невостребованных денег Южной Австралии, дает адрес проживания\n7, <a href="https://www.ancestry.com/search/collections/60525/">www.ancestry.com</a> — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений\n8. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇦🇹 Австрии⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Австрии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n3. www.northdata.com — найдет названия компаний в Европе с которыми связано ФИО\n4, <a href="https://www.ancestry.com/search/collections/60525/">www.ancestry.com</a> — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений\n5. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇦🇷 Аргентины",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Аргентины\n\n1</b>. <a href="https://www.cij.gov.ar/buscador-de-fallos.html">cij.gov.ar</a> — найдет судебные дела\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇧🇾 Бeларуси",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Республики Беларусь\n\n</b>1. mmnt.ru — найдет упоминания в документах\n2. spra.vkaru.net — телефонный справочник\n3. <a href="http://www.portal.nalog.gov.by/grp/#!fl">portal.nalog.gov.by</a> — найдет сведения из гос. реестра плательщиков, такие как УНП и код инспекции\n4. <a href="http://service.court.by/ru/account/login?returnUrl=%2Fru%2Fjuridical%2Fjudgmentresults">service.court.by</a> (r) — найдет судебные постановления, при регистрации нет проверки данных\n5. <a href="https://bankrot.gov.by/Debtors/DebtorsList/">bankrot.gov.by</a> — поиск в списках должников\n6. <a href="http://mtkrbti.by/local/TL/Licence.nsf/WEBSearchView1?SearchView">mtkrbti.by</a> — поиск в базе готовых лицензий, найдет ФИО, адрес, почтовый индекс, УНП, номер транспортной лицензии, срок действия\n7. <a href="http://vinformer.su/#cmdt0472111827">mvd.gov.by</a> — поиск в базе розыска\n8. <a href="http://gr.rcheph.by/">gr.rcheph.by</a> — поиск в  сведениях о государственной регистрации товаров, найдет УНП, название предприятия и наименования продукта\n9. <a href="https://facebot.ru/belarus/">facebot.ru</a> — найдет фотографии\n10. <a href="http://egr.gov.by/egrn/index.jsp?content=Find">egr.gov.by</a> — поиск юридических лиц и индивидуальных предпринимателей в базе данных единого государственного регистра\n11. <a href="https://justbel.info/Liquidation/FindMyRequest">justbel.info</a> — покажет данные о ликвидации юридических лиц\n12. nomer-org.website — найдет полный адрес проживания и номер телефона, нужно указать город\n13. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇧🇷 Брaзилии",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Бразилии\n\n</b>1. <a href="https://sei.df.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php?acao_externa=protocolo_pesquisar&acao_origem_externa=protocolo_pesquisar&id_orgao_acesso_externo=0">sei.df.gov.br</a> — база юридических документов\n2. www.escavador.com — найдет резюме и судебные иски\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇧🇪 Бельгии⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Бельгии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. www.de1212.be — найдет номер телефона и адрес\n3. sanctionssearch.ofac.treas.gov — поиск в санкционном списке США\n4. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇧🇬 Болгарии⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Болгарии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://www.vivacom.bg/bg/residential/polezni-syveti/ukazatel/telefonni-nomera">vivacom.bg</a> — покажет адрес и телефон, необходимо знать город\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇬🇧 Великобритании⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Великобритании\n\n1. <a href="https://beta.companieshouse.gov.uk/search/officers">companieshouse.gov.uk</a> — коммерческий поиск, найдет дату рождения, национальность, компании и их адреса\n2. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n3. www.northdata.com — найдет названия компаний с которыми связано ФИО\n4. <a href="https://www.ancestry.com/search/collections/60525/">www.ancestry.com</a> — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений\n5. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇭🇺 Венгрии",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Венгрии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://www.telekom.hu/lakossagi/tudakozo">telekom.hu</a> — найдет номер телефона и адрес проживания\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇩🇪 Гeрмании",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Германии\n\n</b>1. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n2. <a href="https://personensuche.dastelefonbuch.de/">dastelefonbuch.de</a> — найдет данные из профилей социальных сетей\n3. northdata.de — находит должности в компаниях\n4. www.northdata.com — найдет названия компаний с которыми связано ФИО\n5, <a href="https://www.ancestry.com/search/collections/60525/">www.ancestry.com</a> — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений\n6. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇬🇷 Греции",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Греции\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇩🇰 Дании⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Дании\n\n1. <a href="https://datacvr.virk.dk/data/visninger?">datacvr.virk.dk</a> — найдет иностранный адрес\n2. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n3. <a href="https://statstidende.dk/messages">statstidende.dk</a> — поиск в юридических документах, найдет данные о смене жительства, некрологи и много всего полезного\n4. <a href="https://datacvr.virk.dk/data/">datacvr.virk.dk</a> — поиск в сведениях о зарегистрированных предпринимателях и компаниях\n5. <a href="https://www.krak.dk/">krak.dk</a> —найдет телефон, местоположение на карте и фото дома\n6. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇮🇳 Индии⁣⁣⁣⁣⁣⁣⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Индии\n\n</b>1. www.indianfinders.com — найдет возраст и город проживания\n2. <a href="http://www.contactofindia.com/index.php">www.contactofindia.com</a> — найдет город и название компании которой владеет гражданин\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇮🇪 Ирландии⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Ирландии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇮🇸 Исландии",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Исландии\n\n</b>1. ja.is — найдет данные людей и компаний\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇮🇹 Италии⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Италии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базу должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n3. <a href="https://www.paginebianche.it/">paginebianche.it</a> — найдет номер телефона и адрес\n4. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇨🇦 Канады",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Канады\n\n</b>1. <a href="https://justice.gov.bc.ca/cso/esearch/civil/partySearch.do">justice.gov.bc.ca</a> — находит судебные дела\n2.  <a href="https://www.canada411.ca/search/">www.canada411.ca</a> — возраст, номер телефона, адрнс и другое\n3. <a href="https://www.ancestry.com/search/collections/60525/">www.ancestry.com</a> — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений\n4. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇨🇾 Кипра⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Кипра\n\n</b>1. cylaw.org — поиск в базе правовой информации, найдет документы и записи\n2. <a href="http://www.diadiktion.com/diadiktiondirectory-whitepagescyprus.htm">diadiktion.com</a> — найдет номер телефона и адрес\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇰🇬 Kиргизии",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Киргизии\n\n</b>1. <a href="http://act.sot.kg/kg/search">act.sot.kg</a> — поиск в базе судебных документов, фамилию нужно ввести два раза, при первом поиске в Тарап 1 (первая сторона), а при втором в Тарап 2\n2. www.osoo.kg — поиск в реестре компаний, есть учредители, директора, адреса, доходы и контактные данные\n3. <a href="http://register.minjust.gov.kg/register/SearchAction.seam?logic=and&cid=204">minjust.gov.kg</a> — поиск в реестре компаний, находит базовую информацию об организации\n4. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇨🇳 Китaя",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Китая\n\n</b>1. @sgk123bot — найдет ID QQ, Weibo, email, нужно знать дату рождения\n2. <a href="https://s.weibo.com/user">s.weibo.com</a> — поиск по контенту из Weibo\n3. <a href="http://zxgk.court.gov.cn/zhzxgk">zxgk.court.gov.cn</a> — судебные дела, в которых упоминается определенное имя, фамилия или название компании\n4. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇱🇻 Лaтвии⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Лaтвии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇱🇹 Литвы⁣",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Литвы\n\n</b>1. spra.vkaru.net — телефонный справочник\n2. mmnt.ru — найдет упоминания в документах\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇱🇺 Люксeмбурга",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Люксeмбурга\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. www.northdata.com — найдет названия компаний с которыми связано ФИО\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇲🇹 Мальты",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Мальты\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="Еще ⁣➜",state=Fio.Q1 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>ФИО гражданина какой страны?\n</b>\nСтр. 2 из 2', reply_markup=fio_kb_2)
    await Fio.Q2.set()
    
@dp.message_handler(text="🇲🇩 Молдовы⁣⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Молдовы\n\n</b>1. spra.vkaru.net — телефонный справочник\n2. mmnt.ru — найдет упоминания в документах\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇳🇱 Нидерлaндов",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Нидерландов\n\n1.</b> <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n2. <a href="https://www.telefoonboek.nl/personen/">telefoonboek.nl</a> — найдет адрес и номер телефона\n3. <a href="https://www.detelefoongids.nl/">detelefoongids.nl</a> — находит номер телефона, адрес и местоположение на карте\n4. <a href="https://www.wiewaswie.nl/nl/zoeken/">wiewaswie.nl</a> — голландская генеалогическая база с 17 века\n5. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

    
@dp.message_handler(text="🇳🇴 Норвегии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Норвегии\n\n1. <a href="https://www.proff.no/rolles%C3%B8k?">proff.no</a> — поиск по ФИО, найдет город, год рождения, бизнес и роли в бизнесе\n2. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n3. gulesider.no — выдаст такие данные как телефон, местоположение на карте и фото дома\n4. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇳🇿 Новой Зеландии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Новой Зеландии\n\n</b>1. <a href="https://app.companiesoffice.govt.nz/companies/app/ui/pages/individual/search?">companiesoffice.govt.nz</a> — найдет компании, адрес места жительства\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇵🇱 Польши⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Польши\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. www.northdata.com — найдет названия компаний с которыми связано ФИО\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇵🇹 Португалии",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Португалии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇷🇴 Румынии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Румынии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n3. <a href="http://portal.just.ro/SitePages/acasa.aspx">portal.just.ro</a> — упоминания человека в юридических документах\n4. <a href="http://www.carte-telefoane.info/">carte-telefoane.info</a> — найдет индивидуальных предпринимателей их адрес и контактные данные\n5. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇸🇰 Словакии⁣⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Словакии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇸🇮 Словении⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Словении\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇺🇸 США⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданин США\n\n</b>1. whitepages.com — найдет контактную  и справочную информацию \n2. peekyou.com — найдет публичные записи, Facebook, Instagram, Twitter, Email и изображения\n3. fastpeoplesearch.com — аналог Whitepages\n4. <a href="https://www.truepeoplesearch.com/">truepeoplesearch.com</a> — найдет адрес, почту, бизнес, взаимосвязи и могое другое\n5. <a href="https://intelx.io/tools?tab=person">intelx.io</a> — создает ссылки на поисковые системы, которые находят людей\n6. spiderfoot.net (r) — автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию\n7. www.yasni.com — находит фото, телефонные номера и адреса, профили в соц. сетях, интересы и много еще чего полезного\n8. <a href="https://www.intelius.com/criminal-records/">intelius.com</a> — поиск в криминальной базе, найдет адрес, места работы, телефонные номера и покажет где учился человек\n9. <a href="https://clustrmaps.com/p/">clustrmaps.com</a> — находит адрес проживания, номер телефона, возраст, место работы, специальность и многое другое\n10. xlek.com — поиск в whois и публичных реестрах, найдет много подробностей\n11. <a href="https://www.courtlistener.com/">courtlistener.com</a> — найдет судебные дела\n12. <a href="https://www.theknot.com/registry/couplesearch">theknot.com</a> — свадебный реестр и веб-сайт пары, год и месяц вводить не обязательно\n13. registryfinder.com — реестр свадеб, выпускных и детей\n14. <a href="https://www.thebump.com/search">thebump.com</a> — реестр свадеб\n15. www.judyrecords.com — база судебных дела США\n16. <a href="https://www.cyberbackgroundchecks.com/name">cyberbackgroundchecks.com</a> — найдет адрес проживания, членов семьи, историю изменения и другое, вход на сайт разрешен только с IP адреса США\n17. littlesis.org — база данных, в которой подробно описаны связи между влиятельными людьми и организациями\n18. <a href="https://www.bop.gov/inmateloc/">www.bop.gov</a> — поиск в тюрьмах, найдет возраст, расу, дату освобождения и регистрационный номер\n19. <a href="http://inmateinfo.indy.gov/IML">inmateinfo.indy.gov</a> — поиск арестов, найдет дату рождения и освобождения, физические характеристики и другое\n20. staterecords.org — найдет возраст, штат и город, можно выбрать любой штат, потом будет поиск по всем сразу\n21. findagrave.com — найдет когда умер и где захоронен\n22, <a href="https://www.ancestry.com/search/collections/60525/">www.ancestry.com</a> — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений\n23. www.industrydocuments.ucsf.edu — поиск в документах отраслевых компаний по производству табака, пищи, химии, фармакологии\n24. gravelocator.cem.va.gov — ветераны, дата смерти и рождения, звание, крематорий\n25. <a href="https://www.melissa.com/v2/lookups/personator">melissa.com</a> — найдет дату рождения, адрес проживания, этнос и прочее\n26. radaris.com — выдаёт возраст, профили социальных сетей, судебные решения, адреса проживания и прочее \n27. /fullname — список ресурсов для поиска по ФИО гражданина любой страны\n\n\n<b>Восстановление доступа\n\n</b>1. <a href="https://netsecure.adp.com/ilink/pub/smsess/v3/forgot/theme.jsp">adp.com</a> — покажет часть email или номера телефона, название компании, ID аккаунта, необходимо ввести Email адрес или номер телефона')
    
@dp.message_handler(text="🇹🇷 Турции",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Турции\n\n</b>1. <a href="http://www.ttrehber.turktelekom.com.tr/?type=white">turktelekom.com.tr</a> — найдет компании и людей с номером телефона и адресом\n2. <a href="http://emsal.uyap.gov.tr/BilgiBankasiIstemciWeb/">emsal.uyap.gov.tr</a> — поиск в судебный делах\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇹🇯 Таджикистанa",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Таджикистана\n\n</b>1.<a href="https://andoz.tj/Fehrist/SI?culture=ru-RU"> andoz.tj</a> — найдет сведения о регистрации индивидуальных предпринимателей\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇺🇿 Узбекистана",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Узбекистана\n\n</b>1. lex.uz — поиск в базе судебных документов\n2. orginfo.uz — найдет компании гражданина\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇫🇷 Франции⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Франции\n\n</b>1. <a href="https://dirigeants.bfmtv.com/recherche/">dirigeants.bfmtv.com</a> — найдет дату рождения, мандаты и бизнес\n2. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n3. <a href="http://copainsdavant.linternaute.com/s/?advsrch">copainsdavant.linternaute.com</a> — найдет школу, фото, друзей, место рождения\n4. <a href="https://www.pagesjaunes.fr/pagesblanches/">www.pagesjaunes.fr</a> — найдет номер телефона и адрес проживания\n5. www.deces-en-france.fr — база смертей, найдет дату, место рождения и смерти\n6. <a href="https://francais-a-londres.org/u">francais-a-londres.org</a> — найдет ник, фото, адреса квартир аренды и прочее\n7. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')
    
@dp.message_handler(text="🇫🇮 Финляндии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Финляндии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

@dp.message_handler(text="🇭🇷 Хорватии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Хорватии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

@dp.message_handler(text="🇨🇿 Чехии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Чехии\n\n1. <a href="https://or.justice.cz/ias/ui/rejstrik-$osoba?p%3A%3Asubmit=x&.%2Frejstrik-%24osoba=&prijmeni=Ivanov&jmeno=&narozeni=&obec=&angazma=&soud=&polozek=50&jenPlatne=VSECHNY">justice.cz</a> — поиск в государственном реестре вовлеченных физических лиц, найдет дату рождения, адрес, ICQ, организации, сборник документов\n2. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n3. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n4. seznam.1188.cz — найдет адрес и телефон\n5. <a href="https://isir.justice.cz/isir/common/index.do">isir.justice.cz</a> — поиск в базе должников\n6. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

@dp.message_handler(text="🇨🇭 Швейцарии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Швейцарии\n\n1. <a href="https://www.moneyhouse.ch/de/search?activeMandates=true&tab=persons">moneyhouse.ch</a> — поиск в торговом реестре, найдет владения компаниями, город проживания\n2. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n3. <a href="https://ti.chregister.ch/cr-portal/suche/suche.xhtml">ti.chregister.ch</a> — найдет организации принадлежащие этому человеку\n4. www.northdata.com — найдет названия компаний с которыми связано ФИО\n5. <a href="https://www.local.ch/en/tel">www.local.ch</a> — поиск в реестре бизнесов, найдет сайт, адрес, телефон, фото\n6. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

@dp.message_handler(text="🇸🇪 Швеции⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Швеции\n\n1. hitta.se — найдет адрес проживания, номер телефона, сожителей\n2. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n3. <a href="https://www.eniro.se/">eniro.se</a> — найдет телефон, местоположение на карте и фото дома.\n4. <a href="https://www.upplysning.se/">upplysning.se</a> — поиск в базе граждан и компаний, находит контактные данные людей и компаний\n5, <a href="https://www.ancestry.com/search/collections/60525/">www.ancestry.com</a> — найдет когда умер и где захоронен, есть поиск в реестре браков и рождений\n6. mrkoll.se — найдет дату рождения, адрес, ФИО соседей, номер социального страхования, номера телефонов, корпоративное участие, примерный доход, история изменений ФИО\n7. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

@dp.message_handler(text="🇪🇪 Эстoнии⁣",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по ФИО гражданина Эстонии\n\n1. <a href="https://tva-recherche.lu/recherche/">tva-recherche.lu</a> — найдет номер НДС, адрес и многое другое\n2. <a href="https://e-justice.europa.eu/contentPresentation.do?plang=en&idTaxonomy=246&m=1">e-justice.europa.eu</a> — поиск в базе должников, найдет идентификатор случая, идентификационный номер компании, дату рождения, персональный идентификационный номер, адрес и статус дела\n3. <a href="https://www.teatmik.ee/ru/advancedsearch/private">teatmik.ee</a> — найдет дату рождения, юр. лица, деловую сеть\n4. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')



@dp.message_handler(text="🇰🇷 Южнoй Кореи",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Южной</b> Кореи\n\n1. <a href="https://people.search.naver.com/">people.search.naver.com</a> — найдет фото, места учебы и работы, с кем состоит в браке, дата и место рождения\n2. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

@dp.message_handler(text="🇯🇵 Японии",state=Fio.Q2 )
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по ФИО гражданина Японии\n\n</b>1. <a href="http://www.courts.go.jp/app/hanrei_jp/search2">courts.go.jp</a> — поиск по судам\n2. jpon.xyz —  найдет номер телефона и адрес\n3. /fullname — список ресурсов для поиска по ФИО гражданина любой страны')

