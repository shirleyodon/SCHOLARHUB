from .. import db

class ParcoursEtude(db.Model):
    __tablename__ = 'parcoursEtude'
    numParc = db.Column('NumParc', db.Integer, primary_key=True)
    libelleParc = db.Column('LibelleParc', db.String(50), nullable=False)

    # One-to-many with Etudiant
    etudiants = db.relationship('Etudiant', backref='parcoursEtude', lazy=True)

    def __init__(self, libelle):
        self.libelleParc = libelle