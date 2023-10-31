class ParcoursEtude():
    def __init__(self, num, libelle):
        self.numParc = num
        self.libelleParc = libelle

    def to_dict(self):
        return {
            'NumParc': self.numParc,
            'LibelleParc': self.libelleParc,
        }
