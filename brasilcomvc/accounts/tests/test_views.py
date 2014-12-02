from django.contrib.auth import get_user_model
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from brasilcomvc.common.views import AnonymousRequiredMixin, LoginRequiredMixin
from cities_light.models import City

from ..models import UserAddress
from ..views import (
    DeleteUser,
    EditDashboard,
    EditNotifications,
    EditPersonalInfo,
    EditProfessionalInfo,
    EditSecuritySettings,
    EditUserAddress,
    Profile,
    Signup,
)


User = get_user_model()


class SignupTestCase(TestCase):

    url = reverse('signup')

    def test_signup_page_is_accessible(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_inherits_anonymous_required_mixin(self):
        self.assertTrue(issubclass(Signup, AnonymousRequiredMixin))

    def test_signup_success(self):
        data = {
            'email': 'user@example.com',
            'full_name': 'Test User',
            'password': '123',
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, self.url)
        self.assertTrue(User.objects.filter(email=data['email']).exists())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Bem vindo!')

    def test_signup_failure(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.exists())
        self.assertEqual(
            set(response.context['form'].errors),
            set(['email', 'full_name', 'password']))


class ProfileTestCase(TestCase):

    url = reverse('profile')

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(Profile, LoginRequiredMixin))

    def test_template_used(self):
        data = {'email': 'user@example.com', 'password': '123'}
        User.objects.create_user(**data)
        self.client.login(username=data['email'], password=data['password'])
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, 'accounts/profile.html')


class LoginTestCase(TestCase):

    url = reverse('login')

    def test_template_used(self):
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, 'accounts/login.html')

    def test_login_success(self):
        data = {'email': 'user@example.com', 'password': '123'}
        User.objects.create_user(**data)
        response = self.client.post(self.url, data={
            'username': data['email'],
            'password': data['password'],
        })
        self.assertRedirects(response, reverse('profile'))

    def test_logged_user_should_be_redirected_to_profile(self):
        data = {'email': 'user@example.com', 'password': '123'}
        User.objects.create_user(**data)
        self.assertTrue(self.client.login(
            username=data['email'], password=data['password']))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))


class LogoutTestCase(TestCase):

    def test_logout_redirect_to_login(self):
        resp = self.client.get(reverse('logout'))
        self.assertRedirects(resp, reverse('login'))


class EditDashboardTestCase(TestCase):

    url = reverse('edit_dashboard')

    def setUp(self):
        data = {'email': 'user@example.com', 'password': '123'}
        User.objects.create_user(**data)
        self.client.login(
            username=data['email'], password=data['password'])

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(EditDashboard, LoginRequiredMixin))

    def test_template_used(self):
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, 'accounts/edit_dashboard.html')

    def test_page_should_not_display_None(self):
        resp = self.client.get(self.url)
        self.assertNotContains(resp, 'None')


class EditPersonalInfoTestCase(TestCase):

    url = reverse('edit_personal_info')

    def setUp(self):
        data = {'email': 'user@example.com', 'password': '123'}
        user = User.objects.create_user(**data)
        self.client.login(username=data['email'], password=data['password'])
        self.user_id = user.pk

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(EditPersonalInfo, LoginRequiredMixin))

    def test_form_should_have_right_fields_only(self):
        self.assertEqual(
            EditPersonalInfo.fields, ('full_name', 'username', 'email',))

    def test_correct_form_submit_should_update_data(self):
        data = {
            'full_name': 'Test User',
            'email': 'new@example.com',
            'username': 'new_username',
        }
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, reverse('edit_dashboard'))
        user = User.objects.get(pk=self.user_id)
        for key, value in data.items():
            self.assertEqual(getattr(user, key), value)


class EditProfessionalInfoTestCase(TestCase):

    url = reverse('edit_professional_info')

    def setUp(self):
        data = {'email': 'user@example.com', 'password': '123'}
        user = User.objects.create_user(**data)
        self.client.login(username=data['email'], password=data['password'])
        self.user_id = user.pk

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(EditProfessionalInfo, LoginRequiredMixin))

    def test_form_should_have_right_fields_only(self):
        self.assertEqual(
            EditProfessionalInfo.fields, ('job_title', 'bio',))

    def test_correct_form_submit_should_update_data(self):
        data = {
            'job_title': 'Python Programmer',
            'bio': 'I am an unusual person who does not like to write bios',
        }
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, reverse('edit_dashboard'))
        user = User.objects.get(pk=self.user_id)
        for key, value in data.items():
            self.assertEqual(getattr(user, key), value)


