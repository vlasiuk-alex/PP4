from app import *
from models import *

from flask_testing import TestCase
import unittest
import json
import base64
from sqlalchemy.orm import close_all_sessions


user = {
    "username" : "user1",
    "firstname" : "us",
    "lastname" : "usa",
    "email" : "a@gmail.com",
    "password" : "user1",
    "ustatus" : "user" 
}
usered = {
    "username" : "user2",
    "firstname" : "usa",
    "lastname" : "usaa",
    "email" : "aa@gmail.com",
    "password" : "user2",
    "ustatus" : "user" 
}
article = {
    "title" : "b",
    "text" : "b" ,
    "date" : "11/11/11",
    "status" : "admitted"
}




class TestingUser(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        close_all_sessions()
        Base.metadata.create_all(engine)

    def tearDown(self):
        close_all_sessions()
        Base.metadata.drop_all(engine)

    def test_create_users(self):
        client = app.test_client()
        user_data = json.dumps(user).encode('utf-8')

        response = client.post('/api/articles/users', json={'username': user["username"],'firstname': user["firstname"],'lastname': user["lastname"],'email': user["email"],'password': user["password"],'ustatus': user["ustatus"]})
        self.assertEqual(response.status_code,200)

    def test_create_article(self):
         client = app.test_client()
         article_data = json.dumps(article).encode('utf-8')
        
         response = client.post('/api/articles/article', json={'title': article["title"],'text': article["text"],'date': article["date"],'status': article["status"]})
         self.assertEqual(response.status_code,200)

    def test_update_users(self):
        client = app.test_client()
        user_data = json.dumps(user).encode('utf-8')
        response = client.post('/api/articles/users', json={'username': user["username"],'firstname': user["firstname"],'lastname': user["lastname"],'email': user["email"],'password': user["password"],'ustatus': user["ustatus"]})
        user_data = json.dumps(usered).encode('utf-8')
        responses = client.put('/api/articles/users/1', json={'username': usered["username"],'firstname': usered["firstname"],'lastname': usered["lastname"],'email': usered["email"],'password': usered["password"],'ustatus': usered["ustatus"]})
        self.assertEqual(responses.status_code,200)






if __name__ == '__main__':
    unittest.main()