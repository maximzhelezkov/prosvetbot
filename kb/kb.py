from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

startikb = InlineKeyboardMarkup(row_width=1)
startb1= InlineKeyboardButton("Перейти в меню", callback_data='menu')
startikb.add(startb1)

menuikb = InlineKeyboardMarkup(row_width=3)
menub1 = InlineKeyboardButton("О нас", callback_data='menub1')
menub5 = InlineKeyboardButton("Адрес", callback_data='menub5')
menub2 = InlineKeyboardButton("Наш сайт", url='https://pravdaprosvet.ru')
menub3 = InlineKeyboardButton("Наш телеграм канал", url='prosvetcorp.t.me')
menub4 = InlineKeyboardButton("Быстрая бронь", callback_data='menub4')
menuikb.add(menub1, menub5).add(menub2, menub3).add(menub4)

back1 = InlineKeyboardButton("Назад ◀️", callback_data='back1')

menuikb1 = InlineKeyboardMarkup(row_width=1)
menuikb1.add(back1)

menub5ikb = InlineKeyboardMarkup(row_width=2)
menub5b = InlineKeyboardButton("Геолокация", callback_data='menub51')
menub5ikb.add(menub5b).add(back1)