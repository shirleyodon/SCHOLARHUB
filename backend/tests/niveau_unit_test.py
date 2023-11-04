from flask_testing import TestCase
from . import app


class NiveauUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_niveau(self):
        response = self.client.get("/sh/niveauetude/1/")

        target = {
            "IdNiv": 1,
            "LibelleNiv": "L1"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
