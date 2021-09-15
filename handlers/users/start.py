from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Text

from loader import dp
from keyboards.default.menu import global_menu
from aiogram.types import Message

from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: Message, state: FSMContext ):
    await message.answer('<b>ОПИСАНИЕ\n\n</b>Бот содержит в себе каталог из бесплатных ресурсов (сайты, приложения, боты, методы) которые по известным вам данным выдают информацию из открытых источников. \n\n\n<b>НАВИГАЦИЯ\n\n</b>Используйте кнопки под полем ввода текста.\n\n\n<b>УКАЗАТЕЛИ\n\n</b>В конце некоторых ссылок в скобках указаны буквы:\n\n(r) — требуется регистрация на ресурсе\n(t) — программа, устанавливается на устройство\n(a) — приложение на Android или iOS.\n\n\n<b>КОНФИДЕНЦИАЛЬНОСТЬ\n\n</b>Сведения пользователей и того что они отправляют боту приватны.\n\n\nЧто известно?', reply_markup=global_menu)
    await state.finish()




#@dp.message_handler()
#async def bot_echo(message: types.Message):
#    await message.answer(f"🚫 Не отправляй сообщений боту\n\n"
#                         f"Бот не ищет за тебя, а даёт ссылки на ресурсы для поиска.\n\n"

#                         f"Если нет меню, то обнови его командой /start.")



@dp.message_handler(text='🔙 Назад',state='*')
async def bot_start(message: Message, state: FSMContext ):
    await message.answer(f'Что известно?', reply_markup=global_menu)
    await state.finish()