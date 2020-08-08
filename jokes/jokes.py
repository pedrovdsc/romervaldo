import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

import logging
import time
import sys
from pprint import pprint


def dadJokes(update, context):

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="salve")