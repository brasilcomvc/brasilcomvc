from django.test import TestCase

from ..models import User, user_picture_upload_to


class UserManagerTestCase(TestCase):

    _user_data = {
        'email': 'test@example.com',
        'password': '123',
        'full_name': 'Test User',
    }

    def test_create_user(self):
        data = self._user_data.copy()
        self.assertFalse(User.objects.exists())
        User.objects.create_user(**data)
        raw_pwd = data.pop('password')
        self.assertTrue(User.objects.filter(**data).exists())
        user = User.objects.all()[0]
        self.assertTrue(user.check_password(raw_pwd))

    def test_create_superuser(self):
        User.objects.create_superuser(**self._user_data)
        user = User.objects.all()[0]
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class UserTestCase(TestCase):

    def test_short_name_with_long_name(self):
        user = User(full_name='Homer J. Simpson')
        self.assertEqual(user.get_short_name(), 'Homer')

    def test_short_name_with_single_name(self):
        user = User(full_name='Beavis')
        self.assertEqual(user.get_short_name(), 'Beavis')

    def test_short_name_with_no_name(self):
        user = User(full_name='')
        self.assertEqual(user.get_short_name(), '')

    def test_user_picture_upload_to(self):
        user = User(email='user@example.com')
        filename = 'wat.png'
        expected = 'users/u/user@example.com.jpg'
        self.assertEqual(user_picture_upload_to(user, filename), expected)
