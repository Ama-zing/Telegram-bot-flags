from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
updater = Updater(token='700348901:AAGMYDZZmafglP6O9nAwn_yqpEfpzA8m_iw')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
index=39
Data_countries = {'1':'ru', '2':'se','3':'us','4':'tr'}

def change_flag():
    global pic
    pic = 'http://flags.fmcdn.net/data/flags/w580/ru.png'
    random_num = random.randint(1, 4)
    number_for_dict = str(random_num)
    pic2 = Data_countries.get(number_for_dict)
    pic = pic[:index] + pic2 + pic[index + 2:]
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я - Country_by_flag_bot_436. Скоро будем отгадывать страны по флагу...надеюсь :)')
def textMessage(bot, update):
    if update.message.text != '':
        change_flag()
        response = 'Вот тебе флаг'
        bot.send_message(chat_id=update.message.chat_id, text=response)
        bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)
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
