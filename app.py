from aiogram import Bot,types,executor,Dispatcher
import requests
import json
token='1988245317:AAErbb8MkxKgBF87kfgx5ZiqyLY5eHjStpQ'
bot=Bot(token=token)
dp=Dispatcher(bot)

from handlers import *
if __name__=='__main__':
    executor.start_polling(dp)