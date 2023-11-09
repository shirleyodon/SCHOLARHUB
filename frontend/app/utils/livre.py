import requests
from ..config import Config
from ..models import Livre, LivrePlus

BACKEND_BASE_URL = Config.BACKEND_BASE_URL

# Dictionnary to Livre
def dict_to_livre(livre_dict):
    return Livre(
        ref=livre_dict['RefLivre'],
        clef=livre_dict['MotCle'],
        page=livre_dict['NbPage'],
        resume=livre_dict['Resume'],
        theme=livre_dict['Theme'],
        url=livre_dict['Url'],
        annee=livre_dict['CodeAnnee'],
        etab=livre_dict['IdEtab'],
        niv=livre_dict['IdNiv'],
        encad=livre_dict['MatEncad'],
        cat=livre_dict['NumCat']
    )


# Dictionnary to LivrePlus
def dict_to_livrePlus(livre_dict):
    from .annee import dict_to_annee
    from .categorie import dict_to_categorie
    from .encadreur import dict_to_encadreur
    from .etablissement import dict_to_etablissement
    from .etudiant import dict_to_etudiantPlus
    from .niveau import dict_to_niveau

    return LivrePlus(
        ref=livre_dict['RefLivre'],
        clef=livre_dict['MotCle'],
        page=livre_dict['NbPage'],
        resume=livre_dict['Resume'],
        theme=livre_dict['Theme'],
        url=livre_dict['Url'],

        annee=dict_to_annee(livre_dict['AnneeUniversitaire']),
        etab=dict_to_etablissement(livre_dict['EtablissementAcceuil']),
        niv=dict_to_niveau(livre_dict['NiveauEtude']),
        encad=dict_to_encadreur(livre_dict['EncadreurPedagogique']),
        cat=dict_to_categorie(livre_dict['CategorieLivre']),
        etudiants=[dict_to_etudiantPlus(item)
                   for item in livre_dict['Etudiants']]
    )


# Search Livre by multiple criterion
def search_livre_by_theme_categorie_parcours_niveau(theme, cat, parc, niv):
    from ..models import Information, Error

    url = f"{BACKEND_BASE_URL}search/livre?theme={theme}"
    if cat:
        url += f"&cat={cat}"
    if parc:
        url += f"&parc={parc}"
    if niv:
        url += f"&niv={niv}"

    try:
        response = requests.get(url)

        # Si le backend repond favorablement
        if response.status_code == 200:
            # If no book found
            if not response.json():
                return Information("Aucun livre n'a été trouvé")
            else:
                return [dict_to_livrePlus(livre) for livre in response.json()]

    except requests.exceptions.RequestException as e:
        message = "Une erreur s'est produite ! Veillez verifier que le serveur backend fonctionne"
        print(f"{message}\n{e}")

        return Error(message)


# Get a Livre by Reference
def get_livre(refLivre):
    from ..models import Error

    url = f"{BACKEND_BASE_URL}livre/{refLivre}"
    try:
        response = requests.get(url)

        # Si le backend repond favorablement
        if response.status_code == 200:
            return dict_to_livrePlus(response.json())
        else:
            return Error(requests.json())

    except requests.exceptions.RequestException as e:
        message = "Une erreur s'est produite ! Veillez verifier que le serveur backend fonctionne"
        print(f"{message}\n{e}")

        return Error(message)
