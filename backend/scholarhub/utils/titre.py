from ..models import TitreEncadreur

# Object TitreEncadreur to dictionnary
def titre_to_dict_1(titre):
    return {
        'CodeTitre': titre.codeTitre,
        'LibelleTitre': titre.libelleTitre
    }

def titre_to_dict_2(titre):
    from .encadreur import encadreur_to_dict_1
    
    return {
        'CodeTitre': titre.codeTitre,
        'LibelleTitre': titre.libelleTitre,
        'EncadreursPedagogiques': [encadreur_to_dict_1(encad) for encad in titre.encadreursPedagogiques]
    }

# Get all TitreEncadreur
def get_all_titre():
    return TitreEncadreur.query.all()

# Get a TitreEncadreur
def get_titre(codeTitre):
    return TitreEncadreur.query.get(codeTitre)

# Create TitreEncadreur object with Json data
def create_titre(json_data):
    return TitreEncadreur(json_data.get('LibelleTitre'))

# Updata TitreEncadreur object with Json data
def update_titre(titre, json_data):
    titre.libelleTitre = json_data.get('LibelleTitre')