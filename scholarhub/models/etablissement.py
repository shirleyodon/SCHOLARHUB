from .. import db

class EtablissementAccueil(db.Model):
    __tablename__ = 'etablissementAccueil'
    idEtab = db.Column('IdEtab', db.Integer, primary_key=True)
    adresse = db.Column('Adresse', db.String(100), nullable=False)
    contact = db.Column('Contact', db.String(20), nullable=False)
    nomEtab = db.Column('NomEtab', db.String(100), nullable=False)
    sigle = db.Column('Sigle', db.String(30))
    siteWeb = db.Column('SiteWeb', db.String(100))

    # One-to-many with Livre
    livres = db.relationship('Livre', backref='etablissementAccueil', lazy=True)

    def __init__(self, adr, contact, nom, sigle, site):
        self.adresse = adr
        self.contact = contact
        self.nomEtab = nom
        self.sigle = sigle
        self.siteWeb = site