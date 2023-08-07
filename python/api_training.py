import requests
import json

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