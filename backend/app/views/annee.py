from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import annee_to_dict_1, get_all_annee, get_annee, create_annee, update_annee

route_annee = Blueprint('route_annee', __name__)


@route_annee.route("/sh/anneeuniversitaire/", methods=["GET", "POST"])
def create_or_get_all_annees():
    if request.method == "GET":
        try:
            annees = get_all_annee()
            return jsonify([annee_to_dict_1(an) for an in annees]), 200

        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500

    else:
        try:
            data = request.get_json()
            if data:
                db.session.add(create_annee(data))
                db.session.commit()
                return jsonify({'Message': 'Nouvelle AnneeUniversitaire créée avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400

        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500


@route_annee.route("/sh/anneeuniversitaire/<int:codeAnnee>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_annee(codeAnnee):
    try:
        annee = get_annee(codeAnnee)

        # Si l'annee n'existe pas
        if not annee:
            return jsonify({'Erreur': "Aucune AnneeUniversitaire n'a été trouvée"}), 404
        else:
            if request.method == "GET":
                return jsonify(annee_to_dict_1(annee))

            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_annee(annee, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour AnneeUniversitaire avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(annee)
                db.session.commit()
                return jsonify({'Message': "Suppression AnneeUniversitaire avec succès"}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500
