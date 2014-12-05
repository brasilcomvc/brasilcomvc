from django.test import TestCase
import mock

from ..models import User
from ..pipelines import set_user_info_from_auth_provider


class SetUserInfoFromAuthProviderTestCase(TestCase):

    def test_should_return_none_if_user_not_found(self):
        self.assertIsNone(set_user_info_from_auth_provider(None, None, None))

    def test_should_register_full_name_and_email_on_user_instance(self):
        backend = mock.Mock()
        details = {
            'email': 'cool@mailinator.com',
            'fullname': 'My Name Yo',
        }
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.full_name, '')

        set_user_info_from_auth_provider(backend, user, details)

        self.assertEqual(user.email, details['email'])
        self.assertEqual(user.full_name, details['fullname'])
        backend.strategy.storage.user.changed.assert_called_once_with(user)
