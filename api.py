def flag(text):
    import requests
    import json
    from googletrans import Translator
    tarjimon=Translator()
    name=tarjimon.translate(text,dest='en')
    url='https://restcountries.eu/rest/v2/name/'+name.text
    response=requests.get(url)
    rest=json.loads(response.text)
    return rest[0]['flag']
def countryinfo(text):
    import requests
    import json
    from googletrans import Translator
    tarjimon=Translator()
    name=tarjimon.translate(text,dest='en')
    url='https://restcountries.eu/rest/v2/name/'+name.text
    response=requests.get(url)
    rest=json.loads(response.text)

    if response.status_code==404:
         return 'Xatolik'
    else:
     davlatnomi=tarjimon.translate(rest[0]['name'],dest='uz')
     poytaxt= tarjimon.translate(rest[0]['capital'],dest='uz')
     aholi=rest[0]['population']
     maydoni=rest[0]['area']
     millat=rest[0]['languages'][0]['nativeName']
     valyutanomi=rest[0]['currencies'][0]['name']
     valyutakodi=rest[0]['currencies'][0]['code']
     for i in rest[0]['topLevelDomain']:
                 i=' '+i+'\n'
     domain=i
     for k in rest[0]['callingCodes']:
                     k='+'+k+'\n'
     telefonkod=k   
     hudud=tarjimon.translate(rest[0]['region'],dest='uz').text+'da joylashgan!'

     result="Mamlakat nomi:"+davlatnomi.text+"\n"+'Poytaxti:'+poytaxt.text+"\n"+'Aholi soni:'+str(aholi)+' ta'+"\n"+"Maydoni:"+str(maydoni)+' kv km'+"\n"+'Millat nomi:'+millat+"\n"+"Til:"+millat+' tili'+"\n"+'Valyuta nomi:'+valyutanomi+'\n'+"Valyuta kodi:"+valyutakodi+"\n"+'Domen:'+domain+"\n"+'Telefon raqam kodi:'+telefonkod+"\n"+hudud
     return result


def link(text):
    import requests
    import json
    from googletrans import Translator
    tarjimon=Translator()
    name=tarjimon.translate(text,dest='en')
    url='https://restcountries.eu/rest/v2/name/'+name.text
    return url
def wikipedia(text):
    urlmanzil='https://uz.wikipedia.org/wiki/'+text