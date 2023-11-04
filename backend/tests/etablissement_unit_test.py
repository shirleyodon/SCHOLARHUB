from flask_testing import TestCase
from . import app


class EtablissementUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_etablissement(self):
        response = self.client.get("/sh/etablissementacceuil/1/")

        target = {
            "Adresse": "Tanambao Fianarantsoa",
            "Contact": "+261340573336",
            "IdEtab": 1,
            "NomEtab": "Ecole Nationale d'Informatique",
            "Sigle": "ENI",
            "SiteWeb": None
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
