from flask_testing import TestCase
from . import app


class RegisterUnitTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_register(self):
        response = self.client.get('/sh/register/')

        self.assert200(
            response, {"Erreur": "Impossible de joindre la resource 'register'"})
        self.assertTemplateUsed(name='register.html')
