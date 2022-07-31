import datetime
from datetime import datetime

from sqlalchemy import ForeignKey
from application import db

#Models updated from one to many to many to many 

user_post = db.Table('user_post', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
    )

class User(db.Model): 
    tablename = 'user' 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(95), nullable=False) 
    email = db.Column(db.String(180), unique=True , nullable=False) 
    posts = db.relationship("Post", secondary=user_post, backref=db.backref('user_post', lazy='dynamic'),lazy='dynamic')

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column('author', db.String(95), db.ForeignKey('user.name'))
    title = db.Column(db.String(300))
    content = db.Column(db.Text(700))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(200))

    def __repr__(self):
        return f"Title: {self.title}"