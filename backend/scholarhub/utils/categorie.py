from ..models import CategorieLivre

# Object CategorieLivre to dictionnary


def categorie_to_dict_1(cat):
    return {
        'NumCat': cat.numCat,
        'LibelleCat': cat.libelleCat,
    }


def categorie_to_dict_2(cat):
    from .livre import livre_to_dict_1

    return {
        'NumCat': cat.numCat,
        'LibelleCat': cat.libelleCat,
        'Livres': [livre_to_dict_1(livre) for livre in cat.livres]
    }

# Get all CategorieLivre


def get_all_categorie():
    return CategorieLivre.query.all()

# Get a CategorieLivre


def get_categorie(numCat):
    return CategorieLivre.query.get(numCat)

# Create a CategorieLivre from Json data


def create_categorie(json_data):
    return CategorieLivre(json_data.get('LibelleCat'))

# Update a CategorieLivre object with Json data


def update_categorie(cat, json_data):
    cat.libelleCat = json_data.get('LibelleCat')


# Search Categorie by libelleCat
def search_categorie_by_libelle(libelle):
    return CategorieLivre.query.filter(CategorieLivre.libelleCat.ilike(f'{libelle}')).first()
