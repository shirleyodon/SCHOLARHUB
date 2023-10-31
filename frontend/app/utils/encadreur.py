from ..models import EncadreurPedagogique


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
