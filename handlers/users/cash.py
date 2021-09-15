from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from keyboards.default.dop_kb import dop_kb
from loader import dp
from keyboards.default.account_kb import account_kb_1, account_kb_2, vk_kb
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from states.states import Cash
from keyboards.default.cash_kb import cash_kb, cripto_kb, cash2_kb, cash3_kb, cash4_kb




@dp.message_handler(text="Номер кошелька")
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer("К каким категориям данные относятся?", reply_markup=cash_kb)
    await Cash.Q1.set()
    

@dp.message_handler(text='Криптокошельки⁣⁣⁣⁣⁣⁣', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Кошелек какой криптовалюты?', reply_markup=cripto_kb)
    await Cash.Q2.set()
    
    
@dp.message_handler(text='BTC⁣⁣⁣⁣⁣⁣', state=Cash.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по адресу крипто кошелька Bitcoin\n\n</b>1. <a href="https://intelx.io/tools?tab=bitcoin">intelx.io</a> — найдет упоминания в утечках и БД\n2. www.blockchain.com — покажет все транзакции\n3. live.blockcypher.com — покажет все транзакции\n4. blockchair.com — покажет все транзакции\n5. <a href="http://maltego.com/downloads/">maltego</a> (t) — визуальное представление и анализ транзакций\n6. oxt.me (r) — визуальное представление и анализ транзакций в браузере, не работает мобильная версия\n7. <a href="https://learnmeabitcoin.com/tools/path/">learnmeabitcoin.com</a> — цепочка транзакций между двумя кошельками\n8. addresschecker.eu — загружаете список адресов и получаете таблицу с данными текущего баланса за все время\n9. blockpath.com — покажет транзакции кошелька в виде графа, можно добавлять несколько адресов\n10. @cryptoaml_bot — узнает источники поступления средств на крипто кошелёк и дает оценку риска, 1 бесплатный поиск на аккаунт\n\n\n<b>Инструменты\n\n</b>1. <a href="https://cryptocurrencyalerting.com/wallet-watch.html">cryptocurrencyalerting.com</a> (r) — следит за изменениями баланса кошелька, отправляет уведомление на Email, SMS, Discord или в Telegram')
    
    
    
@dp.message_handler(text='ETH⁣⁣⁣⁣⁣⁣', state=Cash.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по адресу крипто кошелька Ethirium\n\n</b>1. etherchain.org — анализ Ethereum адреса\n2. etherscan.io — анализ Ethereum адреса\n3. blockchair.com — информация о транзакциях\n\n\n<b>Инструменты\n\n</b>1. <a href="https://cryptocurrencyalerting.com/wallet-watch.html">cryptocurrencyalerting.com</a> (r) — следит за изменениями баланса кошелька, отправляет уведомление на Email, SMS, Discord или в Telegram')
    
    
    
@dp.message_handler(text='DASH⁣⁣⁣⁣⁣⁣', state=Cash.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по адресу крипто кошелька Dash\n\n</b>1. <a href="https://live.blockcypher.com/dash/">live.blockcypher.com</a> — информация о транзакциях\n2. blockchair.com — информация о транзакциях')
    
 
 
@dp.message_handler(text='DOGE⁣⁣⁣⁣⁣⁣', state=Cash.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Поиск по адресу крипто кошелька DogeCoin\n\n1.<a href="https://live.blockcypher.com/doge/"> live.blockcypher.com</a> — информация о транзакциях\n2. blockchair.com — информация о транзакциях')
    
@dp.message_handler(text='LTC⁣⁣⁣⁣⁣⁣', state=Cash.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по адресу крипто кошелька Litecoin\n\n</b>1. <a href="https://live.blockcypher.com/ltc/">live.blockcypher.com</a> — информация о транзакциях\n2. blockchair.com — информация о транзакциях')
 
@dp.message_handler(text='Другой⁣⁣⁣⁣⁣⁣', state=Cash.Q2)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Для кошельков с криптовалютой</b>\n\ncoin360.com — ссылки на ресурсы поиска транзакций кошелька, для каждой криптовалюты есть пункт explorers и там ссылка на сайт по поиску транзакций')
    
 
    
@dp.message_handler(text='Платёжные системы⁣⁣⁣⁣⁣⁣', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Данные кошелька какой платежной системы?', reply_markup=cash2_kb)
    
    
    
@dp.message_handler(text='Webmoney⁣⁣⁣⁣⁣⁣', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по данным аккаунта Webmoney\n\n</b>1. <a href="https://passport.webmoney.ru/asp/VerifyWMID.asp">passport.webmoney.ru</a> — поиск по WM идентификатору или кошельку, покажет инфо о кошельке webmoney\n\n\n<b>Через URL\n\n1</b>. https://arbitrage.webmoney.ru/asp/claims.asp?wmid=1234567890 — претензии, отзывы, иски аккаунта, замените <code>1234567890</code> на WMID кошелька\n2. https://passport.webmoney.ru/asp/CertviewSu.asp?wmid=1234567890 — покажет статус обслуживания, замените <code>1234567890</code> на WMID кошелька')
    
    
@dp.message_handler(text='Venmo⁣⁣⁣⁣⁣⁣', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по данным аккаунта Venmo\n\n</b>1. <a href="https://github.com/sc1341/Venmo-OSINT">Venmo-OSINT</a> (t) — найдет транзакции пользователя')
    
@dp.message_handler(text='Номер банковской карты⁣⁣⁣⁣⁣⁣', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Карта какого банка?', reply_markup=cash3_kb)

@dp.message_handler(text='Любого⁣⁣⁣⁣⁣⁣', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Поиск по номеру на пластиковой карте любого банка\n\n</b>1<b>.</b> binlist.net — определит к какому банку принадлежит карта\n2. bindb.com — определит к какому банку принадлежит карта\n3. <a href="https://github.com/josh0xA/Scylla">Scylla</a> (t) — найдет упоминания номера карты в утечках', reply_markup=dop_kb)
    
    
#  @dp.message_handler(text= '🇺🇦 Украины',state=Cash.Q1)
# async def get_phone_menu(message: Message, state: FSMContext):
#     await message.answer('', reply_markup=account_kb_2)
    
 
@dp.message_handler(text='Дополнительныe методы⁣⁣⁣⁣⁣', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('Дополнительныe методы⁣⁣⁣⁣⁣', reply_markup=cash4_kb)
    
@dp.message_handler(text='Найти номер телефона или логин', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>Номер телефона по номеру пластиковой карты любого банка\n\n<i></b>Не работает с картой Qiwi, Sberbank, Alpha, Россельхозбанк, ЮMoney\n\n</i>[1] Открой www.card2card.kz\n[2] Где "Отправитель" введи карту номер телефона которой хочешь узнать. А CVC и срок действия укажи любой\n[3] Где  "Получатель" укажи всякую карту, например <code>4893 4704 7283 6532\n</code>[4] Введи различную сумму и нажми перевести\n\nОткроется сайт 3DS где указывается часть номера телефона и в редких случаях логин или email.')
    
@dp.message_handler(text='Найти ФИО', state=Cash.Q1)
async def get_phone_menu(message: Message, state: FSMContext):
    await message.answer('<b>ФИО по номеру пластиковой карты любого банка\n\n</b>[1] Определи банк карты. Найди приложение этого банка или сайт. На нем отправь деньги на эту карту.')
    
 