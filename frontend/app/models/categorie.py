class CategorieLivre():
    def __init__(self, num, libelle):
        self.numCat = num
        self.libelleCat = libelle

    def to_dict(self):
        return {
            'NumCat': self.numCat,
            'LibelleCat': self.libelleCat,
        }
