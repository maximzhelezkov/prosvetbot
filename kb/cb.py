from boot import bot, dp, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import MessageNotModified 
from db.dbcon import db_add_info, db_get_info
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from data.txt import START_MESSAGE, MENUB1_MESSAGE, MENUB4_MESSAGE, MENUB41_MESSAGE,EQP_ABOUT_MESSAGE, MENUB111_MESSAGE, ADMIN_PANEL_MESSAGE, MENU4_MESSAGE, MENU44_MESSAGE, MENU3_MESSAGE, ABOUT_STUDIO_MESSAGE
from kb.kb import timeikb,back4, menuikb, menuikb1p1, menuikb1p2 , preferenceikb, abouteqbikb ,studioikb1, about_studioikb, callback_data_map, forwardikb, backikb2, backikb1,menuikb1p2p2 ,menuikb1p4, back3, back5, menuikb1p3,menuikb2p4, adminikb, studioikb21, studioikb22, studioikb23, studioikb24, studioikb25, studioikb26, studioikb27, studioikb28, studioikb29, studioikb210, studioikb211, studioikb212
from boot import storage
from datetime import datetime
from data.config import chat_log_id, admin_id
import re

#-=Хранить данные перед записью в дб=-

user_selected_date = {}
user_selected_times = {}
user_selected_month = {}
user_selected_days = {}

#-=Классы=-

class Form(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_msg = State()

class PassForm(StatesGroup):
    waiting_for_date = State()
    waiting_for_car_plate = State()
    waiting_for_full_name = State()
    waiting_for_phone = State()

class EquipmentForm(StatesGroup):
    waiting_for_equipment_list = State()
    waiting_for_date = State()
    waiting_for_full_name = State()
    waiting_for_phone = State()

#-=Старт=-

@dp.callback_query_handler(lambda cb: cb.data == 'smenu')
async def smenu(call: CallbackQuery):
        await bot.edit_message_text(
        chat_id=call.message.chat.id, 
        text=START_MESSAGE, 
        reply_markup=menuikb,
        message_id=call.message.message_id)


#-=Админ панель=-

@dp.callback_query_handler(lambda cb: cb.data == 'adminikb')
async def callback_menub1(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=ADMIN_PANEL_MESSAGE, 
                                reply_markup=adminikb)


@dp.callback_query_handler(lambda cb: cb.data == 'adminb1')
async def adminb1(call: CallbackQuery):
    if call.from_user.id in admin_id:
        info = db_get_info()
        if not info:
            await bot.send_message(chat_id=call.message.chat.id, text="Брони нет")
            return
        for row in info:
            id, user_id, username, name, number, selected_date, time_str = row
            date_str = ' — '.join(f"{d}.{m}" for d, m in selected_date)
            message = (
                f"<b>ID:</b> <code>{id}</code>\n"
                f"<b>user_id:</b> <code>{user_id}</code>\n"
                f"<b>username:</b> @{username if username else 'none'}\n"
                f"<b>Имя:</b> {name}\n"
                f"<b>Номер:</b> {number}\n"
                f"<b>Дата:</b> {date_str}\n"
                f"<b>Время:</b> {time_str}\n"
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


#-=Цепочка menub1=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub1')
async def callback_menub1(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=MENUB4_MESSAGE, 
                                reply_markup=menuikb1p1)

@dp.callback_query_handler(lambda cb: cb.data == 'back1')
async def callback_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, 
                                text=START_MESSAGE, 
                                reply_markup=menuikb)

@dp.callback_query_handler(lambda cb: cb.data == 'about_studio')
async def callback_studio(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=ABOUT_STUDIO_MESSAGE,
                                reply_markup=about_studioikb)

@dp.callback_query_handler(lambda cb: cb.data == 'studio')
async def callback_studio(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Выберите месяц:",
                                reply_markup=studioikb1)

@dp.callback_query_handler(lambda cb: cb.data == 'studio11')
async def callback_studio(call: CallbackQuery):
    user_id = call.from_user.id
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Выберите месяц:",
                                reply_markup=studioikb1)
    user_selected_times.pop(user_id, None)
    user_selected_date.pop(user_id, None)
    user_selected_month.pop(user_id, None)
    user_selected_days.pop(user_id, None)

