from ..models import Livre

# Object Livre to dictionnary


def livre_to_dict_1(livre):
    return {
        'RefLivre': livre.refLivre,
        'MotCle': livre.motCle,
        'NbPage': livre.nbPage,
        'Resume': livre.resume,
        'Theme': livre.theme,
        'Url': livre.url,
        'CodeAnnee': livre.codeAnnee,
        'IdEtab': livre.idEtab,
        'IdNiv': livre.idNiv,
        'MatEncad': livre.matEncad,
        'NumCat': livre.numCat
    }


def livre_to_dict_2(livre):
    # To avoid circular import
    from .annee import annee_to_dict_1
    from .categorie import categorie_to_dict_1
    from .encadreur import encadreur_to_dict_1
    from .etablissement import etablissement_to_dict_1
    from .etudiant import etudiant_to_dict_3
    from .niveau import niveau_to_dict_1

    return {
        'RefLivre': livre.refLivre,
        'MotCle': livre.motCle,
        'NbPage': livre.nbPage,
        'Resume': livre.resume,
        'Theme': livre.theme,
        'Url': livre.url,

        'AnneeUniversitaire': annee_to_dict_1(livre.anneeUniversitaire),
        'EtablissementAcceuil': etablissement_to_dict_1(livre.etablissementAccueil),
        'NiveauEtude': niveau_to_dict_1(livre.niveauEtude),
        'EncadreurPedagogique': encadreur_to_dict_1(livre.encadreurPedagogique),
        'CategorieLivre': categorie_to_dict_1(livre.categorieLivre),
        'Etudiants': [etudiant_to_dict_3(etud) for etud in livre.etudiants]
    }

# Get all Livre


def get_all_livre():
    return Livre.query.all()

# Get a Livre


def get_livre(refLivre):
    return Livre.query.get(refLivre)

# Create a Livre from Json data


def create_livre(json_data):
    return Livre(
        json_data.get('MotCle'),
        json_data.get('NbPage'),
        json_data.get('Resume'),
        json_data.get('Theme'),
        json_data.get('Url'),
        json_data.get('CodeAnnee'),
        json_data.get('IdEtab'),
        json_data.get('IdNiv'),
        json_data.get('MatEncad'),
        json_data.get('NumCat')
    )

# Update a Livre object with Json data


def update_livre(livre, json_data):
    livre.motCle = json_data.get('MotCle')
    livre.nbPage = json_data.get('NbPage')
    livre.resume = json_data.get('Resume')
    livre.theme = json_data.get('Theme')
    livre.url = json_data.get('Url')
    livre.codeAnnee = json_data.get('CodeAnnee')
    livre.idEtab = json_data.get('IdEtab')
    livre.idNiv = json_data.get('IdNiv')
    livre.matEncad = json_data.get('MatEncad')
    livre.numCat = json_data.get('NumCat')


# Search a Livre by Theme
def search_livre_by_theme(theme):
    return Livre.query.filter(Livre.theme.ilike(f'%{theme}%'))


# Search a Livre by Categorie
def search_livre_by_categorie(libelleCat):
    from .categorie import search_categorie_by_libelle
    return Livre.query.filter_by(categorieLivre=search_categorie_by_libelle(libelleCat))


# Search a Livre by Parcours
def search_livre_by_parcours(libelleParc):
    from ..models import Etudiant
    from .etudiant import search_etudiant_by_parcours
    matricules = [
        etudiant.matEtud for etudiant in search_etudiant_by_parcours(libelleParc)]

    return Livre.query.filter(Livre.etudiants.any(Etudiant.matEtud.in_(matricules))).all()


# Search a Livre by Niveau
def search_livre_by_niveau(libelleNiv):
    from .niveau import search_niveau_by_libelle
    return Livre.query.filter_by(niveauEtude=search_niveau_by_libelle(libelleNiv))


# Search a Livre by Theme - Categorie - Parcours - Niveau
def search_livre_by_theme_categorie_parcours_niveau(theme, cat, parc, niv):
    livres_by_theme = search_livre_by_theme(theme)

    # Si listes_by_theme non vide
    if livres_by_theme:
        livres = livres_by_theme

        # Si Categorie fait partie des criteres de recherche
        if cat:
            livres_by_cat = search_livre_by_categorie(cat)

            # Si livres_by_cat non vide
            if livres_by_cat:
                livres = list(set(livres) & set(livres_by_cat))
            else:
                return []

        # Si Parcours fait partie des criteres de recherche
        if parc:
            livres_by_parc = search_livre_by_parcours(parc)

            # Si livres_by_parc non vide
            if livres_by_parc:
                livres = list(set(livres) & set(livres_by_parc))
            else:
                return []

        # Si Niveau fait partie des criteres de recherche
        if niv:
            livres_by_niv = search_livre_by_niveau(niv)

            # Si livres_by_niv non vide
            if livres_by_niv:
                livres = list(set(livres) & set(livres_by_niv))
            else:
                return []

        return list(livres)

    else:
        return []
