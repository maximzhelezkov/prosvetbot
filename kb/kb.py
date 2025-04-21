from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup    
from datetime import date, timedelta, datetime
from data.txt import MENUB41_MESSAGE



#-=Какой сегодня день и месяц=-

today = datetime.today()
day = today.day + 1
month_num = today.month


#-=Кнопки сообщения для новых пользователей=-

startikb = InlineKeyboardMarkup(row_width=1)
startb = InlineKeyboardButton("Начать!", callback_data='smenu')
startikb.add(startb)


#-=Кнопки назад=-

back1 = InlineKeyboardButton("Назад ⬅️", callback_data='back1')
back2 = InlineKeyboardButton("Назад ⬅️", callback_data='back2')
back3 = InlineKeyboardButton("Назад ⬅️", callback_data='studio11')
back4 = InlineKeyboardButton("Назад ⬅️", callback_data='menub1')
back5 = InlineKeyboardButton("Назад ⬅️", callback_data='adminikb')
back6 = InlineKeyboardButton("Назад ⬅️", callback_data='menub3')
back7 = InlineKeyboardButton("Назад ⬅️", callback_data='menub4')

backikb1 = InlineKeyboardMarkup(row_width=1)
backikb1.add(back1)

backikb2 = InlineKeyboardMarkup(row_width=1)
backikb2.add(back1)

#-=Кнопки в меню=-

menuikb = InlineKeyboardMarkup(row_width=2)
menub1 = InlineKeyboardButton("Бронирование", callback_data='menub1')
menub3 = InlineKeyboardButton("Оформить пропуск", callback_data='menub33')
menub5 = InlineKeyboardButton("Мероприятия", callback_data='menub5')
menub7 = InlineKeyboardButton("Контакты", callback_data='menub7')
menub6 = InlineKeyboardButton("О студии", callback_data='menub6')
menuikb.add(menub1).add(menub3).add(menub5).add(menub6, menub7)


#-=Цепочка menub1=-

menuikb1p1 = InlineKeyboardMarkup(row_width=3)
menu1b1 = InlineKeyboardButton("Студия", callback_data='about_studio')
menu1b2 = InlineKeyboardButton("Оборудование", callback_data='equipment')
menuikb1p1.add(menu1b1).add(menu1b2).add(back1)

abouteqbikb = InlineKeyboardMarkup(row_width=1)
about_eqbb = InlineKeyboardButton("Забронировать", callback_data='eqb')
abouteqbikb.add(about_eqbb).add(back4)

about_studioikb = InlineKeyboardMarkup(row_width=1)
about_studiob1 = InlineKeyboardButton("Продолжить", callback_data='studio')
about_studioikb.add(about_studiob1).add(back4)

current_month = datetime.now().month

months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]

monthbuttons = []
for i in range(12):
    month_index = (current_month + i - 1) % 12
    button1 = InlineKeyboardButton(months[month_index], callback_data=f'stb{month_index+1}')
    monthbuttons.append(button1)

studioikb1 = InlineKeyboardMarkup(row_width=4)  
studioikb1.add(*monthbuttons).add(back4)

