class NiveauEtude():
    def __init__(self, id, libelle):
        self.idNiv = id
        self.libelleNiv = libelle

    def to_dict(self):
        return {
            'IdNiv': self.idNiv,
            'LibelleNiv': self.libelleNiv,
        }
