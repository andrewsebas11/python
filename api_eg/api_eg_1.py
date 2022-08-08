import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=3b38f7256941d04dc249f965f535ca29&q='
city = input('City Name :')
url = api_address + city
print(url)
json_data = requests.get(url).json()
print(json_data)
format_add = json_data['weather'][0]['main']
format_add1 = json_data['weather'][0]['description']
format_add2 = json_data['coord']['lon']
format_add3 = json_data['coord']['lat']
format_add4 = json_data['wind']['speed']
print(format_add,"and ",format_add1,"and ",format_add2,"and ",format_add3,"and ",format_add4)
