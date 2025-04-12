from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from data.txt import MENUB41_MESSAGE

menuikb = InlineKeyboardMarkup(row_width=3)
menub1 = InlineKeyboardButton("О нас \ Адрес", callback_data='menub1')
menub2 = InlineKeyboardButton("Наш сайт", url='https://pravdaprosvet.ru')
menub3 = InlineKeyboardButton("Наш телеграм канал", url='prosvetcorp.t.me')
menub4 = InlineKeyboardButton("Быстрая бронь", callback_data='menub4')
menuikb.add(menub2, menub3).add(menub1).add(menub4)

back1 = InlineKeyboardButton("Назад ⬅️", callback_data='back1')

menuikb1 = InlineKeyboardMarkup(row_width=1)
menuikb1.add(back1)

menuikb1 = InlineKeyboardMarkup(row_width=2)
menub1b = InlineKeyboardButton("Геолокация", callback_data='menub11')
menub1b2 = InlineKeyboardButton("Отзывы", url='https://yandex.com/maps/org/prosvet_studio/113587603396/reviews/?ll=37.718387%2C55.782858&z=15.4')
menub1b3 = InlineKeyboardButton("Портфолио", url='https://pravdaprosvet.ru/portfolio')
menuikb1.add(menub1b2, menub1b3).add(menub1b).add(back1)

menuikb4 = InlineKeyboardMarkup(row_width=3)
menu4b1 = InlineKeyboardButton("Студия", callback_data='studio')
menu4b2 = InlineKeyboardButton("Оборудование", callback_data='equipment')
menuikb4.add(menu4b1).add(menu4b2).add(back1)


current_month = datetime.datetime.now().month

months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]

buttons = []
for i in range(6):
    month_index = (current_month + i - 1) % 12
    button1 = InlineKeyboardButton(months[month_index], callback_data=f'stb{month_index+1}')
    buttons.append(button1)

hallikb = InlineKeyboardMarkup(row_width=2)
hallb1 = InlineKeyboardButton("Зал Лондон", callback_data="hall_london")
hallb2 = InlineKeyboardButton("Зал Париж", callback_data="hall_paris")
hallikb.add(hallb1, hallb2)

studioikb1 = InlineKeyboardMarkup(row_width=3)  
studioikb1.add(*buttons)

studioikb21 = InlineKeyboardMarkup(row_width=5)

studioikb22 = InlineKeyboardMarkup(row_width=5)

studioikb23 = InlineKeyboardMarkup(row_width=5)

studioikb24 = InlineKeyboardMarkup(row_width=7)
sb24m = InlineKeyboardButton('ПН', callback_data='null')
sb24tu = InlineKeyboardButton('ВТ', callback_data='null')
sb24w = InlineKeyboardButton('СР', callback_data='null')
sb24te = InlineKeyboardButton('ЧТ', callback_data='null')
sb24f = InlineKeyboardButton('ПТ', callback_data='null')
sb24sa = InlineKeyboardButton('СБ', callback_data='null')
sb24su = InlineKeyboardButton('ВС', callback_data='null')
sb2_0 = InlineKeyboardButton('-', callback_data='null')

forwardikb = InlineKeyboardMarkup(row_width=2)
forwardb = InlineKeyboardButton("", callback_data='')


sb241 = []
for i in range(1, 7):
    button2 = InlineKeyboardButton(str(i), callback_data=f"sb24{i}")
    sb241.append(button2)

sb242 = []
for i in range(7, 14):
    button3 = InlineKeyboardButton(str(i), callback_data=f"sb24{i}")
    sb242.append(button3)

sb243 = []
for i in range(14, 21):
    button4 = InlineKeyboardButton(str(i), callback_data=f"sb24{i}")
    sb243.append(button4)

sb244 = []
for i in range(21, 28):
    button5 = InlineKeyboardButton(str(i), callback_data=f"sb24{i}")
    sb244.append(button5)

sb245 = []
for i in range(28, 31):
    button6 = InlineKeyboardButton(str(i), callback_data=f"sb24{i}")
    sb245.append(button6)

studioikb24.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,*sb241).add(*sb242).add(*sb243).add(*sb244).add(*sb245, sb2_0, sb2_0, sb2_0, sb2_0)



studioikb25 = InlineKeyboardMarkup(row_width=5)

studioikb26 = InlineKeyboardMarkup(row_width=5)

studioikb27 = InlineKeyboardMarkup(row_width=5)

studioikb28 = InlineKeyboardMarkup(row_width=5)

studioikb29 = InlineKeyboardMarkup(row_width=5)

studioikb210 = InlineKeyboardMarkup(row_width=5)

studioikb211 = InlineKeyboardMarkup(row_width=5)

studioikb212 = InlineKeyboardMarkup(row_width=5)


timeikb = InlineKeyboardMarkup(row_width=2)
timeb1 = InlineKeyboardButton("Продолжить➡️", callback_data='forward')
timeb2 = InlineKeyboardButton("Изменить⬅️", callback_data='studio')
timeikb.add(timeb1).add(timeb2)

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