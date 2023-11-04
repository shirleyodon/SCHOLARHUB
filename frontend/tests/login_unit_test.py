from flask_testing import TestCase
from . import app


class LoginUnitTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_login(self):
        response = self.client.get('/sh/login/')

        self.assert200(
            response, {"Erreur": "Impossible de joindre la resource 'login'"})
        self.assertTemplateUsed(name='login.html')
