from app import *
from models import *

from flask_testing import TestCase
import unittest
import requests
import json
import base64

from sqlalchemy.orm import close_all_sessions

class TestingUsers(TestCase):

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
        with app.test_client() as cl:
            user_data = {
                "username" : "user1",
                "firstname" : "us",
                "lastname" : "usa",
                "email" : "a@gmail.com",
                "password" : "user1",
                "ustatus" : "user" 
            }
            json_data= json.dumps(user_data).encode('utf-8')
            
            r2 = cl.open(path='/articles/users', method='POST', data = json_data,headers={'Content-Type': 'application/json'})
            self.assertEqual(r2.status_code, 500)

    def test_delete_users(self):
        with app.test_client() as cl:
            user_data = {
               "username" : "user1",
               "firstname" : "us",
               "lastname" : "usa",
               "email" : "a@gmail.com",
               "password" : "user1",
               "ustatus" : "user" 
            }
            user_data2 = {
               "username" : "user2",
               "firstname" : "usq",
               "lastname" : "usaq",
               "email" : "aq@gmail.com",
               "password" : "user2",
               "ustatus" : "user" 
            }
            json_data1 = json.dumps(user_data).encode('utf-8')
            json_data2 = json.dumps(user_data2).encode('utf-8')
            rr = cl.open(path='/articles/users', method='POST', data = json_data1,headers={'Content-Type': 'application/json'})
            rr = cl.open(path='/articles/users', method='POST', data=json_data2,headers={'Content-Type': 'application/json'})

            r2 = cl.open(path='/articles/users/1', method='DELETE', headers={'Authorization': 'Basic ' + base64.b64encode('aq@gmail.com:user2'.encode()).decode()})
            r1 = cl.open(path='/articles/users/3', method='DELETE',headers={'Authorization': 'Basic ' + base64.b64encode('a@gmail.com:user1'.encode()).decode()})

            r3 = cl.open(path='/articles/users/1', method='DELETE', headers={'Authorization': 'Basic ' + base64.b64encode('a@gmail.com:user1'.encode()).decode()})

            #self.assertEqual(r2.status_code, 403)
            #self.assertEqual(r1.status_code, 404)
            #self.assertEqual(r3.status_code, 200)

