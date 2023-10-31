from .. import db

class Livre(db.Model):
    __tablename__ = 'livre'
    refLivre = db.Column('RefLivre', db.Integer, primary_key=True)
    motCle = db.Column('MotCle', db.Text, nullable=False)
    nbPage = db.Column('NbPage', db.Integer, nullable=False)
    resume = db.Column('Resume', db.Text, nullable=False)
    theme = db.Column('Theme', db.Text, nullable=False)
    url = db.Column('Url', db.String(200), nullable=False)
    
    # Many-to-one with AnneeUniversitaire
    codeAnnee = db.Column('CodeAnnee', db.Integer, db.ForeignKey('anneeUniversitaire.CodeAnnee'), nullable=False)
    
    # Many-to-one with EtablissementAccueil
    idEtab = db.Column('IdEtab', db.Integer, db.ForeignKey('etablissementAccueil.IdEtab'), nullable=False)
    
    # Many-to-one with NiveauEtude
    idNiv = db.Column('IdNiv', db.Integer, db.ForeignKey('niveauEtude.IdNiv'), nullable=False)

    # Many-to-one with EncadreurPedagogique
    matEncad = db.Column('MatEncad', db.String(10), db.ForeignKey('encadreurPedagogique.MatEncad'), nullable=False)
    
    # Many-to-one with CategorieLivre
    numCat = db.Column('NumCat', db.Integer, db.ForeignKey('categorieLivre.NumCat'), nullable=False)

    def __init__(self, clef, page, resume, theme, url, annee, etab, niv, encad, cat):
        self.motCle = clef
        self.nbPage = page
        self.resume = resume
        self.theme = theme
        self.url = url
        self.codeAnnee = annee
        self.idEtab = etab
        self.idNiv = niv
        self.matEncad = encad
        self.numCat = cat
        
        
        
