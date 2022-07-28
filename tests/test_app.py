from flask import render_template, url_for
from flask_testing import TestCase
from application import app, db
from application import *
from application.models import *
from application.forms import *


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            # SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://radiagulzan@db-relationship-practice-mysql:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('SERVER_NAME')}:3306/test_db",
            SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3',
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=False,
            WTF_CSRF_ENABLED=False
            )

        @app.errorhandler(404)
        def pageNotFound(error_parameter):
            return render_template('404.html'), 404
        
        @app.errorhandler(500)
        def serverError(error_parameter):
            return render_template('500.html'), 500
        
        return app
    

    def setUp(self):
        db.drop_all()

        # Create table schema
        db.create_all()
        
        global test_user1, test_user2
        test_user1 = User(name = "Test User", email = "testuser@live.it")
        test_user2 = User(name = "Alif", email = "alif@live.it")
        
        db.session.add(test_user1)
        db.session.add(test_user2)
        db.session.commit()

        global test_post1, test_post2, test_post3, test_post4
        test_post1 = Post(author=test_user1.name, title="An utterly testy post", content="Testy stories and more", slug="testpost1")
        test_post2 = Post(author=test_user2.name, title="Alif's GF sister", content="Cooking for a GF sister experience", slug="testpost2")
        test_post3 = Post(author=test_user2.name, title="Alif's heavenly vegan cake", content="Vegan cake made of cloud", slug="testpost3")
        test_post4 = Post(author=test_user1.name, title="A sugarless post", content="For testing", slug="testpost4")

        db.session.add(test_post1)
        db.session.add(test_post2)
        db.session.add(test_post3)
        db.session.add(test_post4)
        db.session.commit()

        test_user1.posts.append(test_post1)
        test_user2.posts.append(test_post2)
        test_user2.posts.append(test_post3)
        test_user1.posts.append(test_post4)
        db.session.commit()

        #--------------------------------teardown not besing used for now, to check the database----------------------------
    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()

class TestModels(TestBase):
    def test_User_model(self):
        
        assert f"{test_user1.__repr__()}" == "User: Test User, testuser@live.it"   
        assert f"{test_user2.__repr__()}" == "User: Alif, alif@live.it"  
        
        self.assertEqual(User.query.count(), 2)

    def test_Post_model(self):
        assert f"{test_post1.__repr__()}" == "Title: An utterly testy post"
        assert len(Post.query.all()) == 4
    
    def test_user_post_model(self):
        assert test_user2.posts[0].title == "Alif's GF sister"
        assert len(test_user2.posts) == 2

class TestRoutes(TestBase):
    def test_addnewpost(self):
        response = self.client.get(url_for('addnewpost')) 
        self.assertEqual(response.status_code, 200) 
        self.assertIn(b'Post any GF recipees, tips about the lifestyle or your GF stories!', response.data)

    def test_home(self):
        response = self.client.get(url_for('index')) 
        self.assertEqual(response.status_code, 200) 
        self.assertIn(b'GF FLASK', response.data)

    def test_register(self):
        response = self.client.get(url_for('register')) 
        self.assertEqual(response.status_code, 200)  
        self.assertIn(b'Welcome to our Gluten Free Flask website!', response.data)
    
    def test_dashboard(self):
            response = self.client.get(url_for('dashboard'))
            self.assertEqual(response.status_code, 200)
    
    # def test_posts(self):
    #     response = self.client.get(url_for('register')) 
    #     self.assertEqual(response.status_code, 200) 
    #     self.assertIn(b"Our gluten free community's blog posts", response.data)
    
    # def test_apost(self):
    #         response = self.client.get(url_for('apost'))
    #         self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

#--------------------------------CRUD---------------------------

class TestCRUD(TestBase):
    def test_update_user(self):
        previous_user1_name = test_user1.name
        new_user1_name = "Little Cupcake"
        test_user1.name = new_user1_name
        list_posts = Post.query.all()
        for p in list_posts:
            if p.author == previous_user1_name:
                p.author = new_user1_name
        db.session.commit()
        self.assertEqual(test_user1.posts[1].title, "A sugarless post")
        self.assertEqual(test_user1.name, test_post1.author)
        assert len(test_user1.posts) == 2

    def test_delete_user(self):
        all_users = User.query.count()
        userToDelete = test_user1

        userToDelete_name = userToDelete.name
        #checks if the user had any posts, if it does, it deletes the posts before deleting the user
        filtered_posts_by_user = Post.query.filter_by(author = userToDelete_name).all()
        if len(filtered_posts_by_user) >= 1:
            for p in filtered_posts_by_user:
                db.session.delete(p)
        
        db.session.delete(userToDelete)
        db.session.commit()

        posts_filter = len(Post.query.filter_by(author = userToDelete_name).all())
        self.assertEqual(User.query.count(), all_users-1)
        self.assertEqual(posts_filter, 0)

    

