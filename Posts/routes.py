from . import views


def init_posts_routes(app):
    if app:
        app.add_url_rule('/api/posts', 'getPosts', views.getPosts, methods=['GET'])
        app.add_url_rule('/api/posts/<string:username>', 'get_user_posts', views.get_user_posts, methods=['GET'])
        app.add_url_rule('/api/posts/create/<int:id>', 'createPost', views.createPost, methods=['POST'])
        app.add_url_rule('/api/posts/update/<int:id>', 'updatePost', views.updatePost, methods=['PUT'])
        app.add_url_rule('/api/posts/delete/<int:id>', 'deletePost', views.deletePost, methods=['DELETE'])