from . import views


def init_routes(app):
    if app:
        app.add_url_rule('/api/dummyUsers','create_dummy_users',views.create_dummy_users,methods=['GET'])
        app.add_url_rule('/api/create', 'new_user', views.new_user, methods=['POST'])
        app.add_url_rule('/api/users/<int:id>', 'get_user', views.get_user, methods=['GET'])
        app.add_url_rule('/api/users','get_all_users',views.get_all_users, methods=['GET'])