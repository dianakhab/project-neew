from aiogram.types import KeyboardButton, InlineKeyboardMarkup

inline_kb = InlineKeyboardMarkup(row_width=2)
inline_btn_1 = InlineKeyboardButton('Кнопка 1', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Кнопка 2', callback_data='button2')
inline_kb.add(inline_btn_1, inline_btn_2)

@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=inline_kb)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы нажали на кнопку 1')

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы нажали на кнопку 2')

menu_kb = InlineKeyboardMarkup(row_width=1)
menu_btn_1 = InlineKeyboardButton('Опция 1', callback_data='menu1')
menu_btn_2 = InlineKeyboardButton('Опция 2', callback_data='menu2')
menu_kb.add(menu_btn_1, menu_btn_2)

@dp.message_handler(commands=['start'])
async def show_main_menu(message: types.Message):
    await message.reply("Главное меню:", reply_markup=menu_kb)

@dp.callback_query_handler(lambda c: c.data == 'menu1')
async def process_menu1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали опцию 1')

@dp.callback_query_handler(lambda c: c.data == 'menu2')
async def process_menu2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали опцию 2')