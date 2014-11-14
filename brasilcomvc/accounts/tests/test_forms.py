from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailField
from django.test import TestCase

from ..forms import LoginForm


class LoginFormTestCase(TestCase):

    def test_username_authenticationform_subclass(self):
        self.assertTrue(issubclass(LoginForm, AuthenticationForm))

    def test_username_field_is_emailfield_instance(self):
        f = LoginForm()
        self.assertTrue(isinstance(f.fields['username'], EmailField))
