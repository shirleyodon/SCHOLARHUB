from ..models import CategorieLivre


# Dictionnary to CategorieLivre
def dict_to_categorie(cat_dict):
    return CategorieLivre(
        num=cat_dict['NumCat'],
        libelle=cat_dict['LibelleCat']
    )
