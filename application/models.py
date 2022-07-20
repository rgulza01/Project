import datetime
from datetime import datetime
from application import db

#---------------------------------------------------Models---------------------------------------------------
user_post = db.Table('user_post',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(95), nullable=False)
    email = db.Column(db.String(180), unique=True , nullable=False)
    posts = db.relationship('Post', secondary=user_post, backref='user')
    

    def __repr__(self):
        return f"User: {self.name}, {self.email}"

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(190), nullable=False)
    title = db.Column(db.String(300))
    content = db.Column(db.Text(700))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(200))
    
    def __repr__(self):
        return f"Title: {self.title}"
        
#---------------------------------------------------Forms-----------------------------------------


# class UserForm(FlaskForm):
#     name_box = StringField("Enter your full name (this will also be the name you use to post very gluten free stories): ", validators=[DataRequired(), Length(min=3, max=80)])
#     email_box= StringField("Email address here: ", validators=[DataRequired(), Email()])
#     submit_button = SubmitField("Submit")

# class UserFormUpdate(FlaskForm):
#     name_box = StringField("Enter the new name: ", validators=[DataRequired(), Length(min=3, max=80)])
#     email_box= StringField("Enter the new email address: ", validators=[DataRequired(), Email()])
#     submit_button = SubmitField("Submit")

# class PostForm(FlaskForm):
#     title_box = StringField("Enter the title of the post: ", validators=[DataRequired(), Length(min=3, max=300)])
#     content_box = StringField("Enter your post here: ", validators=[DataRequired()], widget=TextArea())
#     author_box = StringField("Enter your name as inserted for signing up: ", validators=[DataRequired(), Length(min=3, max=190)])
#     slug_box = StringField("Slug: ", validators=[DataRequired()])
#     submit_button = SubmitField("Submit")


