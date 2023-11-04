from ..models import EncadreurPedagogique


# Object EncadreurPedagogique to dictionnary
def encadreur_to_dict_1(encad):
    return {
        'MatEncad': encad.matEncad,
        'EmailEncad': encad.emailEncad,
        'MotPasseEncad': encad.motPasseEncad,
        'NomEncad': encad.nomEncad,
        'PrenomEncad': encad.prenomEncad,
        'CodeTitre': encad.codeTitre,
    }


def encadreur_to_dict_2(encad):
    from .livre import livre_to_dict_1
    from .titre import titre_to_dict_1

    return {
        'MatEncad': encad.matEncad,
        'EmailEncad': encad.emailEncad,
        'MotPasseEncad': encad.motPasseEncad,
        'NomEncad': encad.nomEncad,
        'PrenomEncad': encad.prenomEncad,
        'TitreEncadreur': titre_to_dict_1(encad.titreEncadreur),
        'Livres': [livre_to_dict_1(livre) for livre in encad.livres]
    }


# Get all EncadreurPedagogique
def get_all_encadreur():
    return EncadreurPedagogique.query.all()


# Get an EncadreurPedagogique
def get_encadreur(matEncad):
    from .. import db
    return db.session.get(EncadreurPedagogique, matEncad)
    # return EncadreurPedagogique.query.get(matEncad)


# Create EncadreurPedagogique with Json data
def create_encadreur(json_data):
    return EncadreurPedagogique(
        json_data.get('MatEncad'),
        json_data.get('EmailEncad') if json_data.get('EmailEncad') else None,
        json_data.get('MotPasseEncad') if json_data.get(
            'MotPasseEncad') else None,
        json_data.get('NomEncad'),
        json_data.get('PrenomEncad'),
        json_data.get('CodeTitre')
    )


# Update EncadreurPedagogique with Json data
def update_encadreur(encad, json_data):
    encad.matEncad = json_data.get('MatEncad')
    encad.emailEncad = json_data.get(
        'EmailEncad') if json_data.get('EmailEncad') else None
    encad.motPasseEncad = json_data.get(
        'MotPasseEncad') if json_data.get('MotPasseEncad') else None
    encad.nomEncad = json_data.get('NomEncad')
    encad.prenomEncad = json_data.get('PrenomEncad')
    encad.codeTitre = json_data.get('CodeTitre')


# Search Encadreur by Nom et/ou Prenom
def search_encadreur_by_names(nom, prenom=None):
    if prenom:
        return EncadreurPedagogique.query.filter(
            EncadreurPedagogique.nomEncad.ilike(f'{nom}'),
            EncadreurPedagogique.prenomEncad.ilike(f'{prenom}')
        ).first()
    else:
        return EncadreurPedagogique.query.filter(
            EncadreurPedagogique.nomEncad.ilike(f'{nom}')
        ).first()
