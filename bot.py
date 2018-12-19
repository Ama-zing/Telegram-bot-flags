from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='700348901:AAGMYDZZmafglP6O9nAwn_yqpEfpzA8m_iw')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
index = 39
Data_countries = {'1': 'ru', '2': 'se', '3': 'us', '4': 'tr', '5': 'dz', '6': 'az', '7': 'ar', '8': 'am', '9': 'au',
                  '10': 'at', '11': 'by', '12': 'be', '13': 'br', '14': 'bg', '15': 'ca', '16': 'cl',
                  '17': 'co', '18': 'hr', '19': 'cu', '20': 'cz', '21': 'dk', '22': 'eg', '23': 'ee', '24': 'fi',
                  '25': 'fr', '26': 'ge', '27': 'de', '28': 'gr', '29': 'hu', '30': 'is', '31': 'in', '32': 'ir',
                  '33': 'iq', '34': 'ie', '35': 'il', '36': 'it', '37': 'jm', '38': 'jp', '39': 'jo', '40': 'kz',
                  '41': 'lv', '42': 'lt', '43': 'mx', '44': 'md', '45': 'nl', '46': 'nz', '47': 'kp', '48': 'no',
                  '49': 'cn', '50': 'pl', '51': 'pt', '52': 'ro', '53': 'rs', '54': 'sk',
                  '55': 'si', '56': 'kr', '57': 'es', '58': 'ch', '59': 'ua', '60': 'gb', '61': 'uy'}
Data_name_countries = {'Россия': 'ru', 'Швеция': 'se', 'США': 'us', 'Турция': 'tr', 'Алжир': 'dz','Азербайджан':'az', 'Аргентина': 'ar',
                       'Армения': 'am', 'Австралия': 'au', 'Австрия': 'at','Беларусь':'by', 'Бельгия': 'be', 'Бразилия': 'br',
                       'Болгария': 'bg', 'Канада': 'ca', 'Чили': 'cl', 'Колумбия': 'co', 'Хорватия': 'hr', 'Куба': 'cu',
                       'Чехия': 'cz', 'Дания': 'dk', 'Египет': 'eg', 'Эстония': 'ee', 'Финляндия': 'fi', 'Франция': 'fr', 'Грузия': 'ge',
                       'Германия': 'de', 'Греция': 'gr', 'Венгрия': 'hu', 'Исландия': 'is', 'Индия': 'in', 'Иран': 'ir',
                       'Ирак': 'iq', 'Ирландия': 'ie', 'Израиль': 'il', 'Италия': 'it', 'Ямайка': 'jm', 'Япония': 'jp',
                       'Иордан': 'jo', 'Казахстан': 'kz', 'Латвия': 'lv', 'Литва': 'lt', 'Мексика': 'mx', 'Молдавия': 'md',
                       'Нидерланды': 'nl', 'Новая Зеландия': 'nz', 'Северная Корея': 'kp', 'Норвегия': 'no',
                       'Китай': 'cn', 'Польша': 'pl', 'Португалия': 'pt', 'Румыния': 'ro', 'Сербия': 'rs',
                       'Словакия': 'sk', 'Словения': 'si', 'Южная Корея': 'kr', 'Испания': 'es', 'Швейцария': 'ch',
                       'Украина': 'ua', 'Великобритания': 'gb', 'Уругвай': 'uy'}
Data_name_countries_reversed=dict(map(reversed, Data_name_countries.items()))
pic = 'http://flags.fmcdn.net/data/flags/w580/ru.png'
pic2 = 'ru'


def change_flag():
    global pic
    global pic2
    random_num=(random.choice(list(Data_countries.keys())))
    number_for_dict = str(random_num)
    pic2 = Data_countries.get(number_for_dict)
    pic = pic[:index] + pic2 + pic[index + 2:]


def start(bot, update):
    global active_game
    active_game = 1
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я - Country_by_flag_bot_436. Сейчас я пришлю тебе фото флага. Твоя задача - написать в ответ название этой страны на русском языке. Игра началась :)')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)


def textMessage(bot, update):
    if active_game == 1:
        if update.message.text != '':
            answer = update.message.text
            if Data_name_countries.get(answer) == pic2:
                bot.send_message(chat_id=update.message.chat_id, text='Молодец. Абсолютно верно !')
            else:
                Right_answer=Data_name_countries_reversed.get(pic2)
                bot.send_message(chat_id=update.message.chat_id, text='А вот и неправильно !')
                bot.send_message(chat_id=update.message.chat_id,text='Правильный ответ:' +Right_answer)
            change_flag()
            response = 'Вот тебе следующий флаг, что это за страна ?'
            bot.send_message(chat_id=update.message.chat_id, text=response)
            bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Для начала игры напиши /start')


def photo(bot, update):
    bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)


start_handler = CommandHandler('start', start)
photo_handler = CommandHandler('photo', photo)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()
