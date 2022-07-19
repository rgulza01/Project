from flask_testing import TestCase
from flask import url_for
import app
from application import *
from application.models import *


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://radiagulzan@db-relationship-practice-mysql:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('SERVER_NAME')}:3306/test_db",
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True,
        WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        # Create table schema
        db.create_all()
        # Create test objects
        test_user = User(name = "Test User", email = "testuser@live.it")
        test_post = Post(title="A testy vegan post", content="Testy stories and more", author="Test User", slug="test post", user=test_user)
        # save sample data to database
        db.session.add_all([test_user, test_post])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestModels(TestCase):
    def test_User_model(self):
        db.create_all()
        user1 = User(name = "Bismillah", email = "bismillah@live.it")
        assert user1.email == "bismillah@live.it"
        assert f"{user1.__repr__()}" == 'User: Bismillah, bismillah@live.it'   
        assert self.assertEqual(User.query.count(), 2)

class TestRoutes(TestCase):
    pass



