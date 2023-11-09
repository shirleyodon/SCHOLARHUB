from flask import Flask
from .config import Config


# Create flask app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .views import login_route, register_route, home_route, result_route, print_route, logout_route

    app.register_blueprint(login_route)
    app.register_blueprint(register_route)
    app.register_blueprint(home_route)
    app.register_blueprint(result_route)
    app.register_blueprint(print_route)
    app.register_blueprint(logout_route)
    return app
