from .. import db
from .inscription import inscription
from .redaction import redaction
from .niveau import NiveauEtude

class Etudiant(db.Model):
    __tablename__ = 'etudiant'
    matEtud = db.Column('MatEtud', db.String(10), primary_key=True)
    emailEtud = db.Column('EmailEtud', db.String(50))
    motPasseEtud = db.Column('MotPasseEtud', db.String(50))
    nomEtud = db.Column('NomEtud', db.String(30), nullable=False)
    prenomEtud = db.Column('PrenomEtud', db.String(50), nullable=False)

    # Many-to-one with ParcoursEtude
    numParc = db.Column('NumParc', db.Integer, db.ForeignKey('parcoursEtude.NumParc'), nullable=False)
    
    # Many-to-many with NiveauEtude and AnneeUniversitaire
    niveauxEtude = db.relationship('NiveauEtude',
        secondary = inscription,
        primaryjoin = matEtud==inscription.c.MatEtud,
        secondaryjoin = NiveauEtude.idNiv==inscription.c.IdNiv,
        backref = db.backref('etudiants', lazy='dynamic'),
        lazy = 'dynamic'
    )

    # Many-to-many with Livre
    livres = db.relationship('Livre', secondary=redaction, lazy='subquery', backref=db.backref('etudiants', lazy=True))

    def __init__(self, mat, email, pwd, nom, prenom, parc):
        self.matEtud = mat
        self.emailEtud = email
        self.motPasseEtud = pwd
        self.nomEtud = nom
        self.prenomEtud = prenom
        self.numParc = parc