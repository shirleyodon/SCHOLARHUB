class Livre():
    def __init__(self, ref, clef, page, resume, theme, url, annee, etab, niv, encad, cat):
        self.refLivre = ref
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

    def to_dict(self):
        return {
            'RefLivre': self.refLivre,
            'MotCle': self.motCle,
            'NbPage': self.nbPage,
            'Resume': self.resume,
            'Theme': self.theme,
            'Url': self.url,
            'CodeAnnee': self.codeAnnee,
            'IdEtab': self.idEtab,
            'IdNiv': self.idNiv,
            'MatEncad': self.matEncad,
            'NumCat': self.numCat
        }


class LivrePlus():
    def __init__(self, ref, clef, page, resume, theme, url, annee, etab, niv, encad, cat, etudiants):
        self.refLivre = ref
        self.motCle = clef
        self.nbPage = page
        self.resume = resume
        self.theme = theme
        self.url = url
        self.anneeUniversitaire = annee
        self.etablissementAccueil = etab
        self.niveauEtude = niv
        self.encadreurPedagogique = encad
        self.categorieLivre = cat
        self.etudiants = etudiants

    def to_dict(self):
        return {
            'RefLivre': self.refLivre,
            'MotCle': self.motCle,
            'NbPage': self.nbPage,
            'Resume': self.resume,
            'Theme': self.theme,
            'Url': self.url,

            'AnneeUniversitaire': self.anneeUniversitaire.to_dict(),
            'EtablissementAcceuil': self.etablissementAccueil.to_dict(),
            'NiveauEtude': self.niveauEtude.to_dict(),
            'EncadreurPedagogique': self.encadreurPedagogique.to_dict(),
            'CategorieLivre': self.categorieLivre.to_dict(),
            'Etudiants': [etud.to_dict() for etud in self.etudiants]
        }
