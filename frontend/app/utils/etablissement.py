from ..models import EtablissementAccueil


# Dictionnary to EtablissementAcceuil
def dict_to_etablissement(etab_dict):
    return EtablissementAccueil(
        id=etab_dict['IdEtab'],
        adr=etab_dict['Adresse'],
        contact=etab_dict['Contact'],
        nom=etab_dict['NomEtab'],
        sigle=etab_dict['Sigle'],
        site=etab_dict['SiteWeb']
    )
