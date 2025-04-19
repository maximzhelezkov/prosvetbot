from boot import bot, dp, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import MessageNotModified 
from db.dbcon import db_add_info, db_get_info
from datetime import date, timedelta, datetime
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from data.txt import START_MESSAGE, MENUB1_MESSAGE, MENUB4_MESSAGE, MENUB41_MESSAGE,EQP_ABOUT_MESSAGE, MENUB111_MESSAGE, ADMIN_PANEL_MESSAGE, MENU4_MESSAGE, MENU44_MESSAGE, MENU3_MESSAGE, ABOUT_STUDIO_MESSAGE
from kb.kb import timeikb,back4, menuikb, menuikb1p1, menuikb1p2 , menuikb5, preferenceikb, abouteqbikb ,studioikb1, about_studioikb, callback_data_map, forwardikb, backikb2, backikb1,menuikb1p2p2 ,menuikb1p4, back3, back5, menuikb1p3,menuikb2p4, adminikb, studioikb21, studioikb22, studioikb23, studioikb24, studioikb25, studioikb26, studioikb27, studioikb28, studioikb29, studioikb210, studioikb211, studioikb212
from boot import storage
from data.config import chat_log_id, admin_id
import re

#-=Хранить данные перед записью в дб=-

user_selected_date = {}
user_selected_times = {}
user_selected_month = {}
user_selected_days = {}
state_data = {}


#-=Классы=-

class Form(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_msg = State()

class PassForm(StatesGroup):
    waiting_for_car_plate = State()
    waiting_for_date = State()
    waiting_for_full_name = State()
    waiting_for_phone = State()

class EquipmentForm(StatesGroup):
    waiting_for_equipment_list = State()
    waiting_for_date = State()
    waiting_for_time = State()
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

async def return_to_main_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(START_MESSAGE, reply_markup=menuikb)

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
            date_str = selected_date
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
    await bot.send_photo(chat_id=call.message.chat.id, photo='https://sun9-48.userapi.com/impg/gQw_caw4wgBZxQn-kEbTGZo2DZgguhm5GGnRng/XKBWT8ji8sI.jpg?size=1080x1080&quality=95&sign=d91350d3026280d397baa3707f3f10ef&type=album')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(chat_id=call.message.chat.id,
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


async def ask_time_for_day(call, user_id, days_list, index):
    if index >= len(days_list):
        await show_summary(call, user_id, days_list)
        return

    current_day = days_list[index]
    state_data[user_id] = {'days': days_list, 'index': index}

    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"Выберите время для {current_day}:",
        reply_markup=time_keyboard(user_id, current_day)
    )

@dp.callback_query_handler(lambda cb: cb.data.startswith("sb2"))
async def select_date_handler(call: CallbackQuery):
    user_id = call.from_user.id
    try:
        studio_code, day, month = call.data.split('_')
        day, month = int(day), int(month)
    except ValueError:
        await bot.answer_callback_query(call.id, text="Ошибка данных", show_alert=True)
        return

    selected = user_selected_date.get(user_id, [])

    if not selected:
        user_selected_date[user_id] = [(day, month)]
        await bot.answer_callback_query(call.id)
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"Дата выбрана: {day}.{month}. Выберите вторую дату \n(или нажмите ту же дату ещё раз, чтобы выбрать только её):",
            reply_markup=get_studio_keyboard(studio_code)
        )
    else:
        first_day, first_month = selected[0]
        user_selected_date[user_id].append((day, month))

        if first_day == day and first_month == month:
            days_range = [f"{day:02d}.{month:02d}"]
        else:
            start_date = date(2025, first_month, first_day)
            end_date = date(2025, month, day)
            if end_date < start_date:
                start_date, end_date = end_date, start_date

            days_range = [(start_date + timedelta(days=i)).strftime('%d.%m') 
                          for i in range((end_date - start_date).days + 1)]

        user_selected_times[user_id] = {}
        await ask_time_for_day(call, user_id, days_range, 0)

