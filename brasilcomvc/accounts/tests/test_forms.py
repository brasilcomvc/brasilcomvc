# encoding: utf8
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailField
from django.test import TestCase

from cities_light.models import City, Region

from ..forms import DeleteUserForm, LoginForm, UserAddressForm


User = get_user_model()


class LoginFormTestCase(TestCase):

    def test_username_authenticationform_subclass(self):
        self.assertTrue(issubclass(LoginForm, AuthenticationForm))

    def test_username_field_is_emailfield_instance(self):
        f = LoginForm()
        self.assertTrue(isinstance(f.fields['username'], EmailField))


class UserAddressFormTestCase(TestCase):

    fixtures = ['test_cities']

    def test_form_should_have_all_fields(self):
        self.assertEqual(UserAddressForm.Meta.fields, '__all__')

    def test_form_state_field_should_have_used_regions_only(self):
        region = Region.objects.order_by('?')[0]
        City.objects.filter(region=region).delete()
        self.assertEqual(
            set(UserAddressForm().fields['state'].queryset),
            set(Region.objects.exclude(id=region.id)))

    def test_form_group_cities(self):
        expected_choices = [
            (region.name, list(
                region.city_set.order_by('name').values_list('pk', 'name')),)
            for region in Region.objects.order_by('name')
        ]
        self.assertEqual(UserAddressForm()._group_cities(), expected_choices)


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
