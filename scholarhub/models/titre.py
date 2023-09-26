from .. import db

class TitreEncadreur(db.Model):
    __tablename__ = 'titreEncadreur'
    codeTitre = db.Column('CodeTitre', db.Integer, primary_key=True)
    libelleTitre = db.Column('LibelleTitre', db.String(100), nullable=False)
    # One-to-many with EncadreurPedagogique
    encadreursPedagogiques = db.relationship('EncadreurPedagogique', backref='titreEncadreur', lazy=True)

    def __init__(self, libelle):
        self.libelleTitre = libelle