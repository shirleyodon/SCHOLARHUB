import requests
from ..models import Etudiant, EtudiantPlus, Success, Error
from ..config import Config

BACKEND_BASE_URL = Config.BACKEND_BASE_URL

# Dictionnary to Etudiant object
def dict_to_etudiant(etud_dict):
    return Etudiant(
        mat=etud_dict['MatEtud'],
        email=etud_dict['EmailEtud'],
        pwd=etud_dict['MotPasseEtud'],
        nom=etud_dict['NomEtud'],
        prenom=etud_dict['PrenomEtud'],
        parc=etud_dict['NumParc']
    )


def dict_to_etudiantPlus(etud_dict):
    from .parcours import dict_to_parcours

    return EtudiantPlus(
        mat=etud_dict['MatEtud'],
        email=etud_dict['EmailEtud'],
        pwd=etud_dict['MotPasseEtud'],
        nom=etud_dict['NomEtud'],
        prenom=etud_dict['PrenomEtud'],
        parc=dict_to_parcours(etud_dict['ParcoursEtudiant'])
    )


# Search an Etudiant by E-mail
def search_etudiant_by_email(email):
    url = f"{BACKEND_BASE_URL}search/etudiant/byemail/{email}"

    try:
        response = requests.get(url)
        # Si le backend repond favorablement
        if response.status_code == 200:
            return dict_to_etudiant(response.json())

        # Si resource Not found
        else:
            return Error(response.json())

    except requests.exceptions.RequestException as e:
        message = "Une erreur s'est produite ! Veillez verifier que le serveur backend fonctionne"
        print(f"{message}\n{e}")

        return Error(message)


# Search Etudiant by matricule
def search_etudiant_by_matricule(matricule):
    url = f"{BACKEND_BASE_URL}etudiant/{matricule}"
    try:
        response = requests.get(url)
        # Si le backend repond favorablement
        if response.status_code == 200:
            return dict_to_etudiant(response.json())

        # Si resource Not found
        else:
            return Error(response.json())

    except requests.exceptions.RequestException as e:
        message = "Une erreur s'est produite ! Veillez verifier que le serveur backend fonctionne"
        print(f"{message}\n{e}")

        return Error(message)


# Enrol Etudiant
def enrol_etudiant(etud_dict):
    url = f"{BACKEND_BASE_URL}etudiant/{etud_dict['MatEtud']}"

    try:
        response = requests.put(url, json=etud_dict)
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
def is_valid_email(email):
    '''To prevent duplicated email as login'''
    response = search_etudiant_by_email(email)
    return not isinstance(response, Etudiant)
