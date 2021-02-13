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
import requests
translator = Translator()


def translate(text,source,target):
    print("translate chamada")
    url = "https://libretranslate.com/translate"
    payload={'q': text,
        'source': source,
        'target': target}
    response = requests.request("POST", url, data=payload)
    print(response.text)
    print("translate: ",response.json()['translatedText'])
    return response.json()['translatedText']


def detect(text):
    print("detect chamada")
    url = "https://libretranslate.com/detect"
    payload={'q': text}
    print(payload)
    response = requests.request("POST", url, data=payload)
    print(response.text)
    print(response.json()[0]['language'])
    return response.json()[0]['language']

## TO LANGUAGE FUNCTIONS ##

# FUNCTION TO TRANSLATE TO BRAZILIAN PORTUGUESE
def topt(update, context):
    replied_message = update.message.reply_to_message
    
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Doido, tem nada pra traduzir aqui não.")
        return
    print(replied_message.text)
    #print(translate("hello world",detect("hello world"),"pt"))
    translated = translate(replied_message.text,detect(replied_message.text),'pt')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated)

# FUNCTION TO TRANSLATE TO JAPANESE
def toja(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="馬鹿")
        return
    translated = translator.translate(replied_message.text, dest='ja')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

# FUNCTION TO TRANSLATE TO FRENCH

def tofr(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tu es bête?")
        return
    translated = translator.translate(replied_message.text, dest='fr')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)


# FUNCTION TO TRANSLATE TO ITALIAN
def toit(update, context):
    replied_message = update.message.reply_to_message
       
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sei stupido?")
        return
    translated = translator.translate(replied_message.text, dest='it')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

# FUNCTION TO TRANSLATE TO GERMAN
def toge(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumm!")
        return
    translated = translator.translate(replied_message.text, dest='de')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)

# FUNCTION TO TRANSLATE TO ENGLISH
def toen(update, context):
    replied_message = update.message.reply_to_message
        
    if replied_message.text == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Dumb! Give me something to translate.")
        return
    translated = translator.translate(replied_message.text, dest='en')
    update.message.reply_text(reply_to_message_id=replied_message.message_id,text=translated.text)