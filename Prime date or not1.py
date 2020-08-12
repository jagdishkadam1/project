from datetime import date
import requests
today = date.today()
print(today)
d1 = int(input('enter date in number:'))
if d1 > 1:
    for i in range(2, d1): 
        if (d1 % i) == 0: 
           print(d1, "Date is not prime so no date") 
           break
        else: 
           print(d1, "Date is prime")
           api_address = 'https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=439d4b804bc8187953eb36d2a8c26a02'
           city = input('City Name::')
           url = api_address + city
           json_data = requests.get(url).json()
           formated = json_data['main']
           print(formated)
else:
	print(d1,'Date is not prime so no date')

