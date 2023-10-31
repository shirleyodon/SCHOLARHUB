from .. import db

# Livre-Etudiant association table
redaction = db.Table('redaction',
    db.Column('RefLivre', db.Integer, db.ForeignKey('livre.RefLivre'), primary_key=True),
    db.Column('MatEtud', db.String(10), db.ForeignKey('etudiant.MatEtud'), primary_key=True),
)