def get_studio_keyboard(studio_code):
    return {
        "sb21": studioikb21,
        "sb22": studioikb22,
        "sb23": studioikb23,
        "sb24": studioikb24,
        "sb25": studioikb25,
        "sb26": studioikb26,
        "sb27": studioikb27,
        "sb28": studioikb28,
        "sb29": studioikb29,
        "sb210": studioikb210,
        "sb211": studioikb211,
        "sb212": studioikb212
    }.get(studio_code)

@dp.callback_query_handler(lambda cb: cb.data.startswith("sb2"))
async def select_date_handler(call: CallbackQuery):
    user_id = call.from_user.id
    try:
        studio_code, day, month = call.data.split('_')
    except ValueError:
        await bot.answer_callback_query(call.id, text="Ошибка данных", show_alert=True)
        return

    selected_dates = user_selected_date.get(user_id, [])

    if not selected_dates:
        user_selected_date[user_id] = [(day, month)]
        await bot.answer_callback_query(call.id)
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"\U0001F4C5 Дата выбрана: {day}.{month} \nВыберите вторую дату (или нажмите ту же дату снова для брони одного дня):",
            reply_markup=get_studio_keyboard(studio_code)
        )
    else:
        first_day, first_month = selected_dates[0]
        if (day, month) == (first_day, first_month):
            user_selected_date[user_id] = [(day, month), (day, month)]
        else:
            user_selected_date[user_id].append((day, month))
        date_str = ' — '.join(f"{d}.{m}" for d, m in selected_dates)
        formatted_dates = f"{date_str}"

        user_selected_times[user_id] = []

        await bot.answer_callback_query(call.id)
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"✅ Вы выбрали:\nДата: {formatted_dates}\n Выберите время в которое вы будете в студии: ",
            reply_markup=time_keyboard(user_id)
        )

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
        start_day, start_month = map(int, user_selected_date[user_id][0])
        end_day, end_month = map(int, user_selected_date[user_id][1])

        from datetime import date

        start_date = date(2025, start_month, start_day)
        end_date = date(2025, end_month, end_day)
        total_days = (end_date - start_date).days + 1
        total_hours = end - start
        total_hours2 = start + end

        price = 0
        print(total_days, total_hours)
        if total_days == 1:
            if total_hours == 12:
                price = 50000
            elif total_hours == 24:
                price = 90000
            elif total_hours > 12:
                price = total_hours * 4000
            else:
                price = total_hours * 4500
                
                formatted_dates = f"{start_day}.{start_month} — {end_day}.{end_month}"

                await bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=f"""\u2705 Вы выбрали:\nДата: {formatted_dates}\nВремя: с {start}:00 до {end}:00\nПримерная цена: {price} руб.\nИтоговая цена может отличаться, <a href='https://pravdaprosvet.ru/rooles'>почитать правила можно тут</a>""",
                    reply_markup=timeikb,
                    disable_web_page_preview=True)
    
        if total_days >= 2:
            if total_hours > 12:
                total_total = total_days * total_hours
                price += total_total * 4500
            else:
                total_total = total_days * total_hours
                price += total_total * 4000
        
        formatted_dates = f"{start_day}.{start_month} — {end_day}.{end_month}"

        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"""\u2705 Вы выбрали:\nДата: {formatted_dates}\nВремя: с {start}:00 до {end}:00\nПримерная цена: {price} руб.\nИтоговая цена может отличаться, <a href='https://pravdaprosvet.ru/rooles'>почитать правила можно тут</a>""",
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
    full_name = message.text.strip()
    if not re.match(r'^[А-Яа-яЁёA-Za-z\s\-]+$', full_name):
        await message.answer("⚠️ Пожалуйста, введите только буквы.")
        return
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.waiting_for_phone.set()
    await message.answer("Введите ваш номер телефона:\n\nПример: 89255125373")


