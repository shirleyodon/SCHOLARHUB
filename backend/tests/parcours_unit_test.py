from flask_testing import TestCase
from . import app


class ParcoursUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_parcours(self):
        response = self.client.get("/sh/parcoursetude/1/")

        target = {
            "LibelleParc": "Génie logiciel et base de données",
            "NumParc": 1
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
