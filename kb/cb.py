from boot import bot, dp, types
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from data.txt import START_MESSAGE,MENUB1_MESSAGE, MENUB4_MESSAGE, MENUB41_MESSAGE
from kb.kb import timeikb, menuikb, menuikb1, menuikb4, studioikb1, callback_data_map

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
    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=START_MESSAGE, reply_markup=menuikb)

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
                                text=MENUB41_MESSAGE, 
                                reply_markup=studioikb1)
    

user_selected_date = {}  
user_selected_times = {}  

@dp.callback_query_handler(lambda cb: cb.data.startswith("sb24"))
async def time(call: CallbackQuery):
    user_id = call.from_user.id
    day = call.data.replace("sb24", "")
    user_selected_date[user_id] = day
    user_selected_times[user_id] = []

    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=f"📅 Дата выбрана: {day} \nТеперь выберите время:",
                                reply_markup=time_keyboard(user_id))

def time_keyboard(user_id):
    hours = list(range(9, 22))
    selected = user_selected_times.get(user_id, [])

    ikb = InlineKeyboardMarkup(row_width=3)
    for i in range(0, len(hours), 4):
        row = []
        for hour in hours[i:i+4]:
            text = f"✅ {hour}:00" if hour in selected else f"{hour}:00"
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
        await bot.answer_callback_query(
            call.id, 
            text="Выберите не более двух времён")
        return

    selected.sort()
    user_selected_times[user_id] = selected

    await bot.answer_callback_query(call.id)

    await bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=time_keyboard(user_id))

    if len(selected) == 2:
        start, end = selected
        date = user_selected_date.get(user_id, 'не выбрана')
        total_hours = end - start
        price = total_hours * 3500    
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"""✅ Вы выбрали:\nДата: {date} апреля\nВремя: с {start}:00 до {end}:00\nПримерная цена: {price} руб.\nИтоговая цена может отличатся, <a href='https://pravdaprosvet.ru/rooles'>почитать правила можно тут</a>""",
            reply_markup=timeikb, 
            disable_web_page_preview=True)

        user_selected_times.pop(user_id, None)
        user_selected_date.pop(user_id, None)

@dp.callback_query_handler(lambda cb: cb.data in callback_data_map)
async def callback_stb(call: CallbackQuery):
    text, markup= callback_data_map.get(call.data, (None, None))
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, 
                                message_id=call.message.message_id, 
                                text=text, 
                                reply_markup=markup)
    

