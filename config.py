import os
from telethon import TelegramClient

api_id = "1492128"
api_hash = "496a1aab7943406f28e3de49fff16ea2"
bot_token = "1846864781:AAF7SauEaJYylzljXtya8vQ_dVI-eldizm4"

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

