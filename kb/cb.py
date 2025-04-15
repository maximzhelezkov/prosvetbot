from boot import bot, dp, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import MessageNotModified 
from db.dbcon import db_add_info, db_get_info
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from data.txt import START_MESSAGE, MENUB1_MESSAGE, MENUB4_MESSAGE, MENUB41_MESSAGE, MENUB111_MESSAGE, ADMIN_PANEL_MESSAGE
from kb.kb import timeikb, menuikb, menuikb1, menuikb4, studioikb1, callback_data_map, forwardikb, menuikb2, back3, back5, adminikb
from boot import storage
from data.config import chat_log_id, admin_id

user_selected_date = {}
user_selected_times = {}
user_selected_month = {}

def time_keyboard(user_id):
    hours = list(range(1, 25))
    selected = user_selected_times.get(user_id, [])

    ikb = InlineKeyboardMarkup(row_width=5)
    for i in range(0, len(hours), 4):
        row = []
        for hour in hours[i:i+4]:
            text = f"\u2705 {hour}:00" if hour in selected else f"{hour}:00"
            row.append(InlineKeyboardButton(
                text,
                callback_data=f"time_{hour}"))
        ikb.row(*row)
        
        
    ikb.add(back3)
    return ikb

@dp.callback_query_handler(lambda cb: cb.data == 'smenu')
async def smenu(call: CallbackQuery):
        await bot.edit_message_text(
        chat_id=call.message.chat.id, 
        text=START_MESSAGE, 
        reply_markup=menuikb,
        message_id=call.message.message_id)

@dp.callback_query_handler(lambda cb: cb.data == 'adminb1')
async def adminb1(call: CallbackQuery):
    if call.from_user.id in admin_id:
        info = db_get_info()
        if not info:
            await bot.send_message(chat_id=call.message.chat.id, text="Брони нет")
            return
        for row in info:
            id, user_id, username, name, number, selected_date, month, time_str = row
            message = (
                f"<b>ID:</b> <code>{id}</code>\n"
                f"<b>user_id:</b> <code>{user_id}</code>\n"
                f"<b>username:</b> @{username if username else 'none'}\n"
                f"<b>Имя:</b> {name}\n"
                f"<b>Номер:</b> {number}\n"
                f"<b>Дата:</b> {selected_date}.{month}\n"
                f"<b>Время:</b> {time_str}"
            )
            userikb = InlineKeyboardMarkup(row_width=1)
            userb = InlineKeyboardButton("Профиль", 
                                        url=f'tg://user?id={user_id}')
            userikb.add(userb)
            await bot.send_message(chat_id=call.message.chat.id, 
                                   text=message,
                                   reply_markup=userikb)
        await bot.send_message( chat_id=call.message.chat.id,
                                text="Выше вся бронь и информация о ней на данный момент",
                                reply_markup=back5)

@dp.callback_query_handler(lambda cb: cb.data == 'adminb2')
async def adminb2(call: CallbackQuery):  
    await call.answer(text="Пока не доступно...", show_alert=True)

# @dp.callback_query_handler(lambda cb: cb.data == 'adminb3')
# async def adminb3(call: CallbackQuery):  


@dp.callback_query_handler(lambda cb: cb.data == 'menub1')
async def callback_menub1(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=MENUB1_MESSAGE, 
                                reply_markup=menuikb1, 
                                disable_web_page_preview=True)

@dp.callback_query_handler(lambda cb: cb.data == 'back1')
async def callback_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, 
                                text=START_MESSAGE, 
                                reply_markup=menuikb)

@dp.callback_query_handler(lambda cb: cb.data == 'back2')
async def callback_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(chat_id=call.message.chat.id, 
                                text=START_MESSAGE, 
                                reply_markup=menuikb)


@dp.callback_query_handler(lambda cb: cb.data == 'menub11')
async def callback_menub11(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.delete_message(chat_id=call.message.chat.id, 
                             message_id=call.message.message_id)
    await bot.send_message(chat_id=call.message.chat.id,
                           text=MENUB111_MESSAGE,
                           disable_web_page_preview=True)
    await bot.send_location(chat_id=call.message.chat.id, 
                            latitude=55.788208, 
                            longitude=37.582715,
                            reply_markup=menuikb2)
    
@dp.callback_query_handler(lambda cb: cb.data == 'menub4')
async def callback_menub4(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=MENUB4_MESSAGE, 
                                reply_markup=menuikb4)

@dp.callback_query_handler(lambda cb: cb.data == 'adminikb')
async def callback_menub1(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=ADMIN_PANEL_MESSAGE, 
                                reply_markup=adminikb)

@dp.callback_query_handler(lambda cb: cb.data == 'studio')
async def callback_studio(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Выберите дату:",
                                reply_markup=studioikb1)


@dp.callback_query_handler(lambda cb: cb.data.startswith("sb21_"))
async def time1(call: CallbackQuery):
    user_id = call.from_user.id
    _, day, month = call.data.split('_')
    user_selected_date[user_id] = day
    user_selected_month[user_id] = month
    user_selected_times[user_id] = []

    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f"\U0001F4C5 Дата выбрана: {day}.{month} \nТеперь выберите время начала и окончания аренды:",
                                reply_markup=time_keyboard(user_id))
    
