from flask_testing import TestCase
from . import app


class LivreUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_livre(self):
        response = self.client.get("/sh/livre/1/")

        target = {
            "AnneeUniversitaire": {
                "CodeAnnee": 1,
                "LibelleAnnee": "2018-2019"
            },
            "CategorieLivre": {
                "LibelleCat": "Rapport de projet",
                "NumCat": 1
            },
            "EncadreurPedagogique": {
                "CodeTitre": 2,
                "EmailEncad": "siakamail1@gmail.com",
                "MatEncad": "ENC004",
                "MotPasseEncad": "siaka",
                "NomEncad": "SIAKA",
                "PrenomEncad": "-"
            },
            "EtablissementAcceuil": {
                "Adresse": "Tanambao Fianarantsoa",
                "Contact": "+261340573336",
                "IdEtab": 1,
                "NomEtab": "Ecole Nationale d'Informatique",
                "Sigle": "ENI",
                "SiteWeb": None
            },
            "Etudiants": [
                {
                    "EmailEtud": "tafitashirleyodon@gmail.com",
                    "MatEtud": "2064",
                    "MotPasseEtud": "shirley",
                    "NomEtud": "TAFITA",
                    "ParcoursEtudiant": {
                        "LibelleParc": "Administrateur système et réseau",
                        "NumParc": 2
                    },
                    "PrenomEtud": "Shirley Odon"
                },
                {
                    "EmailEtud": None,
                    "MatEtud": "2027",
                    "MotPasseEtud": None,
                    "NomEtud": "RAMIHONOSON",
                    "ParcoursEtudiant": {
                        "LibelleParc": "Administrateur système et réseau",
                        "NumParc": 2
                    },
                    "PrenomEtud": "Aimé Francisco"
                },
                {
                    "EmailEtud": None,
                    "MatEtud": "2024",
                    "MotPasseEtud": None,
                    "NomEtud": "TOMBOZAVELO",
                    "ParcoursEtudiant": {
                        "LibelleParc": "Administrateur système et réseau",
                        "NumParc": 2
                    },
                    "PrenomEtud": "Jenny Phillipine"
                }
            ],
            "MotCle": "Arduino, automatisation, carrefour, feu tricolore, prototypage, simulation",
            "NbPage": 50,
            "NiveauEtude": {
                "IdNiv": 1,
                "LibelleNiv": "L1"
            },
            "RefLivre": 1,
            "Resume": "Occaecat do duis magna mollit amet voluptate dolore veniam pariatur. Exercitation sint veniam mollit ullamco mollit eiusmod mollit cupidatat eu enim cupidatat. Velit ipsum ex consequat reprehenderit duis. Velit irure nulla minim sunt. Et aliqua est et aliqua nisi consequat irure deserunt. Laborum minim esse pariatur cupidatat proident ex aute anim do aliqua dolor occaecat fugiat deserunt. Consectetur est proident aliquip id labore consectetur ea tempor aliqua velit id ullamco.",
            "Theme": "Création d'un prototype de simulation de feu tricolores sur un carrefour avec Arduino",
            "Url": "www.livre1.com"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
