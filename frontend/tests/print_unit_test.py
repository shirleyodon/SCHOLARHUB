from flask_testing import TestCase
from . import app


class PrintUnitTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_print(self):
        response = self.client.get('/sh/print/')

        self.assert200(
            response, {"Erreur": "Impossible de joindre la resource 'print'"})
        self.assertTemplateUsed(name='print.html')
