class TitreEncadreur():
    def __init__(self, code, libelle):
        self.codeTitre = code
        self.libelleTitre = libelle

    def to_dict(self):
        return {
            'CodeTitre': self.codeTitre,
            'LibelleTitre': self.libelleTitre
        }
