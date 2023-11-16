from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import encadreur_to_dict_1, get_all_encadreur, get_encadreur, create_encadreur, \
    update_encadreur, search_encadreur_by_email

route_encadreur = Blueprint('route_encadreur', __name__)


@route_encadreur.route("/sh/encadreurpedagogique/", methods=["GET", "POST"])
def create_or_get_all_encadreurs():
    if request.method == "GET":
        try:
            encadreurs = get_all_encadreur()
            return jsonify([encadreur_to_dict_1(encad) for encad in encadreurs]), 200

        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500

    else:
        try:
            data = request.get_json()
            if data:
                db.session.add(create_encadreur(data))
                db.session.commit()
                return jsonify({'Message': 'Nouvel EncadreurPedagogique créé avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400

        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500


@route_encadreur.route("/sh/encadreurpedagogique/<matEncad>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_encadreurs(matEncad):
    try:
        encadreur = get_encadreur(matEncad)

        # Si l'encadreur n'existe pas
        if not encadreur:
            return jsonify({'Erreur': "Aucun EncadreurPedagogique n'a été trouvé"}), 404
        else:
            if request.method == "GET":
                return jsonify(encadreur_to_dict_1(encadreur)), 200

            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_encadreur(encadreur, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour EncadreurPedagogique avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(encadreur)
                db.session.commit()
                return jsonify({'Message': 'Suppression EncadreurPedagogique avec succès'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500


# Search an EncadreurPedagogique by E-mail
@route_encadreur.route('/sh/search/encadreurpedagogique/byemail/<email>/')
def search_by_email(email):
    try:
        encadreur = search_encadreur_by_email(email)

        # Si l'encadreur n'existe pas
        if not encadreur:
            return jsonify({'Erreur': "Aucun compte rataché à cet E-mail n'a été trouvé"}), 404
        else:
            return jsonify(encadreur_to_dict_1(encadreur)), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig']) if 'origin' in e.__dict__ else e
        print(msg)
        return jsonify({'Erreur': msg}), 500