from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='700348901:AAGMYDZZmafglP6O9nAwn_yqpEfpzA8m_iw')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я - Country_by_flag_bot_436. Скоро будем отгадывать страны по флагу...надеюсь :)')
def textMessage(bot, update):
    response = 'Я пока ни черта не умею)))00 Но вижу, что ты написал мне:' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

start_handler = CommandHandler('start', start)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()
