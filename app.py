from aiogram import Bot,types,executor,Dispatcher
import requests
import json
token='Telegram Token'
bot=Bot(token=token)
dp=Dispatcher(bot)

from handlers import *
if __name__=='__main__':
    executor.start_polling(dp)