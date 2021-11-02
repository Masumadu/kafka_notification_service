from flask_testing import TestCase
from app import create_app, db
from .test_responses import SharedResponse


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app("config.TestingConfig")
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.create_all()
        self.shared_responses = SharedResponse()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()