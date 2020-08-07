# Código feito por Pedro Custódio, Arthur Lorencini, Maiky Barreto, João Nunes. 


# Importando os módulos importantes

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator

from to_functions.to_functions import toenglish, tofrench, togerman, toitalian, tojapanese, toportuguese
from bot_functions.general import caps, start, unknown, commands, relt

import logging
import time
import sys
from pprint import pprint

TOKEN = sys.argv[1]

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

duolingo_id = -1001455037506

translator = Translator()

def debug_message(message):
    print('####################################')
    print(message.date)
    print(f'username: {message.from_user.username}')
    pprint(message.from_user.name)
    print(f'id: {message.from_user.id}')
    print(f'chat_id: {message.chat_id}')
    print(f'message_id: {message.message_id}')
    print('Text: \n' +message.text)
    print('####################################')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

## Não sei oq isso faz ainda.
updater.start_polling()

## General handlers

commands_handler = CommandHandler('commands', commands)
dispatcher.add_handler(commands_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

relt_handler = CommandHandler('relt', relt)
dispatcher.add_handler(relt_handler)


## Language handlers ##

toportuguese_handler = CommandHandler('topt', toportuguese)
dispatcher.add_handler(toportuguese_handler)

tofrench_handler = CommandHandler('tofr', tofrench)
dispatcher.add_handler(tofrench_handler)

toitalian_handler = CommandHandler('toit', toitalian)
dispatcher.add_handler(toitalian_handler)

tojapanese_handler = CommandHandler('toja', tojapanese)
dispatcher.add_handler(tojapanese_handler)

togerman_handler = CommandHandler('toge', togerman)
dispatcher.add_handler(togerman_handler)

toenglish_handler = CommandHandler('toen', toenglish)
dispatcher.add_handler(toenglish_handler)


## End of Language Handlers ##

# Por algum motivo ele tem que ficar no final
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


print ('Bot ligado')
