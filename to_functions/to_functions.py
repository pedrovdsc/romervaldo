import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator
from datetime import datetime

import time
import sys
from pprint import pprint

duolingo_id = -1001455037506

translator = Translator()

## TO LANGUAGE FUNCTIONS ##

# FUNCTION TO TRANSLATE TO BRAZILIAN PORTUGUESE
def toportuguese(update, context):
    replied_message = update.message.reply_to_message
    
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Doido, tem nada pra traduzir aqui não.")
        return
    translated = translator.translate(replied_message.text, dest='pt')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)
    if replied_message.chat.id == duolingo_id:
        write_log('topt')


# FUNCTION TO TRANSLATE TO JAPANESE
def tojapanese(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="馬鹿")
        return
    translated = translator.translate(replied_message.text, dest='ja')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)
    if replied_message.chat.id == duolingo_id:
        write_log('toja')
        
# FUNCTION TO TRANSLATE TO JAPANESE
def tospanish(update, context):
	'''
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="??")
        return
    translated = translator.translate(replied_message.text, dest='sp')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)
    if replied_message.chat.id == duolingo_id:
        write_log('tosp')
	'''
	update.message.reply_text(reply_to_message_id=replied_message.message_id,text='\U0001F99E \U0001F336')


# FUNCTION TO TRANSLATE TO FRENCH

def tofrench(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tu es bête?")
        return
    translated = translator.translate(replied_message.text, dest='fr')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)
    if replied_message.chat.id == duolingo_id:
        write_log('tofr')

# FUNCTION TO TRANSLATE TO ITALIAN
def toitalian(update, context):
    replied_message = update.message.reply_to_message
       
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sei stupido?")
        return
    translated = translator.translate(replied_message.text, dest='it')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)
    if replied_message.chat.id == duolingo_id:
        write_log('toit')


# FUNCTION TO TRANSLATE TO GERMAN
def togerman(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumm!")
        return
    translated = translator.translate(replied_message.text, dest='de')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)
    if replied_message.chat.id == duolingo_id:
        write_log('toge')


# FUNCTION TO TRANSLATE TO ENGLISH
def toenglish(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumb! Give me something to translate.")
        return
    translated = translator.translate(replied_message.text, dest='en')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)
    if replied_message.chat.id == duolingo_id:
        write_log('toen')

# ESTA FUNCAO SÓ ESTÁ AQUI PQ NÃO SEI IMPORTAR ELA DE OUTRA PASTA
def write_log(funcao):
    now = datetime.now()
    with open('log_comandos.txt', 'a') as f:
        f.write(funcao+';'+now.strftime('%d/%m/%Y %H:%M') +'\n')

