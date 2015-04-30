import os
import unittest

from flask import current_app
from app import create_app, db


class EntryModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_database(self):
        """
        Ensure that the database file exists
        """

        tester = os.path.exists('data-test.sqlite')
        self.assertTrue(tester)
