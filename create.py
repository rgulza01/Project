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
db.session.commit()

#----------------------------------testing many to many----------------------------------

previous_user3_name = user3.name 

print("-------------------------------------")
print(f"{user3.name}'s followed posts:")
for p in user3.posts:
    print(p)
    
new_user3_name = "Little Cupcake"
user3.name = new_user3_name
# list_posts = Post.query.all()
# for p in list_posts:
#     if p.author == previous_user3_name:
#         p.author = new_user3_name

db.session.commit()

# print("-----------------------------------")
# print(f"{user3.name}'s followed posts:")
# for p in user3.posts:
#     print(p)

# print(user3.name)
print(post3.author)

# print(len(user3.posts) == 2)
# print(User.query.filter_by(name="Bismillah").all())

# print("-----------------------------------")
# print(user3.posts[0])
# print(post3.author == new_user3_name)

# print(user3.posts[1].title == "Maple syrup stories")

# posts_filter = Post.query.filter_by(author = "Bismillah").all()
# print(posts_filter)

# AttributeError: type object 'User' has no attribute 'user1'
# user1_data = User.query.filter_by(id=1).first()
# print(type(user1_data.name))