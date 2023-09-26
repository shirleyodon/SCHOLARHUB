from .. import db

# Etudiant-NiveauEtude-CodeAnnee association table
inscription = db.Table('inscription',
    db.Column('MatEtud', db.String(10), db.ForeignKey('etudiant.MatEtud'), primary_key=True),
    db.Column('IdNiv', db.Integer, db.ForeignKey('niveauEtude.IdNiv'), primary_key=True),
    db.Column('CodeAnnee', db.Integer, db.ForeignKey('anneeUniversitaire.CodeAnnee'), primary_key=True)            
)