from ..models import NiveauEtude


# Dictionnary to NiveauEtude
def dict_to_niveau(niv_dict):
    return NiveauEtude(
        id=niv_dict['IdNiv'],
        libelle=niv_dict['LibelleNiv']
    )
