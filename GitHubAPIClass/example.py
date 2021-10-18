from gitcalls import GitHubAPI
import base64
import json
from clear import Clear



token='YOUR_TOKEN'

techhub=GitHubAPI('Hackbook','techhub-community',token)

dataFolder= techhub.getContent(['data'])


if type(dataFolder) is not str:
     
     Names=[]
     count=1
     for data in dataFolder:
          dots='.'*count
          print('loading'+dots)  
          requestData=techhub.getContent(['data',data['name'],f"{data['name']}.md"])
          if type(requestData) is not str:
               jsonData=json.loads('{'+base64.b64decode(requestData['content']).decode('utf-8')+'}')
               Names.append(jsonData['name'])
          else:
               print(requestData)
               break
          Clear.clear()
          if count>3:
               count=1
          else:
               count+=1

     for name in Names:
          print(name)
     hold=input()
else:
     print(dataFolder)