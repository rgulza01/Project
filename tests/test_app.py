from unittest import TestCase
from flask import url_for
import app
from application import *
from application.models import User


class TestBase(TestCase):
    def create_app(self):
        app.config.update( SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3',
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True)
        return app

    def test_user_model(self):
        db.create_all()
        user = User(name = "Bismillah", email = "bismillah@live.it")
        assert user.email == "bismillah@live.it"
        #we are making this as a string in itself
        assert f"{user.__repr__()}" == 'User: Bismillah, bismillah@live.it'

    def test_user_form_get(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200) # 200 default
        self.assertIn(b'Welcome to our Gluten Free Flask website!', response.data) 

    def test_user_form_post(self):
        response = self.client.post(
            url_for('register'),
            data = dict(name_box="Bismillah", email_box="bismillah@live.it"),
            follow_redirects=True   
        )
        self.assertIn(b'something', response.data) # assert that the website's title is present in the HTTP response's data

# client.post and send it to the url


# So do post and get 

# response = self.client.get(
#     url_for('register'),
#     data = dict(name_box="Barkus Aurelius", ....)
#     follow_redirects=True
# )
# self.assertIn(b'Welcome to my website', response.data) # assert that the website's title is present in the HTTP response's data
# assertIN




  