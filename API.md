REST API- Application programing interface.

- how 2 sofwtwares communicate with each other

- client consumes info from server -> one way relationship

JSON is language of communication and API what things what we can communicate (eg, retrieve a list of users)

REST - mean of comunication (eg, face to face, text, etc) -> in this case by the web 

client ->  API endpoit -> backend -> API endpoint -> Database
Why not connect directly client to Database? 
    1- Security
    2- Versitility -> we can use the same API and backend for diferent apps
    3- Modularity -> we can make changes without breaking everything
    4- interoperability 

API Methods:
GET- when client is retriving something from server
DELETE- Delete
PATCH- replace diferent pieces 
PUT- writte - update data - replace resource
POST- writte (new) data - add resource
we might use POST /adress and PUT /adress/id

example
import requests
import json

#retrieving a collection of questions on stackoverflow to filter some data
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#retrieving json and creating a index for items -> crating a list
questions_list = response.json()['items']

#iterate over the list -> retrieving only the titles of each question
for question in questions_list:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
       
    else:
        print("no unawser questions")
    print()