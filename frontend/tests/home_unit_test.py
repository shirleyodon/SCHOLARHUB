from flask_testing import TestCase
from . import app


class HomeUnitTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home(self):
        response = self.client.get('/sh/home/')

        self.assert200(
            response, {"Erreur": "Impossible de joindre la resource 'home'"})
        self.assertTemplateUsed(name='home.html')
