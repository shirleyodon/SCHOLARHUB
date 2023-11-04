from flask_testing import TestCase
from . import app


class EncadreurUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_encadreur(self):
        response = self.client.get("/sh/encadreurpedagogique/ENC001/")

        target = {
            "CodeTitre": 5,
            "EmailEncad": "fontainerafamant@yahoo.fr",
            "MatEncad": "ENC001",
            "MotPasseEncad": "fontaine",
            "NomEncad": "RAFAMANTANANTSOA",
            "PrenomEncad": "Fontaine"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
