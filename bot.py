from os import environ
def main():
    application.listen(environ["80"])
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='700348901:AAGMYDZZmafglP6O9nAwn_yqpEfpzA8m_iw')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

start_handler = CommandHandler('start', start)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()
