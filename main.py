# Código feito por Pedro Custódio, Arthur Lorencini, Maiky Barreto, João Nunes. 


# Importando os módulos importantes

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator

import logging
import time
import sys
from pprint import pprint

# Aqui o token é atribuido para uma string que é chamada na execução do comando
# na linha de comando do terminal $ python main.py (token em algum lugar remoto)

TOKEN = sys.argv[1]


# Aqui, a função do uptader deve atenticar e usar o bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

translator = Translator()

def debug_message(message):
    ''' função de debug que aparece no computador do pedro para ele debugar
    '''
    print('####################################')
    print(message.date)
    print(f'username: {message.from_user.username}')
    pprint(message.from_user.name)
    print(f'id: {message.from_user.id}')
    print(f'chat_id: {message.chat_id}')
    print(f'message_id: {message.message_id}')
    print('Text: \n' +message.text)
    print('####################################')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# def echo(update, context):
#     """Echo the user message."""
#     pprint('########################')
#     pprint(update.message.chat.username)
#     pprint(update.message.chat.id)
#     pprint('-----------------------')
#     pprint(update.message.reply_to_message)
#     pprint('########################')
#     update.message.reply_text(update.message.text)

# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

def caps(update, context):
    print(context.args)
    print(len(context.args))
    #text_caps = ' '.join(context.args).upper()
    replied_message = update.message.reply_to_message
    text_caps = replied_message.text.upper()
    # pprint('########################')
    # pprint(update.message.chat.username)
    # pprint(update.message.chat.id)
    # pprint('-----------------------')
    # pprint(update.message.reply_markup)
    # pprint('-----------------------')
    # pprint(dir(update.message.reply_markdown_v2))
    # pprint('-----------------------')
    # pprint(dir(update.message.reply_markdown))
    # pprint('########################')
    #update.message.reply_text(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

## TO LANGUAGE FUNCTIONS ##

def to_portuguese(update, context):
    replied_message = update.message.reply_to_message
    debug_message(replied_message)
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Doido, tem nada pra traduzir aqui não.")
        return
    translated = translator.translate(replied_message.text, dest='pt')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

to_portuguese_handler = CommandHandler('topt', to_portuguese)
dispatcher.add_handler(to_portuguese_handler)

def to_french(update, context):
    replied_message = update.message.reply_to_message
    debug_message(replied_message)
    
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tu es bête?")
        return
    translated = translator.translate(replied_message.text, dest='fr')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

to_french_handler = CommandHandler('tofr', to_french)
dispatcher.add_handler(to_french_handler)

def toitalian(update, context):
    replied_message = update.message.reply_to_message
    debug_message(replied_message)
    
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sei stupido?")
        return
    translated = translator.translate(replied_message.text, dest='it')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

toitalian_handler = CommandHandler('toit', toitalian)
dispatcher.add_handler(toitalian_handler)

def tojapanese(update, context):
    replied_message = update.message.reply_to_message
    debug_message(replied_message)
    
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="馬鹿")
        return
    translated = translator.translate(replied_message.text, dest='ja')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

tojapanese_handler = CommandHandler('toja', tojapanese)
dispatcher.add_handler(tojapanese_handler)

def togerman(update, context):
    replied_message = update.message.reply_to_message
    debug_message(replied_message)
    
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumm!")
        return
    translated = translator.translate(replied_message.text, dest='de')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

togerman_handler = CommandHandler('toge', togerman)
dispatcher.add_handler(togerman_handler)

def toenglish(update, context):
    replied_message = update.message.reply_to_message
    debug_message(replied_message)
    
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumb! Give me something to translate.")
        return
    translated = translator.translate(replied_message.text, dest='en')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

toenglish_handler = CommandHandler('toen', toenglish)
dispatcher.add_handler(toenglish_handler)


## END OF TO LANGUAGE FUNCTIONS ##

def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

## Telegram Bot functions ##
## 1) /commands
## 2) /start

# def commands(update, context):
#     replied_message = update.message.reply_to_message
#     list_commands = "/commands - Exibe a lista de comandos;\
#         \n/start - Exibe a saudação inicial;\
#         \n/toja - Traduz a frase para o japonês;\
#         \n/toen - Traduz a frase para o inglês;\
#         \n/tofr - Traduz a frase para o francês;\
#         \n/toal - Traduz a frase para o alemão;\
#         \n/topt - Traduz a frase para o português\
#         \n/caps - FICA TUDO EM CAPSLOCK.
#         "

#     context.bot.send_message(chat_id=update.effective_chat.id, text=list_commands)

# # Cria o handler para segurar o evento quando acontecer.
# commands_handler = MessageHandler(Filters.command, commands)
# dispatcher.add_handler(commands_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Repete aí, doido. Entendi não.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

print ('Bot ligado')
