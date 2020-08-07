import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

import logging
import time
import sys
from pprint import pprint


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salve!\
    \nEu sou o Romervaldo \U0001F916 \U0001F30E e estou aqui para te ajudar a aprender idiomas!\
    \nFeito por Pedro, Arthur, Maiky e Nunes. Todos bonitos de coração.")


def commands(update, context):
    list_commands = "/commands - Exibe esta lista de comandos;\
        \n/start - Exibe a saudação inicial;\
        \n/toja - Traduz a frase para o japonês;\
        \n/toen - Traduz a frase para o inglês;\
        \n/tofr - Traduz a frase para o francês;\
        \n/toge - Traduz a frase para o alemão;\
        \n/topt - Traduz a frase para o português\
        \n/toit - Traduz a frase para o italiano\
        \n/caps - FICA TUDO EM CAPSLOCK."

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=list_commands)

# FUNCTION TO PUT LETTERS IN CAPS


def caps(update, context):
    replied_message = update.message.reply_to_message
    text_caps = replied_message.text.upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# Fallback answer


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Repete aí, ser humano. Entendi não.")

def relt(update, context):
    file2 = open('log_comandos.txt', 'rb')
    context.bot.send_message(chat_id=update.effective_chat.id, text="calma")
    context.bot.send_document(chat_id=update.effective_chat.id, document = file2)

def write_log(funcao):
    arquivo_log = open('log_comandos.txt','a')
    arquivo_log.write(funcao+time.strftime('%d/%m/%Y') +'\n')
    arquivo_log.close()
