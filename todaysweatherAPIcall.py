import requests

url="https://www.metaweather.com/api/location/2295420/2021/1/13/"

request=requests.get(url)

json=request.json()

for i in json:
     print(i)

while 1:
     i=0