async def about_buyer(user_id, name, phone, date_str, time_str):
    userikb = InlineKeyboardMarkup(row_width=1)
    userb = InlineKeyboardButton("Профиль", 
                                 url=f'tg://user?id={user_id}')
    userikb.add(userb)
    await bot.send_message(chat_id=chat_log_id,
                           text=f"""
#Новая_бронь
Дата: {date_str} {time_str}

Контактные данные:
ID: <code>{user_id}</code>
Имя: <code>{name}</code>
Номер: <code>{phone}</code>""",
                            reply_markup=userikb)

@dp.message_handler(state=Form.waiting_for_phone)
async def get_phone(message: types.Message, state: FSMContext):
    phone = message.text.strip().replace(" ", "")
    if not phone.isdigit() or len(phone) < 10:
        await message.answer("⚠️ Пожалуйста, введите корректный номер телефона (только цифры, минимум 10 знаков) Пример: 89255125373.")
        return
    async with state.proxy() as data:
        data['phone'] = message.text 
        selected_date = user_selected_date.get(message.from_user.id, 'не выбрана')
        date_str = ' — '.join(f"{d}.{m}" for d, m in selected_date)
        selected_times = user_selected_times.get(message.from_user.id, [])
        time_str = "с " + ":00 до ".join([str(hour) for hour in selected_times]) + ":00" if selected_times else "не выбрано"

    user_id = message.from_user.id
    name = data['name']
    phone = data['phone']


    await message.answer(
        f"Спасибо! Ваши данные сохранены. \nИмя: {name}\nТелефон: {phone}\nДата: {date_str}\nВремя: {time_str}.\nМы напишем вам в Телеграм", 
        reply_markup=backikb2)
    db_add_info(name, phone, date_str, time_str, user_id)
    await about_buyer(user_id, name, phone, date_str, time_str)
    await state.finish()
    user_selected_times.pop(user_id, None)
    user_selected_date.pop(user_id, None)
    user_selected_month.pop(user_id, None)
    user_selected_days.pop(user_id, None)

user_selected_times2= {}

def time_keyboard2():
    hours = list(range(1, 25))
    ikb2 = InlineKeyboardMarkup(row_width=4)
    for i in range(0, len(hours), 4):
        row = []
        for hour in hours[i:i+4]:
            text = f"{hour}:00"
            row.append(InlineKeyboardButton(
                text=text,
                callback_data=f"time2_{hour}"
            ))
        ikb2.row(*row)
    ikb2.add(back4)
    return ikb2

@dp.callback_query_handler(lambda cb: cb.data == 'equipment')
async def equipment(call: CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=EQP_ABOUT_MESSAGE,
        reply_markup=abouteqbikb)

@dp.callback_query_handler(lambda cb: cb.data == 'eqb')
async def start_equipment_form(call: CallbackQuery):
    user_id = call.from_user.id
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Выберите время начала бронирования:",
        reply_markup=time_keyboard2())
    user_selected_times2.pop(user_id, None)

@dp.callback_query_handler(lambda cb: cb.data.startswith('time2_'))
async def time2(call: CallbackQuery):
    user_id = call.from_user.id 
    hour = int(call.data.replace('time2_', ''))
    user_selected_times2[user_id] = (hour)
    await call.answer()
    await call.message.answer(text="📦 Впишите список оборудования \n\nПример: \nПрожектор Open Face ARRILITE;3шт, \nЗатенитель сетка SILK scrim;3шт,  \nДиммер бытовой 150W/500W/1000W;1шт:")
    await EquipmentForm.waiting_for_equipment_list.set()

