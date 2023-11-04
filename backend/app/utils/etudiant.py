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


def etudiant_to_dict_3(etud):
    from .parcours import parcours_to_dict_1

    return {
        'MatEtud': etud.matEtud,
        'EmailEtud': etud.emailEtud,
        'MotPasseEtud': etud.motPasseEtud,
        'NomEtud': etud.nomEtud,
        'PrenomEtud': etud.prenomEtud,
        'ParcoursEtudiant': parcours_to_dict_1(etud.parcoursEtude)
    }


# Get all Etudiant
def get_all_etudiant():
    return Etudiant.query.all()


# Get an Etudiant
def get_etudiant(matEtud):
    from .. import db
    return db.session.get(Etudiant, matEtud)
    # return Etudiant.query.get(matEtud)


# Search an Etudiant by E-mail
def search_etudiant_by_email(email):
    return Etudiant.query.filter_by(emailEtud=email).first()


# Create Etudiant with Json data
def create_etudiant(json_data):
    return Etudiant(
        json_data.get('MatEtud'),
        json_data.get('EmailEtud') if json_data.get('EmailEtud') else None,
        json_data.get('MotPasseEtud') if json_data.get(
            'MotPasseEtud') else None,
        json_data.get('NomEtud'),
        json_data.get('PrenomEtud'),
        json_data.get('NumParc')
    )


# Update Etudiant with Json data
def update_etudiant(etud, json_data):
    etud.matEtud = json_data.get('MatEtud')
    etud.emailEtud = json_data.get(
        'EmailEtud') if json_data.get('EmailEtud') else None
    etud.motPasseEtud = json_data.get(
        'MotPasseEtud') if json_data.get('MotPasseEtud') else None
    etud.nomEtud = json_data.get('NomEtud')
    etud.prenomEtud = json_data.get('PrenomEtud')
    etud.numParc = json_data.get('NumParc')


# Search Etudiant by Parcours
def search_etudiant_by_parcours(libelleParc):
    from .parcours import search_parcours_by_libelle
    return Etudiant.query.filter_by(parcoursEtude=search_parcours_by_libelle(libelleParc)).all()


# Search Etudiant by names
def search_etudiant_by_names(nom, prenom=None):
    if prenom:
        return Etudiant.query.filter(
            Etudiant.nomEtud.ilike(f'{nom}'),
            Etudiant.prenomEtud.ilike(f'{prenom}')
        ).first()
    else:
        return Etudiant.query.filter(
            Etudiant.nomEtud.ilike(f'{nom}')
        ).first()
