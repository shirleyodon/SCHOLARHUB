from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import livre_to_dict_2, get_all_livre, get_livre, create_livre, update_livre, search_livre_by_theme_categorie_parcours_niveau

route_livre = Blueprint('route_livre', __name__)


@route_livre.route("/sh/livre/", methods=["GET", "POST"])
def create_or_get_all_livres():
    if request.method == "GET":
        try:
            livres = get_all_livre()
            return jsonify([livre_to_dict_2(livre) for livre in livres]), 200

        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500

    else:
        try:
            data = request.get_json()
            if data:
                db.session.add(create_livre(data))
                db.session.commit()
                return jsonify({'Message': 'Nouveau Livre créé avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400

        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500


@route_livre.route("/sh/livre/<int:refLivre>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_livre(refLivre):
    try:
        livre = get_livre(refLivre)

        # Si le livre n'existe pas
        if not livre:
            return jsonify({'Erreur': "Aucun Livre n'a été trouvé"}), 404
        else:
            if request.method == "GET":
                return jsonify(livre_to_dict_2(livre)), 200

            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_livre(livre, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour Livre avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(livre)
                db.session.commit()
                return jsonify({'Message': 'Suppression Livre avec succès'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500


@route_livre.route('/sh/search/livre')
def search_livre():
    try:
        theme = request.args.get('theme', default=None)
        cat = request.args.get('cat', default=None)
        parc = request.args.get('parc', default=None)
        niv = request.args.get('niv', default=None)

        livres = search_livre_by_theme_categorie_parcours_niveau(
            theme, cat, parc, niv)

        return jsonify([livre_to_dict_2(livre) for livre in livres]), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500
