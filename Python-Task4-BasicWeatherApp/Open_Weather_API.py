import requests

city_name= 'Sheoganj'
API_Key= '318eb0e834907d586b0fc1d25309a4e4'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'


response= requests.get(url)
if response.status_code==200:
    data= response.json()
    print('Weather is', data['weather'][0]['description'])
    print('Current Temperature is', data['main']['temp'])
    print('Current Temperature Feels like is', data['main']['feels_like'])
    print('Humidity is', data['main']['humidity'])
