from ..models import AnneeUniversitaire


# Dictionnary to AnneeUniversitaire
def dict_to_annee(annee_dict):
    return AnneeUniversitaire(
        code=annee_dict['CodeAnnee'],
        libelle=annee_dict['LibelleAnnee']
    )
