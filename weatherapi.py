import requests

url = 'http://api.weatherapi.com/v1/current.json?key=402e7bc7b99844d9a84155245250909&q=TA66TT&aqi=no'
response = requests.get(url)
weather_json = response.json()
temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print(description)
print(weather_json)
print(temp)