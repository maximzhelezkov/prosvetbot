from boot import bot, dp, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from db.dbcon import db_add_info
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from data.txt import START_MESSAGE, MENUB1_MESSAGE, MENUB4_MESSAGE, MENUB41_MESSAGE
from kb.kb import timeikb, menuikb, menuikb1, menuikb4, studioikb1, callback_data_map, forwardikb, hallikb
from boot import storage
from data.config import chat_log_id

user_selected_date = {}
user_selected_times = {}
user_selected_hall = {}

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

@dp.callback_query_handler(lambda cb: cb.data == 'menub11')
async def callback_menub11(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.send_location(chat_id=call.message.chat.id, 
                            latitude=55.788208, 
                            longitude=37.582715)
    
@dp.callback_query_handler(lambda cb: cb.data == 'menub4')
async def callback_menub4(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=MENUB4_MESSAGE, 
                                reply_markup=menuikb4)


@dp.callback_query_handler(lambda cb: cb.data == 'studio')
async def callback_studio(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Выберите зал:",
                                reply_markup=hallikb)

@dp.callback_query_handler(lambda cb: cb.data.startswith('hall_'))
async def hall_selected(call: CallbackQuery):
    user_id = call.from_user.id
    hall = call.data.replace('hall_', '')
    user_selected_hall[user_id] = hall

    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f"Вы выбрали зал: {hall.capitalize()}. Теперь выберите дату:",
                                reply_markup=studioikb1)

@dp.callback_query_handler(lambda cb: cb.data.startswith("sb24"))
async def time(call: CallbackQuery):
    user_id = call.from_user.id
    day = call.data.replace("sb24", "")
    user_selected_date[user_id] = day
    user_selected_times[user_id] = []

    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f"\U0001F4C5 Дата выбрана: {day} \nТеперь выберите время:",
                                reply_markup=time_keyboard(user_id))

def time_keyboard(user_id):
    hours = list(range(9, 22))
    selected = user_selected_times.get(user_id, [])

    ikb = InlineKeyboardMarkup(row_width=3)
    for i in range(0, len(hours), 4):
        row = []
        for hour in hours[i:i+4]:
            text = f"\u2705 {hour}:00" if hour in selected else f"{hour}:00"
            row.append(InlineKeyboardButton(
                text,
                callback_data=f"time_{hour}"))
        ikb.row(*row)

    return ikb

@dp.callback_query_handler(lambda cb: cb.data.startswith('time_'))
async def time2(call: CallbackQuery):
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

    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=time_keyboard(user_id))

    if len(selected) == 2:
        start, end = selected
        date = user_selected_date.get(user_id, 'не выбрана')
        hall = user_selected_hall.get(user_id, 'не выбран')
        total_hours = end - start
        price = total_hours * 3500
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"""\u2705 Вы выбрали:\nЗал: {hall.capitalize()}\nДата: {date}.04\nВремя: с {start}:00 до {end}:00\nПримерная цена: {price} руб.\nИтоговая цена может отличатся, <a href='https://pravdaprosvet.ru/rooles'>почитать правила можно тут</a>""",
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

@dp.callback_query_handler(lambda cb: cb.data == 'forward')
async def callback_forward(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text="Теперь нам нужны контактные данные\nПожалуйста, введите ваше имя:", 
                                reply_markup=forwardikb)

    await Form.waiting_for_name.set()

@dp.message_handler(state=Form.waiting_for_name)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.waiting_for_phone.set()
    await message.answer("Введите ваш номер телефона:")


async def about_buyer(user_id, name, phone, month, selected_date, time_str, hall):
    userikb = InlineKeyboardMarkup(row_width=1)
    userb = InlineKeyboardButton("Профиль", url=f'tg://user?id={user_id}')
    userikb.add(userb)
    await bot.send_message(chat_id=chat_log_id,
                            text=f"""
Новая бронь на зал {hall}
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
        selected_times = user_selected_times.get(message.from_user.id, [])
        time_str = "с " + ":00 до ".join([str(hour) for hour in selected_times]) + ":00" if selected_times else "не выбрано"
        hall = user_selected_hall.get(message.from_user.id, 'не выбран')

    user_id = message.from_user.id
    name = data['name']
    phone = data['phone']
    month = "04"

    db_add_info(name, phone, selected_date, time_str, month, hall, user_id)

    await message.answer(f"Спасибо! Ваши данные сохранены.\nЗал: {hall} \nИмя: {name}\nТелефон: {phone}\nДата: {selected_date}.{month}\nВремя: {time_str}.\nМы с вами свяжемся", reply_markup=ReplyKeyboardRemove())
    await about_buyer(user_id, name, phone, month, selected_date, time_str, hall)
    await state.finish()
    user_selected_times.pop(user_id, None)
    user_selected_date.pop(user_id, None)
    user_selected_hall.pop(user_id, None)
