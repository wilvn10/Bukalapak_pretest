import urllib.request, json 
import requests as rs

class getJson:
     def __init__(self, url):
          self.url = url
          with urllib.request.urlopen(url) as response:
               self.source = response.read()
               self.data = json.loads(self.source)
     def get(self):
          for i in range(len(self.data)):
               userId =isinstance(self.data[i]["userId"], int)
               ident =isinstance(self.data[i]["id"], int)
               title =isinstance(self.data[i]["title"], str)
               body =isinstance(self.data[i]["body"], str)     
               print('list {}: \n userId = {}\n id = {}\n title = {}\n body = {}'.\
                    format(1+i, userId, ident, title, body))
          if userId and ident and title and body:
               print('All datas are correct')
          else:
               print('some of the datas are not correct ') 
     def post(self, data_input):

          self.data_input = data_input
          response = rs.post(self.url, self.data_input) 
          print(response.status_code) 
          print(response.text) 

data_input = {\
          'title':'recommendation', \
          'body':'motorcycle',\
           'userId':12\
          }

if __name__ == '__main__':
     json = getJson("https://jsonplaceholder.typicode.com/posts")
     #run code below for question number 1A
     json.get()

     # run code below for question number 1B
     # json.post(data_input)

