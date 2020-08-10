import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

import logging
import time
import sys
from pprint import pprint
import random


duolingo_id = -310622858


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
    
def relt(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Só um minuto, humano... Já vou enviar...")
    with open('log_comandos.txt', 'rb') as f:
        context.bot.send_document(chat_id=update.effective_chat.id, document = f)
        
        
def magic8ball(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text='\U0001F3B1')
	replied_message = update.message.reply_to_message
	try:
		var = random.randint(1,8)
		if var == 1:
			answer = "Nem por reza"
		elif var == 2:
			answer = "Não, mas na dúvida, tente mais uma vez."
		elif var == 3:
			answer = "Saia fora, humano! Eu sou de LINHARES e sei do que eu estou falando."
		elif var == 4:
			answer = "Para quem é de Linhares, que nem eu, isso daí não é problema!"
		elif var == 5:
			answer = "Quer um conselho? Fuja da Engenharia Elétrica!"
		elif var == 6:
			answer = "Passarinho que come pedra, lembra que tem cu depois. Faça, mas com cuidado..."
		elif var == 7:
			answer = "Vai lá. Cai de cabeça, humano."
		elif var == 8:
			answer = "Pense melhor. O melhor mesmo é não pensar e fazer mesmo."
		update.message.reply_text(reply_to_message_id=replied_message.message_id,text=answer+'\U0001F3B1')
		#context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
	except:
		print("error")
		context.bot.send_message(
       		chat_id=update.effective_chat.id, text="brrrrrrrrrrrr brbrbrbrbrbrbr meu diodo bzzzz esquerdo EXPLODIU! bzbzbzbzzzzz")
        







    
# Fallback answer


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Repete aí, ser humano. Entendi não.")


