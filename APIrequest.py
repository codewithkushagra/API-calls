import requests

url="https://www.metaweather.com/api/location/search/?query=bangalore"

response=requests.get(url)

json=response.json()

for i in json:     
     print(i)

while True:
     i=0
