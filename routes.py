from Posts.routes import init_posts_routes
from Users.routes import init_user_routes
def init_routes(app):
    init_user_routes(app)
    init_posts_routes(app)
