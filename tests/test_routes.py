import unittest

from flask import current_app
from app import create_app, db


class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.tester = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        """
        Homepage loads correctly
        """

        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_no_entry(self):
        """
        No entry right after DB initialization
        """

        response = self.tester.get('/')
        self.assertIn(b'No entries here so far', response.data)

    def test_add_entry(self):
        """
        Ensure that entry can be added
        """

        response = self.tester.post('/', data=dict(
            title='Hello',
            text='HTML Everybody',
        ))
        print response.status_code
        self.assertNotIn(b'No entries here so far', response.data)
        self.assertIn(b'Hello', response.data)
