import schedule
import time
import yagmail
import requests

lat=-12.82
lon=28.21
yag=yagmail.SMTP('blessingsmapalo541@gmail.com' ,'bizf glvc gddu unft')

def temp_weather() : 
    url=f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
    response=requests.get(url)
    data=response.json()
    temperature=(data['current_weather']['temperature'])
    print(f'The current temperature for Kitwe is : {temperature}°C')

    if temperature > 30 :
        
        yag.send('mchanda509@gmail.com' , 'WARNING!' , 'High temperature in Kitwe')
    elif temperature < 15 : 
        
         yag.send('mchanda509@gmail.com' , 'WARNING!' , 'Cold weather in Kitwe')
    else : 
        print(f'The temperature in Kitwe is normal at : {temperature}°C')

schedule.every(30).seconds.do(temp_weather)
while True : 
     schedule.run_pending()
     time.sleep(1)