#- Дни недели-
def generate_calendar_keyboard(month):
    today = datetime.today()
    current_year = today.year
    current_month = today.month

    if month < current_month:
        year = current_year + 1
    else:
        year = current_year

    ikb = InlineKeyboardMarkup(row_width=7)

    days_in_month = (datetime(year, month, 1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    days_count = days_in_month.day

    first_day_of_month = datetime(year, month, 1)
    first_weekday = first_day_of_month.weekday()

    rows = []

    weekdays = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
    weekday_buttons = [InlineKeyboardButton(day, callback_data='null') for day in weekdays]
    rows.append(weekday_buttons)

    row = [InlineKeyboardButton('-', callback_data='null')] * first_weekday
    for day in range(1, days_count + 1):
        current_date = datetime(year, month, day)

        if current_date < today:
            text = f"❌ {day}"
            callback_data = "null"
        else:
            text = str(day)
            callback_data = f"sb{day:02d}_{month}"

        row.append(InlineKeyboardButton(text, callback_data=callback_data))

        if len(row) == 7:
            rows.append(row)
            row = []

    if row:
        while len(row) < 7:
            row.append(InlineKeyboardButton('-', callback_data='null'))
        rows.append(row)

    for row in rows:
        ikb.row(*row)

    return ikb



studioikb21 = generate_calendar_keyboard(month=1)
studioikb22 = generate_calendar_keyboard(month=2)
studioikb23 = generate_calendar_keyboard(month=3)
studioikb24 = generate_calendar_keyboard(month=4)
studioikb25 = generate_calendar_keyboard(month=5)
studioikb26 = generate_calendar_keyboard(month=6)
studioikb27 = generate_calendar_keyboard(month=7)
studioikb28 = generate_calendar_keyboard(month=8)
studioikb29 = generate_calendar_keyboard(month=9)
studioikb210 = generate_calendar_keyboard(month=10)
studioikb211 = generate_calendar_keyboard(month=11)
studioikb212 = generate_calendar_keyboard(month=12)



timeikb = InlineKeyboardMarkup(row_width=2)
timeb1 = InlineKeyboardButton("Продолжить➡️", callback_data='forward')
timeikb.add(timeb1).add(back3)

callback_data_map = {
    'stb1': (MENUB41_MESSAGE, studioikb21),
    'stb2': (MENUB41_MESSAGE, studioikb22),
    'stb3': (MENUB41_MESSAGE, studioikb23),
    'stb4': (MENUB41_MESSAGE, studioikb24),
    'stb5': (MENUB41_MESSAGE, studioikb25),
    'stb6': (MENUB41_MESSAGE, studioikb26),
    'stb7': (MENUB41_MESSAGE, studioikb27),
    'stb8': (MENUB41_MESSAGE, studioikb28),
    'stb9': (MENUB41_MESSAGE, studioikb29),
    'stb10': (MENUB41_MESSAGE, studioikb210),
    'stb11': (MENUB41_MESSAGE, studioikb211),
    'stb12': (MENUB41_MESSAGE, studioikb212)
} 

preferenceikb = InlineKeyboardMarkup(row_width=1)
preferenceb1 = InlineKeyboardButton("Напишите мне в Телеграме", callback_data='msggg')
preferenceb2 = InlineKeyboardButton("Позвоните мне", callback_data='call')
preferenceikb.add(preferenceb1, preferenceb2)    

#-=Цепочка menub2=-

menuikb1p2 = InlineKeyboardMarkup(row_width=1)
menub2b1 = InlineKeyboardButton("Построить маршрут", callback_data='menub22')
menuikb1p2.add(menub2b1).add(back1)

menuikb1p2p2 = InlineKeyboardMarkup(row_width=1)
menuikb1p2p2.add(back2)


#-=Цепочка menub3=-
menuikb1p3 = InlineKeyboardMarkup(row_width=1)
menub3b1 = InlineKeyboardButton("Оформить пропуск", callback_data='menub33') 
menuikb1p3.add(menub3b1)


#-=Цепочка menub4=-

menuikb1p4 = InlineKeyboardMarkup(row_width=2)
menub4b2 = InlineKeyboardButton("Отзывы", url='https://yandex.ru/maps/org/prosvet_studio/206116246597?si=2eprq3xvvy3v3hunt843ty6ygc')
menub4b3 = InlineKeyboardButton("Фото студии", url='https://pravdaprosvet.ru/portfolio')
menuikb1p4.add(menub4b2).add(menub4b3).add(back1)

menuikb2p4 = InlineKeyboardMarkup(row_width=1)
menuikb2p4.add(back7)

#-=Цепочка menub5=-
menuikb5 = InlineKeyboardMarkup(row_width=1)
menuikb5.add(back1)
#-=Кнопки Админ Панели=-

adminikb = InlineKeyboardMarkup(row_width=2)
adminb1 = InlineKeyboardButton("Бронь", callback_data='adminb1')
adminb2 = InlineKeyboardButton("Добавить в Базу Данных", callback_data='adminb2')
adminb3 = InlineKeyboardButton("Рассылка", callback_data='adminb3')
adminikb.add(adminb1).add(adminb2).add(adminb3)
