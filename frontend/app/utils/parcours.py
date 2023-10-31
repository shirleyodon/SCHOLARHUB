from ..models import ParcoursEtude


# Dictionnary to Parcours
def dict_to_parcours(parc_dict):
    return ParcoursEtude(
        num=parc_dict['NumParc'],
        libelle=parc_dict['LibelleParc']
    )
