from ..models import EtablissementAccueil

# Object EtablissementAccueil to dictionnary
def etablissement_to_dict_1(etab):
    return {
        'IdEtab': etab.idEtab,
        'Adresse': etab.adresse,
        'Contact': etab.contact,
        'NomEtab': etab.nomEtab,
        'Sigle': etab.sigle,
        'SiteWeb': etab.siteWeb
    }

def etablissement_to_dict_2(etab):
    from .livre import livre_to_dict_1
    
    return {
        'IdEtab': etab.idEtab,
        'Adresse': etab.adresse,
        'Contact': etab.contact,
        'NomEtab': etab.nomEtab,
        'Sigle': etab.sigle,
        'SiteWeb': etab.siteWeb,
        'Livres': [livre_to_dict_1(livre) for livre in etab.livres]
    }

# Get all EtablissementAccueil
def get_all_etablissement():
    return EtablissementAccueil.query.all()

# Get an EtablissementAccueil
def get_etablissement(idEtab):
    return EtablissementAccueil.query.get(idEtab)

# Create EtablissementAccueil with Json data
def create_etablissement(json_data):
    return EtablissementAccueil(
        json_data.get('Adresse'),
        json_data.get('Contact'),
        json_data.get('NomEtab'),
        json_data.get('Sigle') if json_data.get('Sigle') else None,
        json_data.get('SiteWeb') if json_data.get('SiteWeb') else None
    )

# Update EtablissementAccueil with Json data
def update_etablissement(etab, json_data):
    etab.adresse = json_data.get('Adresse')
    etab.contact = json_data.get('Contact')
    etab.nomEtab = json_data.get('NomEtab')
    etab.sigle = json_data.get('Sigle') if json_data.get('Sigle') else None
    etab.siteWeb = json_data.get('SiteWeb') if json_data.get('SiteWeb') else None