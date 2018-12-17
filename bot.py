from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='700348901:AAGMYDZZmafglP6O9nAwn_yqpEfpzA8m_iw')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
index=39
Data_countries = {'1':'ru', '2':'se','3':'us','4':'tr','5':'dz','6':'ad','7':'ar','8':'am','9':'au','10':'at','11':'az','12':'by','13':'be','14':'br','15':'bg','16':'ca','17':'cl','18':'co','19':'hr','20':'cu','21':'cz','22':'dk','23':'eg','24':'ee','25':'fi',
'26':'fr','27':'ge','28':'de','29':'gr','30':'hu','31':'is','32':'in','33':'ir','34':'iq','35':'ie','36':'il','37':'it','38':'jm','39':'jp','40':'jo','41':'kz','42':'lv','43':'lt','44':'mx','45':'md','46':'nl','47':'nz','48':'kp','49':'no','50':'cn','51':'pl','52':'pt','53':'ro','54':'rs','55':'sk',
'56':'si','57':'kr','58':'es','59':'ch','60':'ua','61':'gb','62':'uy'}
Data_name_countries ={'Россия':'ru','Швеция':'se','США':'us','Турция':'tr','Алжир':'dz','Азербайджан':'ad','Аргентина':'ar','Армения':'am','Австралия':'au','Австрия':'az','Беларусь':'by','Бельгия':'be','Бразилия':'br','Болгария':'bg','Канада':'ca','Чили':'cl','Колумбия':'co','Хорватия':'hr','Куба':'cu','Чехия':'cz','Дания':'dk',
'Египет':'eg','Эстония':'ee','Финляндия':'fi','Франция':'fr','Грузия':'ge','Германия':'de','Греция':'gr','Венгрия':'hu','Исландия':'is','Индия':'in','Иран':'ir','Ирак':'iq','Ирландия':'ie','Израиль':'il','Италия':'it','Ямайка':'jm','Япония':'jp','Иордан':'jo',
'Казахстан':'kz','Латвия':'lv','Литва':'lt','Мексика':'mx','Молдова':'md','Нидерланды':'nl','Новая Зеландия':'nz','Северная Корея':'kp','Норвегия':'no','Китай':'cn','Польша':'pl','Португалия':'pt','Румыния':'ro','Сербия':'rs','Словакия':'sk','Словения':'si','Южная Корея':'kr','Испания':'es','Швейцария':'ch','Украина':'ua',
'Великобритания':'gb','Уругвай':'uy'}
pic = 'http://flags.fmcdn.net/data/flags/w580/ru.png'
pic2='ru'
def change_flag():
    global pic
    global pic2
    item = Data_countries.popitem()
    pic2 = item[1]
    pic = pic[:index] + pic2 + pic[index + 2:]
def start(bot, update):
    global active_game
    active_game=1
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я - Country_by_flag_bot_436. Сейчас я пришлю тебе фото флага. Твоя задача - написать в ответ название этой страны на русском языке. Игра началась :)')
    bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)
def textMessage(bot, update):
    if active_game==1:
        if update.message.text != '':
            answer=update.message.text
            if Data_name_countries.get(answer)==pic2:
                bot.send_message(chat_id=update.message.chat_id, text='Молодец. Абсолютно верно !')
            else:
                bot.send_message(chat_id=update.message.chat_id, text='А вот и неправильно !')
            change_flag()
            response = 'Вот тебе следующий флаг, что это за страна ?'
            bot.send_message(chat_id=update.message.chat_id, text=response)
            bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Для начала игры напиши /start')


start_handler = CommandHandler('start', start)
restart_handler = CommandHandler('restart', photo)
text_message_handler = CommandHandler(Filters.text, textMessage)
dispatcher.add_handler(restart_handler_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()
