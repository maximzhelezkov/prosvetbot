from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup    
import datetime
from data.txt import MENUB41_MESSAGE

#-=Какой сегодня день и месяц=-

today = datetime.datetime.today()
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
menub4 = InlineKeyboardButton("О студии", callback_data='menub4')
menub2 = InlineKeyboardButton("Контакты", callback_data='menub2')
menuikb.add(menub1).add(menub3).add(menub5).add(menub4, menub2)


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

current_month = datetime.datetime.now().month

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

#-Календарь-

studioikb21 = InlineKeyboardMarkup(row_width=7)
current_month = "01"
sb211 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 5)]
sb212 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(5, 12)]
sb213 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(12, 19)]
sb214 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(19, 26)]
sb215 = [InlineKeyboardButton(str(i), callback_data=f"sb21_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(26, 32)]
studioikb21.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,*sb211).add(*sb212).add(*sb213).add(*sb214).add(*sb215, sb2_0)

studioikb22 = InlineKeyboardMarkup(row_width=7)
current_month = "02"
sb221 = InlineKeyboardButton(text='1', callback_data=f"sb22_1_{current_month}"if 1 >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{1}",callback_data="null"))
sb222 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(2, 9)]
sb223 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(9, 16)]
sb224 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(16, 23)]
sb225 = [InlineKeyboardButton(str(i), callback_data=f"sb22_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(23, 29)]
studioikb22.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb221).add(*sb222).add(*sb223).add(*sb224).add(*sb225, sb2_0)

studioikb23 = InlineKeyboardMarkup(row_width=7)
current_month = "03"
sb231 = InlineKeyboardButton(text='1', callback_data=f"sb23_1_{current_month}"if 1 >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{1}",callback_data="null"))
sb232 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(2, 9)]
sb233 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(9, 16)]
sb234 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(16, 23)]
sb235 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(23, 30)]
sb236 = [InlineKeyboardButton(str(i), callback_data=f"sb23_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(30, 32)]
studioikb23.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb231).add(*sb232).add(*sb233).add(*sb234).add(*sb235).add(*sb236, sb2_0, sb2_0, sb2_0, sb2_0, sb2_0)

studioikb24 = InlineKeyboardMarkup(row_width=7)
current_month = "04"
sb241 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 7)]
sb242 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(7, 14)]
sb243 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(14, 21)]
sb244 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(21, 28)]
sb245 = [InlineKeyboardButton(str(i), callback_data=f"sb24_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(28, 31)]
studioikb24.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(sb2_0, *sb241).add(*sb242).add(*sb243).add(*sb244).add(*sb245, sb2_0, sb2_0, sb2_0, sb2_0)

studioikb25 = InlineKeyboardMarkup(row_width=7)
current_month = "05"
sb251 = [InlineKeyboardButton(str(i), callback_data=f"sb25_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 5)]
sb252 = [InlineKeyboardButton(str(i), callback_data=f"sb25_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(5, 12)]
sb253 = [InlineKeyboardButton(str(i), callback_data=f"sb25_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(12, 19)]
sb254 = [InlineKeyboardButton(str(i), callback_data=f"sb25_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(19, 26)]
sb255 = [InlineKeyboardButton(str(i), callback_data=f"sb25_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(26, 32)]
studioikb25.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0, *sb251).add(*sb252).add(*sb253).add(*sb254).add(*sb255,sb2_0)

studioikb26 = InlineKeyboardMarkup(row_width=7)
current_month = "06"
sb261 = InlineKeyboardButton(text='1', callback_data=f"sb26_1_{current_month}"if 1 >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{1}",callback_data="null"))
sb262 = [InlineKeyboardButton(str(i), callback_data=f"sb26_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(2, 9)]
sb263 = [InlineKeyboardButton(str(i), callback_data=f"sb26_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(9, 16)]
sb264 = [InlineKeyboardButton(str(i), callback_data=f"sb26_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(16, 23)]
sb265 = [InlineKeyboardButton(str(i), callback_data=f"sb26_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(23, 30)]
sb266 = InlineKeyboardButton(text='30', callback_data=f"sb26_30_{current_month}"if 30 >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{30}",callback_data="null"))
studioikb26.add(sb24m, sb24tu, sb24w,sb24te,sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb2_0,sb261).add(*sb262).add(*sb263).add(*sb264).add(*sb265).add(sb266, sb2_0, sb2_0, sb2_0, sb2_0, sb2_0, sb2_0)

studioikb27 = InlineKeyboardMarkup(row_width=7)
current_month = "07"
sb271 = [InlineKeyboardButton(str(i), callback_data=f"sb27_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 7)]
sb272 = [InlineKeyboardButton(str(i), callback_data=f"sb27_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(7, 14)]
sb273 = [InlineKeyboardButton(str(i), callback_data=f"sb27_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(14, 21)]
sb274 = [InlineKeyboardButton(str(i), callback_data=f"sb27_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(21, 28)]
sb275 = [InlineKeyboardButton(str(i), callback_data=f"sb27_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(28, 32)]
studioikb27.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(sb2_0,*sb271).add(*sb272).add(*sb273).add(*sb274).add(*sb275,sb2_0,sb2_0,sb2_0)

studioikb28 = InlineKeyboardMarkup(row_width=7)
current_month = "08"
sb281 = [InlineKeyboardButton(str(i), callback_data=f"sb28_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 4)]
sb282 = [InlineKeyboardButton(str(i), callback_data=f"sb28_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(4, 11)]
sb283 = [InlineKeyboardButton(str(i), callback_data=f"sb28_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(11, 18)]
sb284 = [InlineKeyboardButton(str(i), callback_data=f"sb28_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(18, 25)]
sb285 = [InlineKeyboardButton(str(i), callback_data=f"sb28_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(25, 32)]
studioikb28.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(sb2_0,sb2_0,sb2_0,sb2_0, *sb281).add(*sb282).add(*sb283).add(*sb284).add(*sb285)

studioikb29 = InlineKeyboardMarkup(row_width=7)
current_month = "09"
sb291 = [InlineKeyboardButton(str(i), callback_data=f"sb29_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 8)]
sb292 = [InlineKeyboardButton(str(i), callback_data=f"sb29_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(8, 15)]
sb293 = [InlineKeyboardButton(str(i), callback_data=f"sb29_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(15, 22)]
sb294 = [InlineKeyboardButton(str(i), callback_data=f"sb29_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(22, 29)]
sb295 = [InlineKeyboardButton(str(i), callback_data=f"sb29_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(29, 31)]
studioikb29.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(*sb291).add(*sb292).add(*sb293).add(*sb294).add(*sb295, sb2_0, sb2_0, sb2_0, sb2_0, sb2_0)

studioikb210 = InlineKeyboardMarkup(row_width=7)
current_month = "10"
sb2101 = [InlineKeyboardButton(str(i), callback_data=f"sb210_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 6)]
sb2102 = [InlineKeyboardButton(str(i), callback_data=f"sb210_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(6, 13)]
sb2103 = [InlineKeyboardButton(str(i), callback_data=f"sb210_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(13, 20)]
sb2104 = [InlineKeyboardButton(str(i), callback_data=f"sb210_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(20, 27)]
sb2105 = [InlineKeyboardButton(str(i), callback_data=f"sb210_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(27, 32)]
studioikb210.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(sb2_0, sb2_0, *sb2101).add(*sb2102).add(*sb2103).add(*sb2104).add(*sb2105, sb2_0, sb2_0)

studioikb211 = InlineKeyboardMarkup(row_width=7)
current_month = "11"
sb2111 = [InlineKeyboardButton(str(i), callback_data=f"sb211_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 3)]
sb2112 = [InlineKeyboardButton(str(i), callback_data=f"sb211_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(3, 10)]
sb2113 = [InlineKeyboardButton(str(i), callback_data=f"sb211_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(10, 17)]
sb2114 = [InlineKeyboardButton(str(i), callback_data=f"sb211_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(17, 24)]
sb2115 = [InlineKeyboardButton(str(i), callback_data=f"sb211_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(24, 31)]
studioikb211.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(sb2_0, sb2_0, sb2_0, sb2_0, sb2_0, *sb2111).add(*sb2112).add(*sb2113).add(*sb2114).add(*sb2115)

studioikb212 = InlineKeyboardMarkup(row_width=7)
current_month = "12"
sb2121 = [InlineKeyboardButton(str(i), callback_data=f"sb212_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(1, 8)]
sb2122 = [InlineKeyboardButton(str(i), callback_data=f"sb212_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(8, 15)]
sb2123 = [InlineKeyboardButton(str(i), callback_data=f"sb212_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(15, 22)]
sb2124 = [InlineKeyboardButton(str(i), callback_data=f"sb212_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(22, 29)]
sb2125 = [InlineKeyboardButton(str(i), callback_data=f"sb212_{i}_{current_month}")if i >= day or int(current_month) != month_num 
                                                                                else InlineKeyboardButton(f"❌{i}",callback_data="null") for i in range(29, 32)]
studioikb212.add(sb24m, sb24tu, sb24w, sb24te, sb24f, sb24sa, sb24su).add(*sb2121).add(*sb2122).add(*sb2123).add(*sb2124).add(*sb2125, sb2_0, sb2_0, sb2_0, sb2_0)


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
menuikb1p5 = InlineKeyboardMarkup(row_width=1)


#-=Кнопки Админ Панели=-

adminikb = InlineKeyboardMarkup(row_width=2)
adminb1 = InlineKeyboardButton("Бронь", callback_data='adminb1')
adminb2 = InlineKeyboardButton("Оборудование", callback_data='adminb2')
adminb3 = InlineKeyboardButton("Рассылка", callback_data='adminb3')
adminikb.add(adminb1).add(adminb2).add(adminb3)
