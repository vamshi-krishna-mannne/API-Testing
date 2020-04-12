from flask import jsonify, request

from Posts.models import Post
from Users.models import User
from database import db
from auth import auth
@auth.login_required
def getPosts():
    posts = Post.query.all()
    return jsonify(
        [{'id': p.id, 'username': p.author.username, 'body': p.body, 'timestamp': p.timestamp} for p in posts]), 200

@auth.login_required
def createPost(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify("no user exists with id {}".format(id)), 400
    else:
        input = request.json
        post = Post(body=input['body'], author=user, title=input['title'])
        db.session.add(post)
        db.session.commit()
    return jsonify('Created Post for username {}'.format(post.author.username)), 201

@auth.login_required
def updatePost(id):
    rows_changed = Post.query.filter_by(id=id).update(request.json)
    db.session.commit()
    return jsonify('updated post with ID {}'.format(id)), 200

@auth.login_required
def deletePost(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    return jsonify('deleted post for username {}'.format(post.author.username)), 200

@auth.login_required
def get_user_posts(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(user_id=user.id).all()
    return jsonify(
        [{"body": post.body, "id": post.id, "timestamp": post.timestamp, "user_id": post.user_id,"title":post.title} for post in posts])
