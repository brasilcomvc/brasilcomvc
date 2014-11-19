from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailField
from django.test import TestCase

from ..forms import DeleteUserForm, LoginForm


User = get_user_model()


class DeleteUserFormTestCase(TestCase):

    def test_clean_password_with_valid_password(self):
        u = User(email='wat@wat.net')
        u.set_password('test')
        u.save()

        f = DeleteUserForm(user=u, data={'password': 'test'})
        self.assertTrue(f.is_valid())
        self.assertEqual(f.errors, {})

    def test_clean_password_with_invalid_password(self):
        u = User(email='wat@wat.net')
        u.set_password('hardtoguess')
        u.save()

        f = DeleteUserForm(user=u, data={'password': 'guess'})
        self.assertFalse(f.is_valid())
        self.assertIn('password', f.errors)
        self.assertEqual(f.errors['password'], ['Senha inválida'])


class LoginFormTestCase(TestCase):

    def test_username_authenticationform_subclass(self):
        self.assertTrue(issubclass(LoginForm, AuthenticationForm))

    def test_username_field_is_emailfield_instance(self):
        f = LoginForm()
        self.assertTrue(isinstance(f.fields['username'], EmailField))
