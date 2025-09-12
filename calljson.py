import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

print('Number of people in space: ' + str(json['number']))

for person in json['people']:
    print(person['name'] + ' is on IN GODDAMN SPACE on the ' + person['craft'])