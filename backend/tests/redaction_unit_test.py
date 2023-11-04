from flask_testing import TestCase
from . import app


class RedactionUniteTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_redaction(self):
        response = self.client.get("/sh/redaction/1/2064/")

        target = {
            "MatEtud": "2064",
            "RefLivre": 1
        }

        self.assert200(response, response.json)
        self.assertEqual(response.json, target)
