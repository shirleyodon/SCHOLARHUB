from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import parcours_to_dict_1, get_all_parcours, get_parcours, create_parcours, \
    update_parcours

route_parcours = Blueprint('route_parcours', __name__)


@route_parcours.route("/sh/parcoursetude/", methods=["GET", "POST"])
def create_or_get_all_parcours():
    if request.method == "GET":
        try:
            parcours = get_all_parcours()
            return jsonify([parcours_to_dict_1(parc) for parc in parcours]), 200

        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500

    else:
        try:
            data = request.get_json()
            if data:
                db.session.add(create_parcours(data))
                db.session.commit()
                return jsonify({'Message': 'Nouveau ParcoursEtude créé avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400

        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500


@route_parcours.route("/sh/parcoursetude/<int:numParc>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_parcours(numParc):
    try:
        parcours = get_parcours(numParc)

        # Si le parcoursEtude n'existe pas
        if not parcours:
            return jsonify({'Erreur': "Aucun ParcoursEtude n'a été trouvé"}), 404
        else:
            if request.method == "GET":
                return jsonify(parcours_to_dict_1(parcours)), 200

            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_parcours(parcours, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour ParcoursEtude avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(parcours)
                db.session.commit()
                return jsonify({'Message': 'Suppression ParcoursEtude avec succès'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500