class TestingArticles(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        close_all_sessions()
        Base.metadata.create_all(engine)
        cl = app.test_client()
        user_data1 = {
            "username" : "user1",
            "firstname" : "us",
            "lastname" : "usa",
            "email" : "a@gmail.com",
            "password" : "user1",
            "ustatus" : "user" 
            }
        user_data2 = {
            "username" : "user2",
            "firstname" : "usq",
            "lastname" : "usaq",
            "email" : "aq@gmail.com",
            "password" : "user2",
            "ustatus" : "user" }
        json_data1 = json.dumps(user_data1).encode('utf-8')
        json_data2 = json.dumps(user_data2).encode('utf-8')
        rr = cl.open(path='/articles/users', method='POST', data=json_data1, headers={'Content-Type': 'application/json'})
        rr = cl.open(path='/articles/users', method='POST', data=json_data2, headers={'Content-Type': 'application/json'})

    def tearDown(self):
        close_all_sessions()
        Base.metadata.drop_all(engine)

    def test_create_articles(self):
        with app.test_client() as cl:
            article_data1 = {
                "title" : "a",
                "text" : "a" ,
                "date" : "10/10/10",
                "status" : "admitted"
            }
            article_data2 = {
                "title" : "b",
                "text" : "b" ,
                "date" : "11/11/11",
                "status" : "admitted" 
            }
            json_data1 = json.dumps(article_data1).encode('utf-8')
            json_data2 = json.dumps(article_data2).encode('utf-8')
            r1 = cl.open(path = '/articles/article', method = 'POST', data = json_data1 ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('aq@gmail.com:user2'.encode()).decode()})
            #self.assertEqual(r1.status_code, 200)




    def test_get_article(self):
        with app.test_client() as cl:
            article_data1 = {
                "title" : "a",
                "text" : "a" ,
                "date" : "10/10/10",
                "status" : "admitted"
            }
            article_data3 = {
                "title" : "c",
                "text" : "c" ,
                "date" : "11/11/11",
                "status" : "admitted" 
            }

            json_data1 = json.dumps(article_data1).encode('utf-8')
            json_data3 = json.dumps(article_data3).encode('utf-8')

            r = cl.open(path = '/articles/article', method = 'POST', data = json_data1 ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('a@gmail.com:user1'.encode()).decode()})
            r01 = cl.open(path = '/articles/article', method = 'POST', data = json_data3 ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('aq@gmail.com:user2'.encode()).decode()})

            r1 = cl.open(path = '/articles/article/5', method = 'GET', headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('a@gmail.com:user1'.encode()).decode()})
            r2 = cl.open(path = '/articles/article/1', method = 'GET', headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('aq@gmail.com:user2'.encode()).decode()})


            #self.assertEqual(r1.status_code, 404)
            #self.assertEqual(r2.status_code, 200)

    def test_delete_article(self):
        with app.test_client() as cl:
            article_data1 = {
                "title" : "a",
                "text" : "a" ,
                "date" : "10/10/10",
                "status" : "admitted"
            }
            article_data2 = {
                "title" : "b",
                "text" : "b" ,
                "date" : "11/11/11",
                "status" : "admitted" 
            }
            json_data1 = json.dumps(article_data1).encode('utf-8')
            json_data2 = json.dumps(article_data2).encode('utf-8')

            r = cl.open(path = '/articles/article', method = 'POST', data = json_data1 ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('a@gmail.com:user1'.encode()).decode()})
            r0 = cl.open(path = '/articles/article', method = 'POST', data = json_data2 ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('a@gmail.com:user1'.encode()).decode()})


            r1 = cl.open(path = '/articles/article/1', method = 'DELETE', headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('a@gmail.com:user1'.encode()).decode()})
            r3 = cl.open(path = '/articles/article/2', method = 'DELETE', headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('aq@gmail.com:user2'.encode()).decode()})
            r4 = cl.open(path = '/articles/article/99', method = 'DELETE', headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('aq@gmail.com:user2'.encode()).decode()})

            
            #self.assertEqual(r1.status_code, 200)
            #self.assertEqual(r3.status_code, 403)
            #self.assertEqual(r4.status_code, 404)



    def test_update_article(self):
        with app.test_client() as cl:
            article_data1 = {
                "title" : "a",
                "text" : "a" ,
                "date" : "10/10/10",
                "status" : "admitted"
            }
            json_data1 = json.dumps(article_data1).encode('utf-8')
            r = cl.open(path = '/articles/article', method = 'POST', data = json_data1 ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('first@gmail.com:1111'.encode()).decode()})
            new_article_data1 = {
                "title" : "ab",
                "text" : "ab" ,
                "date" : "17/10/10",
                "status" : "waiting for admitting"
            }
            
            json_data = json.dumps(new_article_data1).encode('utf-8')
            r1 = cl.open(path = '/articles/article/1', method = 'PUT', data = json_data ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('second@gmail.com:2222'.encode()).decode()})
            r2 = cl.open(path = '/articles/article/22', method = 'PUT', data = json_data ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('first@gmail.com:1111'.encode()).decode()})
            r3 = cl.open(path = '/articles/article/1', method = 'PUT', data = json_data ,headers={'Content-Type': 'application/json', 'Authorization': 'Basic ' + base64.b64encode('first@gmail.com:1111'.encode()).decode()})

            #self.assertEqual(r1.status_code, 403)
            #self.assertEqual(r2.status_code, 400)
            self.assertEqual(r3.status_code, 500)

if __name__ == "__main__":
    unittest.main()