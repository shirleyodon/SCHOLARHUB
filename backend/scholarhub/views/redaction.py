from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from .. import db
from ..models import redaction
from ..utils import redaction_to_dict, create_redaction

route_redaction = Blueprint('route_redaction', __name__)

@route_redaction.route("/sh/redaction/", methods=["GET", "POST"])
def create_or_get_all_redaction():
    if request.method == "GET":
        try:
            all_redactions = db.session.execute(redaction.select()).fetchall()
            return jsonify([redaction_to_dict(a_redaction) for a_redaction in all_redactions]), 200
        
        except SQLAlchemyError as e:
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
    else:
        try:
            data = request.get_json()
            if data :
                db.session.execute(redaction.insert().values(create_redaction(data)))
                db.session.commit()
                return jsonify({'Message': 'Nouvelle redaction créée avec succès'}), 201
            else:
                return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
        
        except SQLAlchemyError as e:
            db.session.rollback()
            msg = str(e.__dict__['orig'])
            print(msg)
            return jsonify({'Erreur': msg}), 500
        
        
@route_redaction.route("/sh/redaction/<int:refLivre>/<string:matEtud>/", methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_redaction(refLivre, matEtud):
    try:
        a_redaction = db.session.execute(
            redaction.select().where(
                and_(
                    redaction.c.RefLivre == refLivre,
                    redaction.c.MatEtud == matEtud
                )
            )
        ).fetchone()

        # Si la redaction n'existe pas
        if not a_redaction:
            return jsonify({'Erreur': "Aucune redaction n'a été trouvée"}), 404
        else:
            if request.method == "GET":
                return jsonify(redaction_to_dict(a_redaction))
            
            elif request.method == "PUT":
                data = request.get_json()
                if data:
                    db.session.execute(
                        redaction.update().where(
                            and_(
                                redaction.c.RefLivre == refLivre,
                                redaction.c.MatEtud == matEtud
                            )
                        ).values(create_redaction(data))
                    )

                    db.session.commit()
                    return jsonify({'Message': 'Mise à jour redaction avec succès'}), 200
                else:
                    return jsonify({'Erreur': "Aucune donnée n'a été envoyée"}), 400
            else:
                db.session.execute(
                    redaction.delete().where(
                        and_(
                            redaction.c.RefLivre == refLivre,
                            redaction.c.MatEtud == matEtud
                        )
                    )
                )
                db.session.commit()
                return jsonify({'Message': "Suppression redaction avec succès"}), 200
    
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = str(e.__dict__['orig'])
        print(msg)
        return jsonify({'Erreur': msg}), 500