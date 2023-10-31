class EtablissementAccueil():
    def __init__(self, id, adr, contact, nom, sigle, site):
        self.idEtab = id
        self.adresse = adr
        self.contact = contact
        self.nomEtab = nom
        self.sigle = sigle
        self.siteWeb = site

    def to_dict(self):
        return {
            'IdEtab': self.idEtab,
            'Adresse': self.adresse,
            'Contact': self.contact,
            'NomEtab': self.nomEtab,
            'Sigle': self.sigle,
            'SiteWeb': self.siteWeb
        }
