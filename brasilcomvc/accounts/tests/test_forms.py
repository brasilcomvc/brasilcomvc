from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailField
from django.test import TestCase

from cities_light.models import City, Region

from ..forms import LoginForm, UserAddressForm


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
