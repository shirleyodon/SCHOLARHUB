from ..models import ParcoursEtude

# Object ParcoursEtude to dictionnary
def parcours_to_dict_1(parc):
    return {
        'NumParc': parc.numParc,
        'LibelleParc': parc.libelleParc,
    }

def parcours_to_dict_2(parc):
    from .etudiant import etudiant_to_dict_1
    
    return {
        'NumParc': parc.numParc,
        'LibelleParc': parc.libelleParc,
        'Etudiants': [etudiant_to_dict_1(etudiant) for etudiant in parc.etudiants]
    }

# Get all ParcoursEtude
def get_all_parcours():
    return ParcoursEtude.query.all()

# Get a ParcoursEtude
def get_parcours(numParc):
    return ParcoursEtude.query.get(numParc)

# Create ParcoursEtude object with Json data
def create_parcours(json_data):
    return ParcoursEtude(json_data.get('LibelleParc'))

# Updata ParcoursEtude object with Json data
def update_parcours(parc, json_data):
    parc.libelleParc = json_data.get('LibelleParc')