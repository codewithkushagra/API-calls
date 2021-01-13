import requests

url="https://www.metaweather.com/api/location/search/?query=san"

response=requests.get(url)

json=response.json()

for i in json:
     print(i)
