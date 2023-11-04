from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import titre_to_dict_1, get_all_titre, get_titre, create_titre, update_titre

route_titre = Blueprint('route_titre', __name__)


@route_titre.route("/sh/titreencadreur/", methods=["GET", "POST"])
def create_or_get_all_titres():
    if request.method == "GET":
        try:
            titres = get_all_titre()
            return jsonify([titre_to_dict_1(titre) for titre in titres]), 200

        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500

    else:
        try:
            data = request.get_json()
            if data:
                db.session.add(create_titre(data))
                db.session.commit()
                return jsonify({'Message': 'Nouveau TitreEncadreur créé avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400

        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500


@route_titre.route("/sh/titreencadreur/<int:codeTitre>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_titre(codeTitre):
    try:
        titre = get_titre(codeTitre)

        # Si le titre n'existe pas
        if not titre:
            return jsonify({'Erreur': "Aucun TitreEncadreur n'a été trouvé"}), 404
        else:
            if request.method == "GET":
                return jsonify(titre_to_dict_1(titre))

            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_titre(titre, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour TitreEncadreur avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(titre)
                db.session.commit()
                return jsonify({'Message': 'Suppression TitreEncadreur avec succès'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500
