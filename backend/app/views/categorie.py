from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from .. import db
from ..utils import categorie_to_dict_2, get_all_categorie, get_categorie, create_categorie, \
    update_categorie

route_categorie = Blueprint('route_categorie', __name__)

@route_categorie.route("/sh/categorielivre/", methods=["GET", "POST"])
def create_or_get_all_categories():
    if request.method == "GET":
        try:
            categories = get_all_categorie()
            return jsonify([categorie_to_dict_2(cat) for cat in categories]), 200
        
        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
    else:
        try:
            data = request.get_json()
            if data :
                db.session.add(create_categorie(data))
                db.session.commit()
                return jsonify({'Message': 'Nouvelle CategorieLivre créée avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
        
        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
    
@route_categorie.route("/sh/categorielivre/<int:numCat>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_categorie(numCat):
    try:
        categorie = get_categorie(numCat)

        # Si la categorie n'existe pas
        if not categorie:
            return jsonify({'Erreur': "Aucune CategorieLivre n'a été trouvée"}), 404
        else:
            if request.method == "GET":
                return jsonify(categorie_to_dict_2(categorie))
            
            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    update_categorie(categorie, data)
                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour CategorieLivre avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.delete(categorie)
                db.session.commit()
                return jsonify({'Message': 'Suppression CategorieLivre avec succès'}), 200
    
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500
