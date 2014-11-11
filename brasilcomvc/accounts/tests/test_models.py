from django.test import TestCase

from ..models import User


class UserTestCase(TestCase):

    def test_short_name_with_long_name(self):
        user = User(full_name='Homer J. Simpson')
        self.assertEqual(user.get_short_name(), 'Homer')

    def test_short_name_with_single_name(self):
        user = User(full_name='Beavis')
        self.assertEqual(user.get_short_name(), 'Beavis')
