import requests
import json

response = requests.get('https://coqh2vx627.execute-api.us-east-1.amazonaws.com/try1/counter')

#retrieving json and creating a index for items -> crating a list
questions_list = response.json()['body']
print(questions_list)