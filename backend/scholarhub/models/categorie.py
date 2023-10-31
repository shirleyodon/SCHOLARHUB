from .. import db

class CategorieLivre(db.Model):
    __tablename__ = 'categorieLivre'
    numCat = db.Column('NumCat', db.Integer, primary_key=True)
    libelleCat = db.Column('LibelleCat', db.String(50), nullable=False)

    # One-to-many with Livre
    livres = db.relationship('Livre', backref='categorieLivre', lazy=True)

    def __init__(self, libelle):
        self.libelleCat = libelle