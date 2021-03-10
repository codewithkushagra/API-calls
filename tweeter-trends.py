import requests

url="https://twitter-trends-daily.herokuapp.com/alltrends"

request=requests.get(url)

#print(request)

json_data=request.json()

print(json_data)

print(json_data['date'])

#print(json_data['trends']['london'])

# for i in json_data['trends']['india']:
#     print(i)

dict_data=dict(json_data)
#dict_data=json_data
#print(dict_data['trends'].keys())

for i in dict_data['trends'].keys():
    print(f'Country: {i}\n')
    
    if type(dict_data['trends'][i]) is not str:
        for j in json_data['trends'][i]:
            print(j)
        # print(dict_data['trends'][i])
    else:
        print(dict_data['trends'][i])
    print("")
    print("")