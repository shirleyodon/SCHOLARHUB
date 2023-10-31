from ..models import TitreEncadreur


# Dictionnary to TitreEncadreur
def dict_to_titre(titre_dict):
    return TitreEncadreur(
        code=titre_dict['CodeTitre'],
        libelle=titre_dict['LibelleTitre']
    )
