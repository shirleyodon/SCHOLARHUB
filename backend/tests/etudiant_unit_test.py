from flask_testing import TestCase
from . import app


class EtudiantUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_etudiant(self):
        response = self.client.get("/sh/etudiant/2064/")

        target = {
            "EmailEtud": "tafitashirleyodon@gmail.com",
            "MatEtud": "2064",
            "MotPasseEtud": "shirley",
            "NomEtud": "TAFITA",
            "NumParc": 2,
            "PrenomEtud": "Shirley Odon"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)

    def test_search_by_email(self):
        response = self.client.get(
            "/sh/search/etudiant/byemail/tafitashirleyodon@gmail.com/")

        target = {
            "EmailEtud": "tafitashirleyodon@gmail.com",
            "MatEtud": "2064",
            "MotPasseEtud": "shirley",
            "NomEtud": "TAFITA",
            "NumParc": 2,
            "PrenomEtud": "Shirley Odon"
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
