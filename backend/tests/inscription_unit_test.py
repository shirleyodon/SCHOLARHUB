from flask_testing import TestCase
from . import app


class InscriptionUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_inscription(self):
        response = self.client.get("/sh/inscription/2064/1/1/")

        target = {
            "CodeAnnee": 1,
            "IdNiv": 1,
            "MatEtud": "2064"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
