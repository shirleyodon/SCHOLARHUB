class AnneeUniversitaire():
    def __init__(self, code, libelle):
        self.codeAnnee = code
        self.libelleAnnee = libelle

    def to_dict(self):
        return {
            'CodeAnnee': self.codeAnnee,
            'LibelleAnnee': self.libelleAnnee,
        }
