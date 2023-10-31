from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import etudiant_to_dict_1, etudiant_to_dict_2, get_all_etudiant, get_etudiant, create_etudiant, \
    update_etudiant, search_etudiant_by_email

route_etudiant = Blueprint('route_etudiant', __name__)


@route_etudiant.route("/sh/etudiant/", methods=["GET", "POST"])
def create_or_get_all_etudiants():
    if request.method == "GET":
        try:
            etudiants = get_all_etudiant()
            return jsonify([etudiant_to_dict_2(etud) for etud in etudiants]), 200

        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500

    else:
        try:
            data = request.get_json()
            if data:
                db.session.add(create_etudiant(data))
                db.session.commit()
                return jsonify({'Message': 'Nouvel Etudiant créé avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400

        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500


@route_etudiant.route("/sh/etudiant/<matEtud>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_etudiant(matEtud):
    try:
        etudiant = get_etudiant(matEtud)

        # Si l'etudiant n'existe pas
        if not etudiant:
            return jsonify({'Erreur': "Aucun Etudiant n'a été trouvé"}), 404
        else:
            if request.method == "GET":
                return jsonify(etudiant_to_dict_2(etudiant))

            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_etudiant(etudiant, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour Etudiant avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(etudiant)
                db.session.commit()
                return jsonify({'Message': 'Suppression Etudiant avec succès'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig']) if 'origin' in e.__dict__ else e
        print(msg)
        return jsonify({'Erreur': msg}), 500


# Search an Etudiant by E-mail
@route_etudiant.route('/sh/search/etudiant/byemail/<email>/')
def search_by_email(email):
    try:
        etudiant = search_etudiant_by_email(email)
        # Si l'etudiant n'existe pas
        if not etudiant:
            return jsonify({'Erreur': "Aucun compte rataché à cet E-mail n'a été trouvé"}), 404
        else:
            return jsonify(etudiant_to_dict_1(etudiant)), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig']) if 'origin' in e.__dict__ else e
        print(msg)
        return jsonify({'Erreur': msg}), 500


# Search an Etudiant by matricule
@route_etudiant.route('/sh/search/etudiant/bymatricule/<matricule>/')
def search_by_matricule(matricule):
    try:
        etudiant = get_etudiant(matricule)
        # Si l'etudiant n'existe pas
        if not etudiant:
            return jsonify({'Erreur': "Aucun Etudiant n'a été trouvé"}), 404
        else:
            return jsonify(etudiant_to_dict_1(etudiant)), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig']) if 'origin' in e.__dict__ else e
        print(msg)
        return jsonify({'Erreur': msg}), 500