@dp.message_handler(state=EquipmentForm.waiting_for_equipment_list)
async def get_equipment_list(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['equipment'] = message.text
    await message.answer("📅 Укажите дату брони (в формате ДД.ММ.ГГ):")
    await EquipmentForm.waiting_for_date.set()

@dp.message_handler(state=EquipmentForm.waiting_for_date)
async def get_equipment_date(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    date_str = message.text.strip()

    if not re.match(r"^\d{2}\.\d{2}\.\d{2}$", date_str):
        await message.reply("⚠️ Пожалуйста, введите дату в формате ДД.ММ.ГГ (например, 09.04.25).")
        return

    try:
        parsed_date = datetime.strptime(date_str, "%d.%m.%y")
        if parsed_date.date() < datetime.now().date():
            await message.reply("⚠️ Нельзя выбрать прошедшую дату. Введите корректную будущую дату.")
            return

    except ValueError:
        await message.reply("⚠️ Такой даты не существует. Попробуйте ещё раз.")
        return
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("👤 Введите ваше ФИО:")

    await EquipmentForm.waiting_for_full_name.set()

@dp.message_handler(state=EquipmentForm.waiting_for_full_name)
async def get_equipment_fio(message: types.Message, state: FSMContext):
    full_name = message.text.strip()
    if not re.match(r'^[А-Яа-яЁёA-Za-z\s\-]+$', full_name):
        await message.answer("⚠️ Пожалуйста, введите только буквы.")
        return
    async with state.proxy() as data:
        data['full_name'] = message.text
    await message.answer("📞 Введите ваш номер телефона \n\nПример: 89252612612")
    await EquipmentForm.waiting_for_phone.set()

@dp.message_handler(state=EquipmentForm.waiting_for_phone)
async def finish_equipment_form(message: types.Message, state: FSMContext):
    phone = message.text.strip().replace(" ", "")
    if not phone.isdigit() or len(phone) < 10:
        await message.answer("⚠️ Пожалуйста, введите корректный номер телефона (только цифры, минимум 10 знаков). Пример: 89255125373")
        return
    async with state.proxy() as data:
        data['phone'] = message.text
    user_id = message.from_user.id
    userikb = InlineKeyboardMarkup(row_width=1)
    userb = InlineKeyboardButton("Профиль", 
                                 url=f'tg://user?id={user_id}')
    userikb.add(userb)
    selected_times2 = user_selected_times2.get(message.from_user.id)

    await bot.send_message(chat_id=chat_log_id, text=f"""
#Оборудование

📦 Оборудование:\n {data['equipment']}
📅 Дата: {data['date']}
🕐 Время: {selected_times2}:00
👤 ФИО: {data['full_name']}
📞 Телефон: {data['phone']}
ID: <code>{message.from_user.id}</code>
""", 
reply_markup=userikb)

    await message.answer("✅ Заявка отправлена! Смета будет в течение суток.", reply_markup=backikb1)
    await state.finish()
    user_selected_times2.pop(user_id, None)

#-=Цепочка menub2=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub2')
async def callback_menub2(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=MENUB1_MESSAGE, 
                                reply_markup=menuikb1p2, 
                                disable_web_page_preview=True)
    user_selected_times.pop(user_id, None)
    user_selected_days.pop(user_id, None)

@dp.callback_query_handler(lambda cb: cb.data == 'menub22')
async def callback_menub22(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.delete_message(chat_id=call.message.chat.id, 
                             message_id=call.message.message_id)
    await bot.send_message(chat_id=call.message.chat.id,
                           text=MENUB111_MESSAGE,
                           disable_web_page_preview=True)
    await bot.send_location(chat_id=call.message.chat.id, 
                            latitude=55.788208, 
                            longitude=37.582715,
                            reply_markup=menuikb1p2p2)
    
@dp.callback_query_handler(lambda cb: cb.data == 'back2')
async def callback_back(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(chat_id=call.message.chat.id, 
                                text=START_MESSAGE, 
                                reply_markup=menuikb)
    

#-=Цепочка menub3=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub3')
async def callback_menub3(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, 
                                text=MENU3_MESSAGE, 
                                reply_markup=menuikb1p3)
    
@dp.callback_query_handler(lambda cb: cb.data == 'menub33')
async def start_pass_request(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🗓 Напишите дату в формате ДД.ММ.ГГ."
    )
    await PassForm.waiting_for_date.set()

@dp.message_handler(state=PassForm.waiting_for_date)
async def get_pass_date(message: types.Message, state: FSMContext):
    date_str = message.text.strip()

    if not re.match(r"^\d{2}\.\d{2}\.\d{2}$", date_str):
        await message.reply("⚠️ Пожалуйста, введите дату в формате ДД.ММ.ГГ (например, 09.04.25).")
        return

    try:
        parsed_date = datetime.strptime(date_str, "%d.%m.%y")
        if parsed_date.date() < datetime.now().date():
            await message.reply("⚠️ Нельзя выбрать прошедшую дату. Введите корректную будущую дату.")
            return

    except ValueError:
        await message.reply("⚠️ Такой даты не существует. Попробуйте ещё раз.")
        return
    async with state.proxy() as data:
        data['pass_date'] = message.text
    await message.answer("🚗 Напишите номер машины по форме: Х123ХХ123")
    await PassForm.waiting_for_car_plate.set()

car_plate_pattern = re.compile(r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')

@dp.message_handler(state=PassForm.waiting_for_car_plate)
async def get_car_plate(message: types.Message, state: FSMContext):
    plate = message.text.upper().replace(" ", "")
    if not car_plate_pattern.match(plate):
        await message.answer("⚠️ Введите корректный госномер РФ.\nПример: А123ВС77")
        return
    async with state.proxy() as data:
        data['car_plate'] = message.text
    await message.answer("👤 Напишите ваше ФИО:\nПример:\nИванов Иван Иванович")
    await PassForm.waiting_for_full_name.set()

@dp.message_handler(state=PassForm.waiting_for_full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    full_name = message.text.strip()
    if not re.match(r'^[А-Яа-яЁёA-Za-z\s\-]+$', full_name):
        await message.answer("⚠️ Пожалуйста, введите только буквы.")
        return
    async with state.proxy() as data:
        data['full_name'] = message.text
    await message.answer("📞 Напишите ваш номер телефона:\n\nПример: 89255125373")
    await PassForm.waiting_for_phone.set()

@dp.message_handler(state=PassForm.waiting_for_phone)
async def finish_pass_request(message: types.Message, state: FSMContext):
    phone = message.text.strip().replace(" ", "")
    if not phone.isdigit() or len(phone) < 10:
        await message.answer("⚠️ Пожалуйста, введите корректный номер телефона (только цифры, минимум 10 знаков). Пример: 89255125373")
        return

    user_id = message.from_user.id
    userikb = InlineKeyboardMarkup(row_width=1)
    userb = InlineKeyboardButton("Профиль", 
                                 url=f'tg://user?id={user_id}')
    userikb.add(userb)
    async with state.proxy() as data:
        data['phone'] = message.text

        await bot.send_message(chat_id=chat_log_id, 
                               text=f"""
#Оформление_пропуска
🆔ID: {user_id}
📅 Дата: {data['pass_date']}
🚗 Авто: {data['car_plate']}
👤 ФИО: {data['full_name']}
📞 Телефон: {data['phone']}
ID: <code>{message.from_user.id}</code>
""",
reply_markup=userikb)

    await message.answer(f"✅ 1. Заявка на пропуск отправлена\n\n🚗 Авто: {data['car_plate']}\n📅 Дата: {data['full_name']}\n👤 ФИО: {data['full_name']}\n📞 Телефон: {data['phone']} \nМенеджер позвонит вам подтвердить заявку", reply_markup=backikb1)
    await state.finish()

#-=Цепочка menub4=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub4')
async def callback_menub4(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                text=MENU4_MESSAGE,
                                message_id=call.message.message_id, 
                                reply_markup=menuikb1p4)

#-=Цепочка menub5=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub5')
async def menub5(call: CallbackQuery):  
    await call.answer(text="В ближайшее время мероприятий не планируется...",
                     show_alert=True,)