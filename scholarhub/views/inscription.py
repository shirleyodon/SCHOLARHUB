from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from .. import db
from ..models import inscription
from ..utils import inscription_to_dict, create_inscription

route_inscription = Blueprint('route_inscription', __name__)

@route_inscription.route("/sh/inscription/", methods=["GET", "POST"])
def create_or_get_all_inscriptions():
    if request.method == "GET":
        try:
            all_inscriptions = db.session.execute(inscription.select()).fetchall()
            return jsonify([inscription_to_dict(an_inscription) for an_inscription in all_inscriptions]), 200
        
        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
    else:
        try:
            data = request.get_json()
            if data :
                db.session.execute(inscription.insert().values(create_inscription(data)))
                db.session.commit()
                return jsonify({'Message': 'Nouvelle inscription créée avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
        
        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
        
@route_inscription.route("/sh/inscription/<string:matEtud>/<int:idNiv>/<int:codeAnnee>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_inscription(matEtud, idNiv, codeAnnee):
    try:
        an_insription = db.session.execute(
            inscription.select().where(
                and_(inscription.c.MatEtud == matEtud,
                     inscription.c.IdNiv == idNiv,
                     inscription.c.CodeAnnee == codeAnnee
                )
            )
        ).fetchone()

        # Si l'inscription n'existe pas
        if not an_insription:
            return jsonify({'Erreur': "Aucune inscription n'a été trouvée"}), 404
        else:
            if request.method == "GET":
                return jsonify(inscription_to_dict(an_insription))
            
            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    db.session.execute(
                        inscription.update().where(
                            and_(inscription.c.MatEtud == matEtud,
                                inscription.c.IdNiv == idNiv,
                                inscription.c.CodeAnnee == codeAnnee
                            )
                        ).values(create_inscription(data))
                    )

                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour inscription avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.execute(
                    inscription.delete().where(
                        and_(inscription.c.MatEtud == matEtud,
                            inscription.c.IdNiv == idNiv,
                            inscription.c.CodeAnnee == codeAnnee
                        )
                    )
                )
                db.session.commit()
                return jsonify({'Message': "Suppression inscription avec succès"}), 200
    
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500