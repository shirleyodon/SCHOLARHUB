from .. import db

class EncadreurPedagogique(db.Model):
    __tablename__ = 'encadreurPedagogique'
    matEncad = db.Column('MatEncad', db.String(10), primary_key=True)
    emailEncad = db.Column('EmailEncad', db.String(50))
    motPasseEncad = db.Column('MotPasseEncad', db.String(50))
    nomEncad = db.Column('NomEncad', db.String(30), nullable=False)
    prenomEncad = db.Column('PrenomEncad', db.String(50), nullable=False)
    # Many-to-one with TitreEncadreur
    codeTitre = db.Column('CodeTitre', db.Integer, db.ForeignKey('titreEncadreur.CodeTitre'), nullable=False)
    # One-to-many with Livre
    livres = db.relationship('Livre', backref='encadreurPedagogique', lazy=True)

    def __init__(self, mat, email, pwd, nom, prenom, titre):
        self.matEncad = mat
        self.emailEncad = email
        self.motPasseEncad = pwd
        self.nomEncad = nom
        self.prenomEncad = prenom
        self.codeTitre = titre