def time_keyboard(user_id, current_day):
    selected = user_selected_times.get(user_id, {}).get(current_day, [])
    ikb = InlineKeyboardMarkup(row_width=5)

    for hour in range(0, 25, 5):
        row = []
        for h in range(hour, min(hour+5, 25)):
            text = f"\u2705 {h}:00" if h in selected else f"{h}:00"
            row.append(InlineKeyboardButton(text, callback_data=f"time_{current_day}_{h}"))
        ikb.row(*row)

    ikb.add(InlineKeyboardButton("Готово", callback_data=f"next_{current_day}"))
    return ikb

@dp.callback_query_handler(lambda cb: cb.data.startswith("time_"))
async def time_per_day(call: CallbackQuery):
    user_id = call.from_user.id
    _, day, hour = call.data.split('_')
    hour = int(hour)

    times = user_selected_times.setdefault(user_id, {}).setdefault(day, [])
    if hour in times:
        times.remove(hour)
    elif len(times) < 2:
        times.append(hour)
    else:
        await call.answer("Не больше двух времён")
        return

    await call.answer()
    await bot.edit_message_reply_markup(call.message.chat.id,
                                        call.message.message_id,
                                        reply_markup=time_keyboard(user_id, day))

@dp.callback_query_handler(lambda cb: cb.data.startswith("next_"))
async def next_day_handler(call: CallbackQuery):
    user_id = call.from_user.id
    info = state_data.get(user_id)
    if not info:
        return

    days_list = info['days']
    index = info['index'] + 1
    await ask_time_for_day(call, user_id, days_list, index)

async def show_summary(call, user_id, days):
    msg = "✅ Вы выбрали:\n"
    total_hours = 0

    for d in days:
        hours = user_selected_times.get(user_id, {}).get(d, [])
        if hours:
            start, end = sorted(hours)
            msg += f"{d}: с {start}:00 до {end}:00\n"
            total_hours += end - start
    if total_hours == 12:
        price = 50000
    elif total_hours == 24:
        price = 90000
    elif total_hours >=11:
        price = total_hours * 4500
    else:
        price = total_hours * 4000

    msg += f"\nПримерная цена: {price} руб.\n<a href='https://pravdaprosvet.ru/rooles'>Правила студии</a>"

    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=msg,
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
                                text="Теперь нам нужны контактные данные\nПожалуйста, введите ваше фио:")

    await Form.waiting_for_name.set()

@dp.message_handler(state=Form.waiting_for_name)
async def get_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text == "/start":
        await return_to_main_menu(message, state)
        user_selected_times.pop(user_id, None)
        user_selected_date.pop(user_id, None)
        user_selected_month.pop(user_id, None)
        user_selected_days.pop(user_id, None)
        return
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
Дата: {date_str} \n{time_str}

