from flask_testing import TestCase
from . import app


class AnneeUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_annee(self):
        response = self.client.get("/sh/anneeuniversitaire/1/")

        target = {
            "CodeAnnee": 1,
            "LibelleAnnee": "2018-2019"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