class EditNotificationsTestCase(TestCase):

    url = reverse('edit_notifications')

    def setUp(self):
        data = {'email': 'user@example.com', 'password': '123'}
        user = User.objects.create_user(**data)
        self.client.login(username=data['email'], password=data['password'])
        self.user_id = user.pk

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(EditNotifications, LoginRequiredMixin))

    def test_form_should_have_right_fields_only(self):
        self.assertEqual(
            EditNotifications.form_class.Meta.fields, ('email_newsletter',))

    def test_correct_form_submit_should_update_data(self):
        data = {
            'email_newsletter': True,
        }
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, reverse('edit_dashboard'))
        user = User.objects.get(pk=self.user_id)
        for key, value in data.items():
            self.assertEqual(getattr(user, key), value)


class EditSecuritySettingsTestCase(TestCase):

    url = reverse('edit_security_settings')

    def setUp(self):
        data = {'email': 'user@example.com', 'password': '123'}
        user = User.objects.create_user(**data)
        self.client.login(username=data['email'], password=data['password'])
        self.user_id = user.pk

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(EditSecuritySettings, LoginRequiredMixin))

    def test_correct_form_submit_should_update_data(self):
        data = {
            'old_password': '123',
            'new_password1': 'newpwd',
            'new_password2': 'newpwd',
        }
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, reverse('edit_dashboard'))
        user = User.objects.get(pk=self.user_id)
        self.assertTrue(user.check_password(data['new_password1']))


class EditUserAddressTestCase(TestCase):

    url = reverse('edit_user_address')
    fixtures = ('test_cities',)

    def setUp(self):
        data = {'email': 'user@example.com', 'password': '123'}
        user = User.objects.create_user(**data)
        self.client.login(username=data['email'], password=data['password'])
        self.user_id = user.pk

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(EditUserAddress, LoginRequiredMixin))

    def test_correct_form_submit_should_create_object_when_not_existent(self):
        self.assertFalse(UserAddress.objects.exists())
        city = City.objects.order_by('?')[0]
        data = {
            'zipcode': '00000-000',
            'address_line1': 'Rua Sem Fim, 0',
            'address_line2': 'Apto -1',
            'state': city.region.id,
            'city': city.id,
        }
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, reverse('edit_dashboard'))
        address = UserAddress.objects.get(user_id=self.user_id)
        self.assertEqual(address.address_line1, data['address_line1'])
        self.assertEqual(address.address_line2, data['address_line2'])
        self.assertEqual(address.city_id, data['city'])
        self.assertEqual(address.state_id, data['state'])
        self.assertEqual(address.zipcode, data['zipcode'])

    def test_correct_form_submit_should_update_object_when_existent(self):
        city = City.objects.order_by('?')[0]
        address = UserAddress.objects.create(
            user_id=self.user_id,
            zipcode='22222-222',
            address_line1='Avenida Redonda, 3.14',
            address_line2='Apto -5',
            state=city.region,
            city=city)
        data = {
            'address_line1': address.address_line1,
            'address_line2': address.address_line2,
            'state': address.state_id,
            'city': address.city_id,
            'zipcode': '33333-333',
        }
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, reverse('edit_dashboard'))
        address = UserAddress.objects.get(id=address.id)
        self.assertEqual(address.zipcode, data['zipcode'])


class DeleteUserTest(TestCase):

    url = reverse('delete_user')

    def _setup_user(self):
        data = {'email': 'user@example.com', 'password': '123'}
        self.user = User.objects.create_user(**data)
        self.client.login(username=data['email'], password=data['password'])

    def test_delete_user_view_login_required_mixin(self):
        self.assertTrue(issubclass(DeleteUser, LoginRequiredMixin))

    def test_delete_user_view_template(self):
        self._setup_user()

        resp = self.client.get(reverse('delete_user'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounts/delete-user.html')

    def test_delete_user_view_should_delete_user_on_post(self):
        self._setup_user()

        logged_session = self.client.cookies['sessionid'].value

        resp = self.client.post(self.url, {'password': '123'})
        self.assertEqual(resp.status_code, 302)

        self.assertFalse(User.objects.filter(email=self.user.email).exists())
        self.assertNotEqual(
            logged_session,
            self.client.cookies['sessionid'].value,
            'Same sesion found, probably user wasnt logged out')
        self.assertIn('deleted_email', self.client.session)
        self.assertEqual(self.client.session['deleted_email'], self.user.email)

    def test_delete_user_view_should_fail_on_invalid_password(self):
        '''
        Test the delete user view response when received an invalid password
        The invalid password logic is tested directly on the form
        '''
        self._setup_user()
        resp = self.client.post(self.url, {'password': 'invalid'})
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.context['form'].is_valid())
