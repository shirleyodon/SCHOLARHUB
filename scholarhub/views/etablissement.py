from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import etablissement_to_dict_2, get_all_etablissement, get_etablissement, \
    create_etablissement, update_etablissement

route_etablissement = Blueprint('route_etablissement', __name__)

@route_etablissement.route("/sh/etablissementacceuil/", methods=["GET", "POST"])
def create_or_get_all_etablissements():
    if request.method == "GET":
        try:
            etablissements = get_all_etablissement()
            return jsonify([etablissement_to_dict_2(etab) for etab in etablissements]), 200
        
        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
    else:
        try:
            data = request.get_json()
            if data :
                db.session.add(create_etablissement(data))
                db.session.commit()
                return jsonify({'Message': 'Nouvel EtablissementAcceuil créé avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
        
        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
        
@route_etablissement.route("/sh/etablissementacceuil/<int:idEtab>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_etablissement(idEtab):
    try:
        etablissement = get_etablissement(idEtab)

        # Si l'etablissement n'existe pas
        if not etablissement:
            return jsonify({'Erreur': "Aucun EtablissementAcceuil n'a été trouvé"}), 404
        else:
            if request.method == "GET":
                return jsonify(etablissement_to_dict_2(etablissement))
            
            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_etablissement(etablissement, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour EtablissementAcceuil avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(etablissement)
                db.session.commit()
                return jsonify({'Message': 'Suppression EtablissementAcceuil avec succès'}), 200
    
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500