from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import niveau_to_dict_2, get_all_niveau, get_niveau, create_niveau, update_niveau

route_niveau = Blueprint('route_niveau', __name__)

@route_niveau.route("/sh/niveauetude/", methods=["GET", "POST"])
def create_or_get_all_niveaux():
    if request.method == "GET":
        try:
            niveaux = get_all_niveau()
            return jsonify([niveau_to_dict_2(niv) for niv in niveaux]), 200
        
        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
    else:
        try:
            data = request.get_json()
            if data :
                db.session.add(create_niveau(data))
                db.session.commit()
                return jsonify({'Message': 'Nouveau NiveauEtude créé avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
        
        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
        
@route_niveau.route("/sh/niveauetude/<int:idNiv>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_niveau(idNiv):
    try:
        niveau = get_niveau(idNiv)

        # Si le niveau n'existe pas
        if not niveau:
            return jsonify({'Erreur': "Aucun NiveauEtude n'a été trouvé"}), 404
        else:
            if request.method == "GET":
                return jsonify(niveau_to_dict_2(niveau))
            
            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_niveau(niveau, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour NiveauEtude avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(niveau)
                db.session.commit()
                return jsonify({'Message': 'Suppression NiveauEtude avec succès'}), 200
    
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500