import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googletrans import Translator

translator = Translator()

def inline_to_language(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id='Portuguese',
            title='Portuguese',
            input_message_content=InputTextMessageContent(translator.translate(query, dest='pt').text)
        )
    )
    results.append(
        InlineQueryResultArticle(
            id='French',
            title='French',
            input_message_content=InputTextMessageContent(translator.translate(query, dest='fr').text)
        )
    )
    results.append(
        InlineQueryResultArticle(
            id='Italian',
            title='Italian',
            input_message_content=InputTextMessageContent(translator.translate(query, dest='it').text)
        )
    )
    results.append(
        InlineQueryResultArticle(
            id='Japanese',
            title='Japanese',
            input_message_content=InputTextMessageContent(translator.translate(query, dest='ja').text)
        )
    )
    results.append(
        InlineQueryResultArticle(
            id='English',
            title='English',
            input_message_content=InputTextMessageContent(translator.translate(query, dest='en').text)
        )
    )
    results.append(
        InlineQueryResultArticle(
            id='Spanish',
            title='Spanish',
            input_message_content=InputTextMessageContent(translator.translate(query, dest='es').text)
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)
