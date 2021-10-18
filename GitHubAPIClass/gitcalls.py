import requests


class GitHubAPI():
     
     def __init__(self,respository,username,token):
          self.respository=respository
          self.username=username
          self._rootURL="https://api.github.com"
          self.params = {"state": "open"}
          self.header={'Authorization':f'token {token}'}

     def getRespositryData(self):
          url=f'{self._rootURL}/repos/{self.username}/{self.respository}'
          try:
               return requests.get(url,headers=self.header,params=self.params).json()
          except:
               return 'Check you internet connection'
     def getContent(self,data):
          url=f'{self._rootURL}/repos/{self.username}/{self.respository}/contents'
          for path in data:
               url=url+'/'+path
          try:
               data=requests.get(url,headers=self.header,params=self.params).json()
               if type(data) is dict:
                    if 'message' in data.keys():
                         return 'Limit of call exceeded'
                    else:
                         return data
               else:
                    return data
          except:
               return 'Check you internet connection'
       