@dp.callback_query_handler(lambda cb: cb.data.startswith("sb22_"))
async def time2(call: CallbackQuery):
    user_id = call.from_user.id
    _, day, month = call.data.split('_')
    user_selected_date[user_id] = day
    user_selected_month[user_id] = month
    user_selected_times[user_id] = []

    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f"\U0001F4C5 Дата выбрана: {day}.{month} \nТеперь выберите время начала и окончания аренды:",
                                reply_markup=time_keyboard(user_id))

@dp.callback_query_handler(lambda cb: cb.data.startswith("sb23_"))
async def time3(call: CallbackQuery):
    user_id = call.from_user.id
    _, day, month = call.data.split('_')
    user_selected_date[user_id] = day
    user_selected_month[user_id] = month
    user_selected_times[user_id] = []

    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f"\U0001F4C5 Дата выбрана: {day}.{month} \nТеперь выберите время начала и окончания аренды:",
                                reply_markup=time_keyboard(user_id))


@dp.callback_query_handler(lambda cb: cb.data.startswith("sb24_"))
async def time4(call: CallbackQuery):
    user_id = call.from_user.id
    _, day, month = call.data.split('_')
    user_selected_date[user_id] = day
    user_selected_month[user_id] = month
    user_selected_times[user_id] = []

    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"\U0001F4C5 Дата выбрана: {day}.{month} \nТеперь выберите время начала и окончания аренды:",
        reply_markup=time_keyboard(user_id)
    )

@dp.callback_query_handler(lambda cb: cb.data.startswith('time_'))
async def time(call: CallbackQuery):
    user_id = call.from_user.id
    hour = int(call.data.replace('time_', ''))

    selected = user_selected_times.get(user_id, [])

    if hour in selected:
        selected.remove(hour)
    elif len(selected) < 2:
        selected.append(hour)
    else:
        await bot.answer_callback_query(call.id, text="Выберите не более двух времён")
        return

    selected.sort()
    user_selected_times[user_id] = selected

    await bot.answer_callback_query(call.id)
    try:
        await bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=time_keyboard(user_id))
    except MessageNotModified:
        pass

    if len(selected) == 2:
        start, end = selected
        date = user_selected_date.get(user_id, 'не выбрана')
        month = user_selected_month.get(user_id, ' не выбрана')
        total_hours = end - start
        if total_hours == 11:
            price = 50000
        elif total_hours == 23:
            price = 90000
        elif total_hours >= 12:
            price = total_hours * 4000
        else:
            price = total_hours * 4500
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"""\u2705 Вы выбрали:\nДата: {date}.{month}\nВремя: с {start}:00 до {end}:00\nПримерная цена: {price} руб.\nИтоговая цена может отличатся, <a href='https://pravdaprosvet.ru/rooles'>почитать правила можно тут</a>""",
            reply_markup=timeikb,
            disable_web_page_preview=True)

@dp.callback_query_handler(lambda cb: cb.data in callback_data_map)
async def callback_stb(call: CallbackQuery):
    text, markup= callback_data_map.get(call.data, (None, None))
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=text, 
                                reply_markup=markup)


class Form(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_msg = State()

@dp.callback_query_handler(lambda cb: cb.data == 'forward')
async def callback_forward(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text="Теперь нам нужны контактные данные\nПожалуйста, введите ваше фио:", 
                                reply_markup=forwardikb)

    await Form.waiting_for_name.set()

@dp.message_handler(state=Form.waiting_for_name)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.waiting_for_phone.set()
    await message.answer("Введите ваш номер телефона:")


async def about_buyer(user_id, name, phone, month, selected_date, time_str):
    userikb = InlineKeyboardMarkup(row_width=1)
    userb = InlineKeyboardButton("Профиль", 
                                 url=f'tg://user?id={user_id}')
    userikb.add(userb)
    await bot.send_message(chat_id=chat_log_id,
                           text=f"""
#Новая_бронь
Дата: {selected_date}.{month} {time_str}

Контактные данные:
ID: <code>{user_id}</code>
Имя: <code>{name}</code>
Номер: <code>{phone}</code>""",
                            reply_markup=userikb)

@dp.message_handler(state=Form.waiting_for_phone)
async def get_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text 
        selected_date = user_selected_date.get(message.from_user.id, 'не выбрана')
        selected_month = user_selected_month.get(message.from_user.id, 'неизвестен')
        selected_times = user_selected_times.get(message.from_user.id, [])
        time_str = "с " + ":00 до ".join([str(hour) for hour in selected_times]) + ":00" if selected_times else "не выбрано"

    user_id = message.from_user.id
    name = data['name']
    phone = data['phone']


    await message.answer(
        f"Спасибо! Ваши данные сохранены. \nИмя: {name}\nТелефон: {phone}\nДата: {selected_date}.{selected_month}\nВремя: {time_str}.\nМы с вами свяжемся", 
        reply_markup=ReplyKeyboardRemove()
    )
    db_add_info(name, phone, selected_date, time_str, selected_month, user_id)
    await about_buyer(user_id, name, phone, selected_month, selected_date, time_str)
    await state.finish()
    user_selected_times.pop(user_id, None)
    user_selected_date.pop(user_id, None)
    user_selected_month.pop(user_id, None)