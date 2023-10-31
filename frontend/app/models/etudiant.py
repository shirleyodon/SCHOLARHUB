class Etudiant():
    def __init__(self, mat, email, pwd, nom, prenom, parc):
        self.matEtud = mat
        self.emailEtud = email
        self.motPasseEtud = pwd
        self.nomEtud = nom
        self.prenomEtud = prenom
        self.numParc = parc

    def to_dict(self):
        return {
            "MatEtud": self.matEtud,
            "EmailEtud": self.emailEtud,
            "MotPasseEtud": self.motPasseEtud,
            "NomEtud": self.nomEtud,
            "PrenomEtud": self.prenomEtud,
            "NumParc": self.numParc
        }


class EtudiantPlus():
    # Etudiant with Parcours object

    def __init__(self, mat, email, pwd, nom, prenom, parc):
        self.matEtud = mat
        self.emailEtud = email
        self.motPasseEtud = pwd
        self.nomEtud = nom
        self.prenomEtud = prenom
        self.parcoursEtude = parc

    def to_dict(self):
        return {
            "MatEtud": self.matEtud,
            "EmailEtud": self.emailEtud,
            "MotPasseEtud": self.motPasseEtud,
            "NomEtud": self.nomEtud,
            "PrenomEtud": self.prenomEtud,
            "ParcoursEtudiant": self.parcoursEtude.to_dict()
        }
