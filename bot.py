import telebot 
from telebot import types
TOKEN = '5050686416:AAEES5S4zFUlN9Rk6Yn7meTI8RCrkPLgXjY'

import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '16-16046_25278_33881.json')
with open(file_path, 'r') as fi:
    pass

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🇺🇿  O`zbekcha')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item2 = types.KeyboardButton('🇷🇺 Русский')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item3 = types.KeyboardButton('🇺🇸 English')


    markup.add(item1, item2,item3)
    bot.send_message (message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
        if message.text  == '🇺🇿  O`zbekcha':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Toshkent')
            item5 = types.KeyboardButton('Andijon viloyati')
            item6 = types.KeyboardButton('Buxoro viloyati')
            item7 = types.KeyboardButton('Fargʻona viloyati')
            item8 = types.KeyboardButton('Jizzax  viloyati')
            item9 = types.KeyboardButton('Namangan viloyati')
            item10 = types.KeyboardButton('Qashqadaryo viloyati')
            backk = types.KeyboardButton('Keyingi')
            bckk = types.KeyboardButton('TILL')
            markup.add(item4,item5, item6, item7, item8, item9, item10, bckk,backk)

            bot.send_message(message.chat.id, '🇺🇿  O`zbekcha', reply_markup=markup)

        elif message.text == 'Keyingi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item11 = types.KeyboardButton('Toshkent viloyati')
            item12 = types.KeyboardButton('Xorazm viloyati')
            item13 = types.KeyboardButton('Samarqand viloyati')
            item14 = types.KeyboardButton('Sirdaryo viloyati')
            item15 = types.KeyboardButton('Surxondaryo viloyati')
            item16 = types.KeyboardButton('Navoiy viloyati')
            item17 = types.KeyboardButton('Qoraqalpogʻiston   Respublikasi')
            backk = types.KeyboardButton('Menu')
            bckk = types.KeyboardButton('Orqaga')    
            markup.add(item11,item12, item13, item14, item15, item16, item17,backk, bckk)
            bot.send_message(message.chat.id, '🇺🇿  O`zbekcha', reply_markup=markup)

        elif message.text == 'Orqaga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Toshkent')
            item5 = types.KeyboardButton('Andijon viloyati')
            item6 = types.KeyboardButton('Buxoro viloyati')
            item7 = types.KeyboardButton('Fargʻona viloyati')
            item8 = types.KeyboardButton('Jizzax  viloyati')
            item9 = types.KeyboardButton('Namangan viloyati')
            item10 = types.KeyboardButton('Qashqadaryo viloyati')
            backk = types.KeyboardButton('Keyingi')
            bckk = types.KeyboardButton('TILL')
            markup.add(item4,item5, item6, item7, item8, item9, item10, bckk,backk)

            bot.send_message(message.chat.id, '🇺🇿 O`zbekcha', reply_markup=markup)


        
        elif message.text == 'Menu':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇿  O`zbekcha')
            item2 = types.KeyboardButton('🇷🇺 Русский')
            item3 = types.KeyboardButton('🇺🇸 English')


            markup.add(item1, item2,item3)
            

        elif message.text == 'TILL':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇿  O`zbekcha')
            item2 = types.KeyboardButton('🇷🇺 Русский')
            item3 = types.KeyboardButton('🇺🇸 English')


            markup.add(item1, item2,item3)
            bot.send_message (message.chat.id, 'Tini tanlang', reply_markup = markup)


        elif message.text == 'Toshkent':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('O’zbekiston milliy universiteti')
            item22 = types.KeyboardButton('Toshkent davlat texnika universiteti')
            item23 = types.KeyboardButton('Toshkent davlat iqtisodiyot universiteti')
            item24 = types.KeyboardButton('O’zbekiston davlat jahon tillari universiteti')
            box5 = types.KeyboardButton('🔙 Ortga')
            markup.add(item4,item24,item23,item22,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)

        elif message.text =='🔙 Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Toshkent')
            item5 = types.KeyboardButton('Andijon viloyati')
            item6 = types.KeyboardButton('Buxoro viloyati')
            item7 = types.KeyboardButton('Fargʻona viloyati')
            item8 = types.KeyboardButton('Jizzax  viloyati')
            item9 = types.KeyboardButton('Namangan viloyati')
            item10 = types.KeyboardButton('Qashqadaryo viloyati')
            backk = types.KeyboardButton('Keyingi')
            bckk = types.KeyboardButton('TILL')
            markup.add(item4,item5, item6, item7, item8, item9, item10, bckk,backk)

            bot.send_message(message.chat.id, 'O`zbekcha', reply_markup=markup)
            

        elif message.text == 'O’zbekiston milliy universiteti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('📲telefon')
            box8 = types.KeyboardButton('📧Manzl')
            box9 = types.KeyboardButton('💻Sayt')
            bckk = types.KeyboardButton('Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Ma’lumot tanlang', reply_markup=markup)

        elif message.text == '📧Manzl':
            bot.send_message(message.chat.id,  'O’zbekiston milliy universiteti         Manzil: Vuzgorodok, Toshkent, 100174')
        elif message.text == '📲telefon':         
            bot.send_message(message.chat.id,  'Telefon: (+998-71) 227-12-24,        Telefon:(+998-71) 246-53-21')
        elif message.text == '💻Sayt': 
            bot.send_message(message.chat.id,  'Websait: http://www.nuu.uz')



        elif message.text == 'Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('O’zbekiston milliy universiteti')
            item22 = types.KeyboardButton('Toshkent davlat texnika universiteti')
            item23 = types.KeyboardButton('Toshkent davlat iqtisodiyot universiteti')
            item24 = types.KeyboardButton('O’zbekiston davlat jahon tillari universiteti')
            box5 = types.KeyboardButton('🔙 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)

        elif message.text == 'Toshkent davlat texnika universiteti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('📱telfon')
            box8 = types.KeyboardButton('🗺Manzll')
            box9 = types.KeyboardButton('🖥Sayti')
            bckk = types.KeyboardButton('Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Ma’lumot tanlang', reply_markup=markup)

        elif message.text == '🗺Manzll':
            bot.send_message(message.chat.id,  'Toshkent davlat texnika universiteti Manzil:Universitetskaya ko’ch., 2 Toshkent, 100095')
        elif message.text == '📱telfon':         
            bot.send_message(message.chat.id,  'Telefon: (+998-71) 246-46-00,     Telefon:+998-71) 227-10-32 ')
        elif message.text == '🖥Sayti': 
            bot.send_message(message.chat.id,  'Websait:https://tstu.uz/?page_id=6286&lang=ru')
    
        elif message.text == 'Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('O’zbekiston milliy universiteti')
            item22 = types.KeyboardButton('Toshkent davlat texnika universiteti')
            item23 = types.KeyboardButton('Toshkent davlat iqtisodiyot universiteti')
            item24 = types.KeyboardButton('O’zbekiston davlat jahon tillari universiteti')
            box5 = types.KeyboardButton('🔙 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)


        elif message.text == 'Toshkent davlat iqtisodiyot universiteti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('telfon')
            box8 = types.KeyboardButton('Manzll')
            box9 = types.KeyboardButton('Sayti')
            bckk = types.KeyboardButton('Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Ma’lumot tanlang', reply_markup=markup)

        elif message.text == 'Manzll':
            bot.send_message(message.chat.id,  'Toshkent davlat iqtisodiyot universitetiManzil: Uzbekistanskaya koch, 49  Toshkent, 100003')
        elif message.text == 'telfon':         
            bot.send_message(message.chat.id,  'Telefon: (+998-71) 232-64-21,,      (+998-71) 239-41-23 ')
        elif message.text == 'Sayti': 
            bot.send_message(message.chat.id,  'Websait: https://yangi.tsue.uz/uz/static/international-hiedtech')
    
        elif message.text == 'Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('O’zbekiston milliy universiteti')
            item22 = types.KeyboardButton('Toshkent davlat texnika universiteti')
            item23 = types.KeyboardButton('Toshkent davlat iqtisodiyot universiteti')
            item24 = types.KeyboardButton('O’zbekiston davlat jahon tillari universiteti')
            box5 = types.KeyboardButton('🔙 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)

        elif message.text == 'O’zbekiston davlat jahon tillari universiteti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('📞telfon')
            box8 = types.KeyboardButton('🎴Manzll')
            box9 = types.KeyboardButton('🖲Sayti')
            bckk = types.KeyboardButton('Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Ma’lumot tanlang', reply_markup=markup)

        elif message.text == '🎴Manzll':
            bot.send_message(message.chat.id,  'O’zbekiston davlat jahon tillari universitetiManzil: Kichik Xalqa Yoli ko’ch, 21a, Toshkent 100138')
        elif message.text == '📞telfon':         
            bot.send_message(message.chat.id,  'Telefon: (+998-71) 275-77-95,      Telefon:(+998-71) 275-59-08')
        elif message.text == '🖲Sayti': 
            bot.send_message(message.chat.id,  'Websait: http://www.uzswlu.uz')


        elif message.text == 'Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('O’zbekiston milliy universiteti')
            item22 = types.KeyboardButton('Toshkent davlat texnika universiteti')
            item23 = types.KeyboardButton('Toshkent davlat iqtisodiyot universiteti')
            item24 = types.KeyboardButton('O’zbekiston davlat jahon tillari universiteti')
            box5 = types.KeyboardButton('🔙 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Ma’lumot tanlang', reply_markup=markup)






        elif message.text == 'Andijon viloyati':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Andijon davlat universiteti')
            item22 = types.KeyboardButton('Andijon qishloq xo’jaligi instituti')
            item23 = types.KeyboardButton('Andijon davlat tibbiyot instituti')
            item24 = types.KeyboardButton('Andijon mashinasozlik instituti')
            box5 = types.KeyboardButton('🔙 Ortga')
            markup.add(item4,item24,item23,item22,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)

        elif message.text =='🔙 Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Toshkent')
            item5 = types.KeyboardButton('Andijon viloyati')
            item6 = types.KeyboardButton('Buxoro viloyati')
            item7 = types.KeyboardButton('Fargʻona viloyati')
            item8 = types.KeyboardButton('Jizzax  viloyati')
            item9 = types.KeyboardButton('Namangan viloyati')
            item10 = types.KeyboardButton('Qashqadaryo viloyati')
            backk = types.KeyboardButton('Keyingi')
            bckk = types.KeyboardButton('TILL')
            markup.add(item4,item5, item6, item7, item8, item9, item10, bckk,backk)

            bot.send_message(message.chat.id, 'O`zbekcha', reply_markup=markup)
            

        elif message.text == 'Andijon davlat universiteti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('👩🏻‍🎓telefon')
            box8 = types.KeyboardButton('🧑🏻Manzl')
            box9 = types.KeyboardButton('👩🏻‍💻Sayt')
            bckk = types.KeyboardButton('🔚Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Kantakni tanlang', reply_markup=markup)

        elif message.text == '🧑🏻Manzl':
            bot.send_message(message.chat.id,  'Universitetskaya koʻch, 129 Andijan 110000')
        elif message.text == '👩🏻‍🎓telefon':         
            bot.send_message(message.chat.id,  'Telefon:(+998- 374) 223 88 ,        Telefon:(+998-71) 246-53-21')
        elif message.text == '👩🏻‍💻Sayt': 
            bot.send_message(message.chat.id,  'Websait: www.adu.uz')



        elif message.text == '🔚Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Andijon davlat universiteti')
            item22 = types.KeyboardButton('Andijon qishloq xo’jaligi instituti')
            item23 = types.KeyboardButton('Andijon davlat tibbiyot instituti')
            item24 = types.KeyboardButton('Andijon mashinasozlik instituti')
            box5 = types.KeyboardButton('🔙 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)

        elif message.text == 'Andijon mashinasozlik instituti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('🧑telfon')
            box8 = types.KeyboardButton('👩‍💼Manzll')
            box9 = types.KeyboardButton('👨‍💻Sayti')
            bckk = types.KeyboardButton('🔚Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Kantakni tanlang', reply_markup=markup)

        elif message.text == '👩‍💼Manzll':
            bot.send_message(message.chat.id,  'Bobur ko’ch, 56 Andijan, 110019')
        elif message.text == '🧑telfon':         
            bot.send_message(message.chat.id,  'Telefon:(+998-  374) 222-16-30, 224-75-10,     Telefon:(+998-374) 224-72-45')
        elif message.text == '👨‍💻Sayti': 
            bot.send_message(message.chat.id,  'http://www.andmii.uz')
    
        elif message.text == '🔚Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Andijon davlat universiteti')
            item22 = types.KeyboardButton('Andijon qishloq xo’jaligi instituti')
            item23 = types.KeyboardButton('Andijon davlat tibbiyot instituti')
            item24 = types.KeyboardButton('Andijon mashinasozlik instituti')
            box5 = types.KeyboardButton('🔙 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)


        elif message.text == 'Andijon davlat tibbiyot instituti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('☎️telfon')
            box8 = types.KeyboardButton('📺Manzll')
            box9 = types.KeyboardButton('⌨️Sayti')
            bckk = types.KeyboardButton('🔚Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Kantakni tanlang', reply_markup=markup)

        elif message.text == '📺Manzll':
            bot.send_message(message.chat.id,  'Navoi ko’ch, 124, Andijon, 110015')
        elif message.text == '☎️telfon':         
            bot.send_message(message.chat.id,  'Telefon:(+998- 374) 237-11-41,      Telefon:(+998-374) 237-54-33, 256-45-04')
        elif message.text == '⌨️Sayti': 
            bot.send_message(message.chat.id,  'Websait:http://www.adti.uz/')
    
        elif message.text == '🔚Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Andijon davlat universiteti')
            item22 = types.KeyboardButton('Andijon qishloq xo’jaligi instituti')
            item23 = types.KeyboardButton('Andijon davlat tibbiyot instituti')
            item24 = types.KeyboardButton('Andijon mashinasozlik instituti')
            box5 = types.KeyboardButton('🔚 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)

        elif message.text == 'Andijon qishloq xo’jaligi instituti':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('🧝‍♀️telfon')
            box8 = types.KeyboardButton('🧛‍♀️Manzll')
            box9 = types.KeyboardButton('🤵🏻Sayti')
            bckk = types.KeyboardButton('🔚Ortga')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Kantakni tanlang', reply_markup=markup)

        elif message.text == '🧛‍♀️Manzll':
            bot.send_message(message.chat.id,  'Andijon viloyati, Kuyganyar 111529')
        elif message.text == '🧝‍♀️telfon':         
            bot.send_message(message.chat.id,  'Telefon:(+998- 374) 223-90-69,      Faks: (+998-374) 373-13-63')
        elif message.text == '🤵🏻Sayti': 
            bot.send_message(message.chat.id,  'Websait:http://andqxi.uz/uz/')


        elif message.text == 'Ortga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Andijon davlat universiteti')
            item22 = types.KeyboardButton('Andijon qishloq xo’jaligi instituti')
            item23 = types.KeyboardButton('Andijon davlat tibbiyot instituti')
            item24 = types.KeyboardButton('Andijon mashinasozlik instituti')
            box5 = types.KeyboardButton('🔚 Ortga')
            bckk = types.KeyboardButton('Menu')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)



        if message.text  == '🇷🇺 Русский':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Тошкент')
            item5 = types.KeyboardButton('Андижанская область')
            item6 = types.KeyboardButton('Бухарская область')
            item7 = types.KeyboardButton('Ферганская область')
            item8 = types.KeyboardButton('Джизакская область')
            item9 = types.KeyboardButton('Наманганская область')
            item10 = types.KeyboardButton('Кашкадарьинская область')
            backk = types.KeyboardButton('Далее')
            bckk = types.KeyboardButton('Языки')
            markup.add(item4,item5, item6, item7, item8, item9, item10, bckk,backk)

            bot.send_message(message.chat.id, '🇺🇿  O`zbekcha', reply_markup=markup)

        elif message.text == 'Далее':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item11 = types.KeyboardButton('Ташкентская область')
            item12 = types.KeyboardButton('Хорезмская область')
            item13 = types.KeyboardButton('Самарканская область')
            item14 = types.KeyboardButton('Сырдарьинская область')
            item15 = types.KeyboardButton('Сурхандарьинская область')
            item16 = types.KeyboardButton('Навоийская область')
            item17 = types.KeyboardButton('Республика Каракалпакстан')
            backk = types.KeyboardButton('Меню')
            bckk = types.KeyboardButton('Назад')    
            markup.add(item11,item12, item13, item14, item15, item16, item17,backk, bckk)
            bot.send_message(message.chat.id, '🇺🇿  O`zbekcha', reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Тошкент')
            item5 = types.KeyboardButton('Андижанская область')
            item6 = types.KeyboardButton('Бухарская область')
            item7 = types.KeyboardButton('Fargʻona viloyati')
            item8 = types.KeyboardButton('Ферганская область')
            item9 = types.KeyboardButton('Джизакская область')
            item10 = types.KeyboardButton('Наманганская область')
            backk = types.KeyboardButton('Далее')
            bckk = types.KeyboardButton('Языки')
            markup.add(item4,item5, item6, item7, item8, item9, item10, bckk,backk)

            bot.send_message(message.chat.id, '🇺🇿 O`zbekcha', reply_markup=markup)


        
        elif message.text == 'Меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇿  O`zbekcha')
            item2 = types.KeyboardButton('🇷🇺 Русский')
            item3 = types.KeyboardButton('🇺🇸 English')


            markup.add(item1, item2,item3)
            

        elif message.text == 'Языки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🇺🇿  O`zbekcha')
            item2 = types.KeyboardButton('🇷🇺 Русский')
            item3 = types.KeyboardButton('🇺🇸 English')


            markup.add(item1, item2,item3)
            bot.send_message (message.chat.id, 'Tini tanlang', reply_markup = markup)


        elif message.text == 'Тошкент':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Национальный университет узбекистана')
            item22 = types.KeyboardButton('Ташкентский Государственный Технический')
            item23 = types.KeyboardButton('Ташкентский Государственный Экономический Университет')
            item24 = types.KeyboardButton('Узбекский государственный университет мировых языков')
            box5 = types.KeyboardButton('🔙Назад')
            markup.add(item4,item24,item23,item22,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)

        elif message.text =='🔙Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Тошкент')
            item5 = types.KeyboardButton('Андижанская область')
            item6 = types.KeyboardButton('Бухарская область')
            item7 = types.KeyboardButton('Ферганская область')
            item8 = types.KeyboardButton('Джизакская область')
            item9 = types.KeyboardButton('Наманганская область')
            item10 = types.KeyboardButton('Кашкадарьинская область')
            backk = types.KeyboardButton('Далее')
            bckk = types.KeyboardButton('Языки')
            markup.add(item4,item5, item6, item7, item8, item9, item10, bckk,backk)

            bot.send_message(message.chat.id, 'O`zbekcha', reply_markup=markup)
            

        elif message.text == 'Национальный университет узбекистана':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            box7 = types.KeyboardButton('📲Телефон')
            box8 = types.KeyboardButton('📧Локация')
            box9 = types.KeyboardButton('💻Сайт')
            bckk = types.KeyboardButton('Назад')
            markup.add(box7,box8,box9, bckk)

            bot.send_message(message.chat.id, 'Виберте информацию', reply_markup=markup)

        elif message.text == '📧локация':
            bot.send_message(message.chat.id,  'O’zbekiston milliy universiteti         Manzil: Vuzgorodok, Toshkent, 100174')
        elif message.text == '📲Телефон':         
            bot.send_message(message.chat.id,  'Telefon: (+998-71) 227-12-24,        Telefon:(+998-71) 246-53-21')
        elif message.text == '💻Сайт': 
            bot.send_message(message.chat.id,  'Websait: http://www.nuu.uz')



        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item4 = types.KeyboardButton('Узбекский государственный университет мировых языков')
            item22 = types.KeyboardButton('Ташкентский Государственный Технический')
            item23 = types.KeyboardButton('Ташкентский Государственный Экономический Университет')
            item24 = types.KeyboardButton('Узбекский государственный университет мировых языков')
            box5 = types.KeyboardButton('🔙Назад')
            bckk = types.KeyboardButton('Меню')
            markup.add(item4,item22,item23,item24,box5)
            bot.send_message(message.chat.id, 'Univerni tanlang', reply_markup=markup)
                
bot.polling(none_stop = True)