Контактные данные:
ID: <code>{user_id}</code>
Имя: <code>{name}</code>
Номер: <code>{phone}</code>""",
                            reply_markup=userikb)

@dp.message_handler(state=Form.waiting_for_phone)
async def get_phone(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if message.text == "/start":
        await return_to_main_menu(message, state)
        user_selected_times.pop(user_id, None)
        user_selected_date.pop(user_id, None)
        user_selected_month.pop(user_id, None)
        user_selected_days.pop(user_id, None)
        return

    phone = message.text.strip().replace(" ", "")

    if not (phone.startswith('+') and phone[1:].isdigit() or phone.isdigit()) or len(phone.lstrip('+')) < 10:
        await message.answer("⚠️ Пожалуйста, введите корректный номер телефона. Пример: 89255125373 или +79255125373")
        return

    async with state.proxy() as data:
        data['phone'] = message.text 
        selected_date = user_selected_date.get(message.from_user.id, 'не выбрана')
        date_str = ' — '.join(f"{d}.{m}" for d, m in selected_date)
        time_per_day_data = user_selected_times.get(message.from_user.id, {})

        if time_per_day_data:
            time_str_parts = []
            for date, times in time_per_day_data.items():
                if len(times) == 2:
                    start, end = sorted(times)
                    time_str_parts.append(f"{date} с {start}:00 до {end}:00")
                elif len(times) == 1:
                    time_str_parts.append(f"{date} в {times[0]}:00")
                else:
                    time_str_parts.append(f"{date} — время не выбрано")
            time_str = "\n".join(time_str_parts)
        else:
            time_str = "не выбрано"

    user_id = message.from_user.id
    name = data['name']
    phone = data['phone']

    await message.answer(
        f"Спасибо! Ваши данные сохранены. \nИмя: {name}\nТелефон: {phone}\nДата: \n{date_str}\nВремя: \n{time_str}.\nС вами свяжется менеджер", 
        reply_markup=backikb2)
    db_add_info(name, phone, date_str, time_str, user_id)
    await about_buyer(user_id, name, phone, date_str, time_str)
    await state.finish()
    user_selected_times.pop(user_id, None)
    user_selected_date.pop(user_id, None)
    user_selected_month.pop(user_id, None)
    user_selected_days.pop(user_id, None)

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
    await call.message.answer(text="📦 Впишите список оборудования \n\nПример: \nПрожектор Open Face ARRILITE;3шт, \nЗатенитель сетка SILK scrim;3шт,  \nДиммер бытовой 150W/500W/1000W;1шт:")
    await EquipmentForm.waiting_for_equipment_list.set()

@dp.message_handler(state=EquipmentForm.waiting_for_equipment_list)
async def get_equipment_list(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text == "/start":
        await return_to_main_menu(message, state)
        return
    async with state.proxy() as data:
        data['equipment'] = message.text
    await message.answer("📅 Укажите дату брони (в формате ДД.ММ.ГГ):")
    await EquipmentForm.waiting_for_date.set()

@dp.message_handler(state=EquipmentForm.waiting_for_date)
async def get_equipment_date(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text == "/start":
        await return_to_main_menu(message, state)
        return
    date_str = message.text.strip()
    if not re.match(r"^\d{2}\.\d{2}\.\d{2}$", date_str):
        await message.reply("⚠️ Пожалуйста, введите дату в формате ДД.ММ.ГГ (например, 09.09.25).")
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
    await message.answer("⏰ Выберите время брони:", reply_markup=time_keyboard2())
    await EquipmentForm.waiting_for_time.set()


@dp.callback_query_handler(lambda c: c.data.startswith("time2_"), state=EquipmentForm.waiting_for_time)
async def select_time(callback_query: types.CallbackQuery, state: FSMContext):
    hour = callback_query.data.split("_")[1]
    time_s = f"{hour}:00"
    
    async with state.proxy() as data:
        data['time'] = time_s

    await callback_query.message.edit_reply_markup() 
    await callback_query.message.answer(f"Вы выбрали время: {time_s}")
    await callback_query.message.answer("👤 Введите ваше ФИО:")

    await EquipmentForm.waiting_for_full_name.set()

@dp.message_handler(state=EquipmentForm.waiting_for_full_name)
async def get_equipment_fio(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text == "/start":
        await return_to_main_menu(message, state)
        return
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
    user_id = message.from_user.id

    if message.text == "/start":
        await return_to_main_menu(message, state)
        return

    phone = message.text.strip().replace(" ", "")

    if not (phone.startswith('+') and phone[1:].isdigit() or phone.isdigit()) or len(phone.lstrip('+')) < 10:
        await message.answer("⚠️ Пожалуйста, введите корректный номер телефона. Пример: 89255125373 или +79255125373")
        return

    async with state.proxy() as data:
        data['phone'] = phone
    user_id = message.from_user.id
    userikb = InlineKeyboardMarkup(row_width=1)
    userb = InlineKeyboardButton("Профиль", 
                                 url=f'tg://user?id={user_id}')
    userikb.add(userb)
    await bot.send_message(chat_id=chat_log_id, text=f"""
#Оборудование

