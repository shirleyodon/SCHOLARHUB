from flask_testing import TestCase
from . import app


class TitreUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_titre(self):
        response = self.client.get("/sh/titreencadreur/1/")

        target = {
            "CodeTitre": 1,
            "LibelleTitre": "Doctorant en informatique"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
