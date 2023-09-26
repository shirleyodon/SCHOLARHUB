from ..models import Etudiant

# Object Etudiant to dictionnary
def etudiant_to_dict_1(etud):
    return {
        'MatEtud': etud.matEtud,
        'EmailEtud': etud.emailEtud,
        'MotPasseEtud': etud.motPasseEtud,
        'NomEtud': etud.nomEtud,
        'PrenomEtud': etud.prenomEtud,
        'NumParc': etud.numParc
    }

def etudiant_to_dict_2(etud):
    from .livre import livre_to_dict_1
    from .niveau import niveau_to_dict_1
    from .parcours import parcours_to_dict_1
    
    return {
        'MatEtud': etud.matEtud,
        'EmailEtud': etud.emailEtud,
        'MotPasseEtud': etud.motPasseEtud,
        'NomEtud': etud.nomEtud,
        'PrenomEtud': etud.prenomEtud,
        'ParcoursEtudiant': parcours_to_dict_1(etud.parcoursEtude),
        'NiveauxEtude': [niveau_to_dict_1(niv) for niv in etud.niveauxEtude],
        'Livres': [livre_to_dict_1(livre) for livre in etud.livres]
    }

# Get all Etudiant
def get_all_etudiant():
    return Etudiant.query.all()

# Get an Etudiant
def get_etudiant(matEtud):
    return Etudiant.query.get(matEtud)

# Create Etudiant with Json data
def create_etudiant(json_data):
    return Etudiant(
        json_data.get('MatEtud'),
        json_data.get('EmailEtud') if json_data.get('EmailEtud') else None,
        json_data.get('MotPasseEtud') if json_data.get('MotPasseEtud') else None,
        json_data.get('NomEtud'),
        json_data.get('PrenomEtud'),
        json_data.get('NumParc')
    )

# Update Etudiant with Json data
def update_etudiant(etud, json_data):
    etud.matEtud = json_data.get('MatEtud')
    etud.emailEtud = json_data.get('EmailEtud') if json_data.get('EmailEtud') else None
    etud.motPasseEtud = json_data.get('MotPasseEtud') if json_data.get('MotPasseEtud') else None
    etud.nomEtud = json_data.get('NomEtud')
    etud.prenomEtud = json_data.get('PrenomEtud')
    etud.numParc = json_data.get('NumParc')