from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from data.txt import MENUB41_MESSAGE

startikb = InlineKeyboardMarkup(row_width=1)
startb = InlineKeyboardButton("Начать!", callback_data='smenu')
startikb.add(startb)

menuikb = InlineKeyboardMarkup(row_width=3)
menub1 = InlineKeyboardButton("Адрес", callback_data='menub1')
menub2 = InlineKeyboardButton("О нас", url='https://yandex.com/maps/org/prosvet_studio/113587603396/reviews/?ll=37.718387%2C55.782858&z=15.4')
menub3 = InlineKeyboardButton("Наш тг канал", url='prosvetcorp.t.me')
menub4 = InlineKeyboardButton("Быстрая бронь", callback_data='menub4')
menuikb.add(menub2, menub3).add(menub1).add(menub4)

back1 = InlineKeyboardButton("Назад ⬅️", callback_data='back1')
back2 = InlineKeyboardButton("Назад ⬅️", callback_data='back2')
back3 = InlineKeyboardButton("Назад ⬅️", callback_data='studio')
back4 = InlineKeyboardButton("Назад ⬅️", callback_data='menub4')
back5 = InlineKeyboardMarkup("Назад ⬅️", callback_data='adminikb')
menuikb1 = InlineKeyboardMarkup(row_width=1)
menuikb1.add(back1)


menuikb1 = InlineKeyboardMarkup(row_width=2)
menub1b = InlineKeyboardButton("Геолокация", callback_data='menub11')
menub1b2 = InlineKeyboardButton("Отзывы", url='https://yandex.com/maps/org/prosvet_studio/113587603396/reviews/?ll=37.718387%2C55.782858&z=15.4')
menub1b3 = InlineKeyboardButton("Портфолио", url='https://pravdaprosvet.ru/portfolio')
menuikb1.add(menub1b2, menub1b3).add(menub1b).add(back1)

menuikb2 = InlineKeyboardMarkup(row_width=2)
menuikb2.add(menub1b2, menub1b3).add(back2)

menuikb4 = InlineKeyboardMarkup(row_width=3)
menu4b1 = InlineKeyboardButton("Студия", callback_data='studio')
menu4b2 = InlineKeyboardButton("Оборудование", callback_data='equipment')
menuikb4.add(menu4b1).add(menu4b2).add(back1)


adminikb = InlineKeyboardMarkup(row_width=2)
adminb1 = InlineKeyboardButton("Бронь", callback_data='adminb1')
adminb2 = InlineKeyboardButton("Оборудование", callback_data='adminb2')
adminb3 = InlineKeyboardButton("Рассылка", callback_data='adminb3')
adminikb.add(adminb1).add(adminb2).add(adminb3)

current_month = datetime.datetime.now().month



months = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]

buttons = []
for i in range(12):
    month_index = (current_month + i - 1) % 12
    button1 = InlineKeyboardButton(months[month_index], callback_data=f'stb{month_index+1}')
    buttons.append(button1)

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

studioikb1 = InlineKeyboardMarkup(row_width=4)  
studioikb1.add(*buttons).add(back4)

studioikb21 = InlineKeyboardMarkup(row_width=7)
current_month = "01"
sb211 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}") for i in range(1, 5)]
sb212 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}") for i in range(5, 12)]
sb213 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}") for i in range(12, 19)]
sb214 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}") for i in range(19, 26)]
sb215 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}") for i in range(26, 32)]
studioikb21.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,*sb211).add(*sb212).add(*sb213).add(*sb214).add(*sb215, sb2_0)

studioikb22 = InlineKeyboardMarkup(row_width=7)
current_month = "02"
sb221 = InlineKeyboardButton(text='1', callback_data=f"sb22_1_{current_month}")
sb222 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}") for i in range(2, 9)]
sb223 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}") for i in range(9, 16)]
sb224 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}") for i in range(16, 23)]
sb225 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}") for i in range(23, 29)]
studioikb22.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb221).add(*sb222).add(*sb223).add(*sb224).add(*sb225, sb2_0)

studioikb23 = InlineKeyboardMarkup(row_width=7)
current_month = "03"
sb231 = InlineKeyboardButton(text='1', callback_data=f"sb23_1_{current_month}")
sb232 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}") for i in range(2, 9)]
sb233 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}") for i in range(9, 16)]
sb234 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}") for i in range(16, 23)]
sb235 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}") for i in range(23, 30)]
sb236 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}") for i in range(30, 32)]
studioikb23.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb231).add(*sb232).add(*sb233).add(*sb234).add(*sb235).add(*sb236, sb2_0, sb2_0, sb2_0, sb2_0, sb2_0)

studioikb24 = InlineKeyboardMarkup(row_width=7)
current_month = "04"
sb241 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}") for i in range(1, 7)]
sb242 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}") for i in range(7, 14)]
sb243 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}") for i in range(14, 21)]
sb244 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}") for i in range(21, 28)]
sb245 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}") for i in range(28, 31)]
studioikb24.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(sb2_0, *sb241).add(*sb242).add(*sb243).add(*sb244).add(*sb245, sb2_0, sb2_0, sb2_0, sb2_0)


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