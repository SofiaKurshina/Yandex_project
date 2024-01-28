import telebot
from media import Image
import json
from buttons import (markup_quest, markup_quest1, markup_quest0, markup_menu1, markup_menu2, markup_quest7, markup_quest6)

bot = telebot.TeleBot("6814474932:AAEp5xGQY9zX4MUhVDHtcmHEo_192gyTGy0")


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        name = message.chat.first_name
        bot.send_message(message.chat.id, f'<b>Привет, {name}😀\n\n</b>'
                                              f'<i>Пройди квест!\n'
                                              f'Нажимай на "Начать квест😏"\n\n</i>'
                                              f'<b>Удачи, дорогой мой друг!\n</b>', parse_mode='html', reply_markup=markup_menu1)
    except:
        bot.send_message(message.chat.id, 'Произошла ошибка!\n')


@bot.message_handler(func=lambda message: message.text == "Помощь🙏")
def help_message(message):
    bot.send_message(message.chat.id, 'Свяжись с [Соней](https://t.me/SofiaKurshina)',parse_mode='Markdown',)


@bot.message_handler(func=lambda message: message.text == "Начать квест😏")
def start_quest(message):
    try:
        img = Image()
        img1 = img.scene2()
        with open('location.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
        start = data['locations']['start']['description']
        bot.send_photo(message.chat.id, img1, start, parse_mode='html')
        bot.send_message(message.chat.id, 'Привет!', reply_markup=markup_menu2)
    except:
        bot.send_message(message.chat.id, 'Произошла ошибка!\n'
                                          'Попробуй еще раз.')


@bot.message_handler(func=lambda message: True)
def quest_forest(message):
    try:
        if message.text == "Идем далее🚶‍♀️":
            img = Image()
            img1 = img.scene1()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc1 = data['locations']['scene1']['description']
            bot.send_photo(message.chat.id, img1, loc1, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_quest)
        elif message.text == "Войти в комнату 'Алиса в стране чудес'🧚‍♂️":
            img = Image()
            img1 = img.scene3()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc2 = data['locations']['scene2']['description']
            bot.send_photo(message.chat.id, img1, loc2, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_quest0)
        elif message.text == "Искать ключ для выхода рядом с роляю🎹":
            img = Image()
            img2 = img.scene7()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc3 = data['locations']['scene6']['description']
            bot.send_photo(message.chat.id, img2, loc3, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_menu1)
        elif message.text == "Искать ключ для выхода рядом со шкафом и качелями":
            img = Image()
            img5 = img.scene6()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc4 = data['locations']['scene4']['description']
            bot.send_photo(message.chat.id, img.scene5(), loc4, parse_mode='html')
            bot.send_photo(message.chat.id, img5, loc4, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_quest1)
        elif message.text == "Залезть под качели и поискать там ключик🗝":
            img = Image()
            img6 = img.scene5()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc5 = data['locations']['scene5']['description']
            bot.send_photo(message.chat.id, img6, loc5, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_menu1)
        elif message.text == "Искать ключик в шкафу🗝":
            img = Image()
            img3 = img.scene6()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc7 = data['locations']['scene6']['description']
            bot.send_photo(message.chat.id, img3, loc7, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_menu1)
        elif message.text == "Войти в комнату с пауком🕷":
            img = Image()
            img17 = img.scene12()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc8 = data['locations']['scene7']['description']
            bot.send_photo(message.chat.id, img17, loc8, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_quest6)
        elif message.text == "Слишком стало страшно. Хочу в другую комнату😖":
            img = Image()
            img20 = img.scene4()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc9 = data['locations']['scene8']['description']
            bot.send_photo(message.chat.id, img20, loc9, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_quest)
        elif message.text == "Пойти в аквариум к пауку🕷":
            img = Image()
            img21 = img.scene9()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc10 = data['locations']['scene7']['description']
            bot.send_photo(message.chat.id, img21, loc10, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_quest7)
        elif message.text == "Испугаться и не идти😭":
            img = Image()
            img22 = img.scene10()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc11 = data['locations']['scene6']['description']
            bot.send_photo(message.chat.id, img22, loc11, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_menu1)
        elif message.text == "Пойти к пауку и взять из под него ключ😨":
            img = Image()
            img22 = img.scene8()
            with open('location.json', encoding='utf-8') as json_file:
                data = json.load(json_file)
            loc11 = data['locations']['scene5']['description']
            bot.send_photo(message.chat.id, img22, loc11, parse_mode='html')
            bot.send_message(message.chat.id, '', reply_markup=markup_menu1)
        else:
            bot.send_message(message.chat.id, 'Я незнаю такой команды', reply_markup=markup_menu1)
    except:
        bot.send_message(message.chat.id, 'Произошла ошибка!\n'
                                          'Попробуй еще раз.')


bot.polling()