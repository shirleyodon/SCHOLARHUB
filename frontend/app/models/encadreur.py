class EncadreurPedagogique():
    def __init__(self, mat, email, pwd, nom, prenom, titre):
        self.matEncad = mat
        self.emailEncad = email
        self.motPasseEncad = pwd
        self.nomEncad = nom
        self.prenomEncad = prenom
        self.codeTitre = titre

    def to_dict(self):
        return {
            'MatEncad': self.matEncad,
            'EmailEncad': self.emailEncad,
            'MotPasseEncad': self.motPasseEncad,
            'NomEncad': self.nomEncad,
            'PrenomEncad': self.prenomEncad,
            'CodeTitre': self.codeTitre,
        }
