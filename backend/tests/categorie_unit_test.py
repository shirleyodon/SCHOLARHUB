from flask_testing import TestCase
from . import app


class CategorieUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_categorie(self):
        response = self.client.get("/sh/categorielivre/1/")

        target = {
            "LibelleCat": "Rapport de projet",
            "NumCat": 1
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
