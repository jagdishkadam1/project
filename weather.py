import requests

api_address = 'https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=439d4b804bc8187953eb36d2a8c26a02'
city = input('City Name::')
url = api_address + city
json_data = requests.get(url).json()
formated = json_data['main']
print(formated)
