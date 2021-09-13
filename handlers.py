from aiogram import types
from aiogram.types import reply_keyboard
from aiogram.types.message import ParseMode
from app import bot,dp
from keyboards import btn
from api import link,flag,wikipedia
from googletrans import Translator
from google_trans_new import google_translator
tarjimon=Translator()
@dp.message_handler(commands=['start'])
async def welcome(message:types.Message):
    text='<b>✋ Assalomu aleykum!</b>'+'\n'+"<b>🌎 Dunyo davlatlari haqida barcha ma'lumot shu yerda!!!</b>"+'\n'+"<b>✅ Shunchaki botga davlat nomini to'g'ri yozsangiz bo'ldi!</b>"
    await bot.send_message(message.chat.id,text,parse_mode='html',reply_markup=btn)
@dp.message_handler(content_types=['text'])
async def asosiy(message:types.Message):
    text=message.text
    await bot.send_message(message.chat.id,"<b>🔁Iltimos kuting sizning so'rovingiz bajarilmoqda!!!</b>",parse_mode='html')
    def countryinfo(text):
        import requests
        import json
        from googletrans import Translator
        tarjimon=Translator()
        name=tarjimon.translate(text,dest='en')
        url='https://restcountries.eu/rest/v2/name/'+name.text
        response=requests.get(url)
        rest=json.loads(response.text)
  #  return 
        if response.status_code==404:
         return 'Xatolik'
        else:
          davlatnomi=tarjimon.translate(rest[0]['name'],dest='uz')
          poytaxt= tarjimon.translate(rest[0]['capital'],dest='uz')
          aholi=rest[0]['population']
          maydoni=rest[0]['area']
          millat=tarjimon.translate(rest[0]['languages'][0]['nativeName'],dest='uz').text
          valyutanomi=tarjimon.translate(rest[0]['currencies'][0]['name'],dest='uz').text
          valyutakodi=rest[0]['currencies'][0]['code']
          for i in rest[0]['topLevelDomain']:
                 i=i+'\n'
          domain=i
          for k in rest[0]['callingCodes']:
                     k='+'+k+'\n'
          telefonkod=k   
          hudud=tarjimon.translate(rest[0]['region'],dest='uz').text+'da joylashgan!'

          result="Mamlakat nomi:"+davlatnomi.text+"\n"+'Poytaxti:'+poytaxt.text+"\n"+'Aholi soni:'+str(aholi)+' ta'+"\n"+"Maydoni:"+str(maydoni)+' kv km'+"\n"+'Millat nomi:'+millat+"\n"+"Til:"+millat+"\n"+'Valyuta nomi:'+valyutanomi+'\n'+"Valyuta kodi:"+valyutakodi+"\n"+'Domen:'+domain+"\n"+'Telefon raqam kodi:'+telefonkod+"\n"+hudud
          return result
    caption=countryinfo(text)
    if caption=='Xatolik':
        await bot.send_message(message.chat.id,"<b>❗️Diqqatli bo'ling! Davlat nomini xato kiritdingiz! Davlat nomini qayta kiriting!</b>",parse_mode='html')
    else:
        import requests
        import json
        from googletrans import Translator
        tarjimon=Translator()
        name=tarjimon.translate(text,dest='en')
        wik=tarjimon.translate(text,dest='uz')
        url='https://restcountries.eu/rest/v2/name/'+name.text
        response=requests.get(url)
        rest=json.loads(response.text)
        image=flag(text)
        url=link(text)
        wikilink=urlmanzil='https://uz.wikipedia.org/wiki/'+wik.text
        btn1=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton("Json format",url=url)
        button2=types.InlineKeyboardButton("Wikipediadan o'qish",url=wikilink)
        btn1.add(button1,button2)
        code=rest[0]['alpha2Code'].lower()
        photo='https://flagcdn.com/h120/'+code+'.png'
        await bot.send_photo(message.chat.id,photo,caption=caption,reply_markup=btn1)
        
        
