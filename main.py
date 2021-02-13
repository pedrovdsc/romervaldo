# Código feito por Pedro Custódio, Arthur Lorencini, Maiky Barreto, João Nunes. 


# Importando os módulos importantes

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator

from to_functions import toen, tofr, toge, toit, toja, topt
from general import caps, start, unknown, commands,catgirl,magic8ball

import logging
import time
import sys
from pprint import pprint


## Language handlers ##

def wrapper_commandHandler(command,dispatcher):
    dispatcher.add_handler(CommandHandler(command.__name__, command))
    print(command.__name__,"foi embalada!")

def main():
    # Create the Updater and pass it your bot's token.


    # início do código

    TOKEN = sys.argv[1]

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher


    logging.basicConfig(filename = 'log_comandos.log',
                        filemode = 'a', level = logging.INFO,
                        format = '%(message)s;%(asctime)s', datefmt='%d/%m/%Y')
    duolingo_id = -1001455037506

    # inicializando todos os comandos

    print ('Bot ligado')

    commandList = [start,
                    commands,caps,catgirl,magic8ball,
                    toen,topt,toja,toit,toge,tofr]
    for command in commandList:
        wrapper_commandHandler(command,dispatcher)

    # Por algum motivo ele tem que ficar no final
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the Bot
    updater.start_polling()

if __name__ == '__main__':
    main()


