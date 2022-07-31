from lib2to3.pytree import Base
from flask import session
from sqlalchemy import ForeignKey
from application import db
from application.models import *
from application.forms import *

#----------------------------------File used for testing the dataabse----------------------------------

db.drop_all()
db.create_all()

user1 =User(name = "Bismillah", email = "bismillah@live.it")
user2 =User(name = "Bambi", email = "bambi@outlook.com")
user3 =User(name = "Lily", email = "lily@outlook.com")


post1=Post(author=user1.name, title="An utterly vegan post", content="Vegan stories and more", slug="post1")
post2=Post(author=user1.name, title="An untimate sugar free post", content="Sugar free stories and more", slug="post2")
post3=Post(author=user3.name, title="Maple syrup stories", content="Many words and many more", slug="post3")

user1.posts.append(post1)
user1.posts.append(post2)
user3.posts.append(post2)
user3.posts.append(post3)


db.session.add_all([user1, user2, user3, post1, post2, post3])
# db.session.add_all([user1, user2, user3, post1, post3])

db.session.commit()

#----------------------------------testing many to many----------------------------------

previous_user3_name = user3.name 

print("-------------------------------------")
print(f"{user3.name}'s followed posts:")
for p in user3.posts:
    print(p)



#-----------------------------Learning how to merge--------------------------
#because of:
new_user3_name = "Little Cupcake"
user3.name = new_user3_name
# list_posts = Post.query.all()
# for p in list_posts:
#     if p.author == previous_user3_name:
#         p.author = new_user3_name

db.session.commit()
print(f"Should be {user3.name} But it's: ")
print(post3.author)

# db.drop_all()
# db.create_all()

# class User(db.Model):
#     __tablename__ = 'user'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     addresses = db.relationship("Address", backref="user")

# class Address(db.Model):
#     __tablename__ = 'address'

#     id = db.Column(db.Integer, primary_key=True)
#     email_address = db.Column(db.String(50), nullable=False)
#     user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

# u1 = User(name='ed', addresses=[Address(email_address='ed@ed.com')])
# db.session.add(u1) 
# db.session.commit()

# existing_a1 = u1.addresses[0] 
# a1 = Address(id=existing_a1.id) 
# a1.user = u1
# a1 = db.session.merge(a1) #error
# session.commit()
# #----------------------------------merged_object = session.merge(existing_object)---------------------
# # https://docs.sqlalchemy.org/en/14/orm/session_state_management.html#merging
# from sqlalchemy.orm import Session
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Column, Integer, String, event

# def strong_reference_session(session):
#     @event.listens_for(session, "pending_to_persistent")
#     @event.listens_for(session, "deleted_to_persistent")
#     @event.listens_for(session, "detached_to_persistent")
#     @event.listens_for(session, "loaded_as_persistent")
#     def strong_ref_object(sess, instance):
#         if 'refs' not in sess.info:
#             sess.info['refs'] = refs = set()
#         else:
#             refs = sess.info['refs']

#         refs.add(instance)


#     @event.listens_for(session, "persistent_to_detached")
#     @event.listens_for(session, "persistent_to_deleted")
#     @event.listens_for(session, "persistent_to_transient")
#     def deref_object(sess, instance):
#         sess.info['refs'].discard(instance)

# my_session = Session()
# strong_reference_session(my_session)
# maker = sessionmaker()
# strong_reference_session(maker)

# class User(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     addresses = db.relationship("Address", backref="user")

# class Address(Base):
#     __tablename__ = 'address'

#     id = Column(Integer, primary_key=True)
#     email_address = Column(String(50), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

# u1 = User(name='ed', addresses=[Address(email_address='ed@ed.com')])
# db.session.add(u1)
# db.session.commit() #error sqlalchemy.orm.exc.UnmappedInstanceError: Class '__main__.User' is not mapped



    