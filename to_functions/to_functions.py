import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator

import time
import sys
from pprint import pprint

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

# FUNCTION TO TRANSLATE TO JAPANESE
def tojapanese(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="馬鹿")
        return
    translated = translator.translate(replied_message.text, dest='ja')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

# FUNCTION TO TRANSLATE TO FRENCH

def tofrench(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tu es bête?")
        return
    translated = translator.translate(replied_message.text, dest='fr')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)


# FUNCTION TO TRANSLATE TO ITALIAN
def toitalian(update, context):
    replied_message = update.message.reply_to_message
       
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sei stupido?")
        return
    translated = translator.translate(replied_message.text, dest='it')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

# FUNCTION TO TRANSLATE TO GERMAN
def togerman(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumm!")
        return
    translated = translator.translate(replied_message.text, dest='de')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

# FUNCTION TO TRANSLATE TO ENGLISH
def toenglish(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumb! Give me something to translate.")
        return
    translated = translator.translate(replied_message.text, dest='en')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)