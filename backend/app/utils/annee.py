from ..models import AnneeUniversitaire


# Object AnneeUniversitaire to dictionnary
def annee_to_dict_1(annee):
    return {
        'CodeAnnee': annee.codeAnnee,
        'LibelleAnnee': annee.libelleAnnee,
    }


def annee_to_dict_2(annee):
    from .livre import livre_to_dict_1

    return {
        'CodeAnnee': annee.codeAnnee,
        'LibelleAnnee': annee.libelleAnnee,
        'Livres': [livre_to_dict_1(livre) for livre in annee.livres]
    }


# Get all AnneeUniversitaire
def get_all_annee():
    return AnneeUniversitaire.query.all()


# Get an AnneeUniversitaire
def get_annee(codeAnnee):
    from .. import db
    return db.session.get(AnneeUniversitaire, codeAnnee)
    # return AnneeUniversitaire.query.get(codeAnnee)


# Create AnneeUniversitaire object with Json data
def create_annee(json_data):
    return AnneeUniversitaire(json_data.get('LibelleAnnee'))


# Update AnneeUniversitaire object with Json data
def update_annee(annee, json_data):
    annee.libelleAnnee = json_data.get('LibelleAnnee')
