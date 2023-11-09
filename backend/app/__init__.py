from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


# Create Sqlalchemy instance
db = SQLAlchemy()


def create_app():
    # Create flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .views import route_categorie, route_titre, route_encadreur, route_parcours, \
        route_etudiant, route_niveau, route_annee, route_etablissement, route_inscription, \
        route_livre, route_redaction

    # Register blueprints
    app.register_blueprint(route_categorie)
    app.register_blueprint(route_titre)
    app.register_blueprint(route_encadreur)
    app.register_blueprint(route_parcours)
    app.register_blueprint(route_etudiant)
    app.register_blueprint(route_niveau)
    app.register_blueprint(route_annee)
    app.register_blueprint(route_etablissement)
    app.register_blueprint(route_inscription)
    app.register_blueprint(route_livre)
    app.register_blueprint(route_redaction)

    return app
