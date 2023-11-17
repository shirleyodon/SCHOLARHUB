import requests
from ..models import EncadreurPedagogique, Error, Success
from ..config import Config

BACKEND_BASE_URL = Config.BACKEND_BASE_URL


# Dictionnary to EncadreurPedagogique
def dict_to_encadreur(encad_dict):
    return EncadreurPedagogique(
        mat=encad_dict['MatEncad'],
        email=encad_dict['EmailEncad'],
        pwd=encad_dict['MotPasseEncad'],
        nom=encad_dict['NomEncad'],
        prenom=encad_dict['PrenomEncad'],
        titre=encad_dict['CodeTitre']
    )

# Search an EncadreurPedagogique by E-mail
def search_encadreur_by_email(email):
    url = f"{BACKEND_BASE_URL}search/encadreurpedagogique/byemail/{email}"

    try:
        response = requests.get(url)
        # Si le backend repond favorablement
        if response.status_code == 200:
            return dict_to_encadreur(response.json())

        # Si resource Not found
        else:
            return Error(response.json())

    except requests.exceptions.RequestException as e:
        message = "Une erreur s'est produite ! Veillez verifier que le serveur backend fonctionne"
        print(f"{message}\n{e}")

        return Error(message)
    
    
# Search Encadreur by matricule
def search_encadreur_by_matricule(matricule):
    url = f"{BACKEND_BASE_URL}encadreurpedagogique/{matricule}"
    try:
        response = requests.get(url)
        # Si le backend repond favorablement
        if response.status_code == 200:
            return dict_to_encadreur(response.json())

        # Si resource Not found
        else:
            return Error(response.json())

    except requests.exceptions.RequestException as e:
        message = "Une erreur s'est produite ! Veillez verifier que le serveur backend fonctionne"
        print(f"{message}\n{e}")

        return Error(message)
    

# Enrol EncadreurPedagogique
def enrol_encadreur(encad_dict):
    url = f"{BACKEND_BASE_URL}encadreurpedagogique/{encad_dict['MatEncad']}"

    try:
        response = requests.put(url, json=encad_dict)
        # Si le backend repond favorablement
        if response.status_code == 200:
            return Success(response.json())
        # Si resource Not found
        else:
            return Error(response.json())

    except requests.exceptions.RequestException as e:
        message = "Une erreur s'est produite ! Veillez verifier que le serveur backend fonctionne"
        print(f"{message}\n{e}")

        return Error(message)

    
# To prevent duplicated E-mail
def is_valid_encadreur_email(email):
    '''To prevent duplicated email as login'''
    response = search_encadreur_by_email(email)
    return not isinstance(response, EncadreurPedagogique)