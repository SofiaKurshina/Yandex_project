from telebot import types

markup_menu1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Начать квест😏")
btn3 = types.KeyboardButton("Помощь🙏")
markup_menu1.add(btn1, btn3)

markup_menu2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Идем далее🚶‍♀️")
markup_menu2.add(btn1)

markup_quest = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Войти в комнату 'Алиса в стране чудес'🧚‍♂️")
btn2 = types.KeyboardButton("Войти в комнату с пауком🕷")
markup_quest.add(btn1, btn2)

markup_quest0 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton("Искать ключ для выхода рядом с роляю🎹")
btn2 = types.KeyboardButton("Искать ключ для выхода рядом со шкафом и качелями")
markup_quest0.add(btn1, btn2)

markup_quest1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn3 = types.KeyboardButton("Залезть под качели и поискать там ключик🗝")
btn4 = types.KeyboardButton("Искать ключик в шкафу🗝")
markup_quest1.add(btn3, btn4)

markup_quest6 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn9 = types.KeyboardButton("Слишком стало страшно. Хочу в другую комнату😖")
btn10 = types.KeyboardButton("Пойти в аквариум к пауку🕷")
markup_quest6.add(btn9, btn10)

markup_quest7 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn9 = types.KeyboardButton("Испугаться и не идти😭")
btn10 = types.KeyboardButton("Пойти к пауку и взять из под него ключ😨")
markup_quest7.add(btn9, btn10)