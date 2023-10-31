from .. import db

class NiveauEtude(db.Model):
    __tablename__ = 'niveauEtude'
    idNiv = db.Column('IdNiv', db.Integer, primary_key=True)
    libelleNiv = db.Column('LibelleNiv', db.String(5), nullable=False)

    # One-to-many with Livre
    livres = db.relationship('Livre', backref='niveauEtude', lazy=True)

    def __init__(self, libelle):
        self.libelleNiv = libelle