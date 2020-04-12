import json

from Posts.models import Post
from Users.models import User
from database import db


def insert_dummy_data():
    # users data
    with open('Users/users.json') as file:
        data = json.load(file)
    file.close()
    for user_item in data:
        user = User(username=user_item['username'])
        user.email = user_item['email']
        user.hash_password(user_item['password'])
        db.session.add(user)
        db.session.commit()
    # posts data
    with open('Posts/posts.json') as file:
        data = json.load(file)
        for post_item in data:
            post = Post()
            post.id = post_item['id']
            post.body = post_item['body']
            post.user_id = post_item['userId']
            post.title = post_item['title']
            db.session.add(post)
            db.session.commit()