📦 Оборудование:\n {data['equipment']}
📅 Дата: {data['date']}
🕐 Время: {data['time']}:00
👤 ФИО: {data['full_name']}
📞 Телефон: {data['phone']}
ID: <code>{message.from_user.id}</code>
""", 
reply_markup=userikb)

    await message.answer("✅ Заявка отправлена! Смета будет в течение суток.", reply_markup=backikb1)
    await state.finish()    

#-=Цепочка menub2=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub7')
async def callback_menub2(call: CallbackQuery):     
    await bot.edit_message_text(message_id=call.message.message_id,
                                chat_id=call.message.chat.id,
                                text=MENUB1_MESSAGE,
                                reply_markup=menuikb1p2,
                                disable_web_page_preview=True,
                                parse_mode="HTML")

@dp.callback_query_handler(lambda cb: cb.data == 'menub22')
async def callback_menub22(call: CallbackQuery):     
    await bot.answer_callback_query(call.id)
    await bot.delete_message(chat_id=call.message.chat.id, 
                             message_id=call.message.message_id)
    await bot.send_message(chat_id=call.message.chat.id,text=MENUB111_MESSAGE, disable_web_page_preview=True)
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
                                
car_plate_pattern = re.compile(r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')

@dp.callback_query_handler(lambda cb: cb.data == 'menub33')
async def start_pass_request(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="""
<b>Оформите пропуск для въезда в комплекс “Правда”</b>

🚗Напишите номер машины по форме:

Х123ХХ123

Парковка на территории комплекса “Правда” - бесплатная!

Просим вас оформлять пропуск минимум за 6 часов до времени прибытия!"""
    )
    await PassForm.waiting_for_car_plate.set()
    

@dp.message_handler(state=PassForm.waiting_for_car_plate)
async def get_pass_date(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await return_to_main_menu(message, state)
        return
    plate = message.text.upper().replace(" ", "")
    if not car_plate_pattern.match(plate):
        await message.answer("⚠️ Введите корректный госномер РФ.\nПример: А123ВС77")
        return
    async with state.proxy() as data:
        data['car_plate'] = message.text
    await message.answer("🗓 Напишите дату в формате ДД.ММ.ГГ.")
    await PassForm.waiting_for_car_plate.set()


@dp.message_handler(state=PassForm.waiting_for_date)
async def get_car_plate(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await return_to_main_menu(message, state)
        return
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
    await message.answer("👤 Напишите ваше ФИО:\nПример:\nИванов Иван Иванович")
    await PassForm.waiting_for_full_name.set()

@dp.message_handler(state=PassForm.waiting_for_full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await return_to_main_menu(message, state)
        return
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
    user_id = message.from_user.id

    if message.text == "/start":
        await return_to_main_menu(message, state)
        return

    phone = message.text.strip().replace(" ", "")

    if not (phone.startswith('+') and phone[1:].isdigit() or phone.isdigit()) or len(phone.lstrip('+')) < 10:
        await message.answer("⚠️ Пожалуйста, введите корректный номер телефона. Пример: 89255125373 или +79255125373")
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

    await message.answer(f"✅ 1. Заявка на пропуск отправлена\n\n🚗 Авто: {data['car_plate']}\n📅 Дата: {data['pass_date']}\n👤 ФИО: {data['full_name']}\n📞 Телефон: {data['phone']} \nс вами свяжется менеджер", reply_markup=backikb1)
    await state.finish()

#-=Цепочка menub4=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub6')
async def callback_menub4(call: CallbackQuery):
    await bot.edit_message_text(message_id=call.message.message_id,chat_id=call.message.chat.id, text=MENU4_MESSAGE, reply_markup=menuikb1p4)

#-=Цепочка menub5=-

@dp.callback_query_handler(lambda cb: cb.data == 'menub5')
async def menub5(call: CallbackQuery):  
    await bot.edit_message_text(message_id=call.message.message_id, 
                                chat_id=call.message.chat.id, 
                                text="""<b>В ближайшее время мероприятий не планируется</b> \n\nСледите за анонсами в нашем <a href='t.me/prosvetcorp'>телеграм канале ProSvet</a>""",
                                reply_markup=menuikb5)