from ..models import NiveauEtude


# Object NiveauEtude to dictionnary
def niveau_to_dict_1(niv):
    return {
        'IdNiv': niv.idNiv,
        'LibelleNiv': niv.libelleNiv,
    }


def niveau_to_dict_2(niv):
    from .etudiant import etudiant_to_dict_1
    from .livre import livre_to_dict_1

    return {
        'IdNiv': niv.idNiv,
        'LibelleNiv': niv.libelleNiv,
        'Livres': [livre_to_dict_1(livre) for livre in niv.livres],
        'Etudiants': [etudiant_to_dict_1(etud) for etud in niv.etudiants]
    }


# Get all NiveauEtude
def get_all_niveau():
    return NiveauEtude.query.all()


# Get a NiveauEtude
def get_niveau(idNiv):
    return NiveauEtude.query.get(idNiv)


# Create NiveauEtude object with Json data
def create_niveau(json_data):
    return NiveauEtude(json_data.get('LibelleNiv'))


# Update NiveauEtude object with Json data
def update_niveau(niv, json_data):
    niv.libelleNiv = json_data.get('LibelleNiv')


# Search NiveauEtude by libelleNiv
def search_niveau_by_libelle(libelle):
    return NiveauEtude.query.filter(NiveauEtude.libelleNiv.ilike(f'{libelle}')).first()
