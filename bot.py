from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import sendPhoto
updater = Updater(token='700348901:AAGMYDZZmafglP6O9nAwn_yqpEfpzA8m_iw')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
picture ='https://www.crossed-flag-pins.com/animated-flag-gif/images/Flag_Russia.jpg'

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я - Country_by_flag_bot_436. Скоро будем отгадывать страны по флагу...надеюсь :)')
def textMessage(bot, update):
    if update.message.text == 'Russia':
        response = 'Ну крч столица => Moscow'
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        response = 'Напиши мне мб название своей страны на инглише ))0'
        bot.send_message(chat_id=update.message.chat_id, text=response)
def photo(bot, update):
    bot.sendPhoto(chat_id=update.message.chat_id, https://www.crossed-flag-pins.com/animated-flag-gif/images/Flag_Russia.jpg)

start_handler = CommandHandler('start', start)
text_message_handler = MessageHandler(Filters.text, textMessage)
photo_handler = PhotoHandler('Photo', photo)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()
