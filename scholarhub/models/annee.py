from .. import db

class AnneeUniversitaire(db.Model):
    __tablename__ = 'anneeUniversitaire'
    codeAnnee = db.Column('CodeAnnee', db.Integer, primary_key=True)
    libelleAnnee = db.Column('LibelleAnnee', db.String(20), nullable=False)
    
    # One-to-many with Livre
    livres = db.relationship('Livre', backref='anneeUniversitaire', lazy=True)

    def __init__(self, libelle):
        self.libelleAnnee = libelle