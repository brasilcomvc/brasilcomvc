from django.contrib.auth import get_user_model
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from brasilcomvc.common.views import AnonymousRequiredMixin, LoginRequiredMixin

from ..views import DeleteUser, Signup


User = get_user_model()


class SignupTestCase(TestCase):

    url = reverse('signup')

    def test_signup_page_is_accessible(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_signup_view_inherits_anonymous_required_mixin(self):
        self.assertTrue(issubclass(Signup, AnonymousRequiredMixin))

    def test_signup_success(self):
        user_data = {
            'email': 'user@example.com',
            'full_name': 'Test User',
            'password': '123',
        }
        response = self.client.post(self.url, user_data)
        self.assertRedirects(response, self.url)
        self.assertTrue(User.objects.filter(email=user_data['email']).exists())
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

    def test_anonymous_is_redirect_to_login(self):
        resp = self.client.get(self.url)
        self.assertRedirects(
            resp, '{}?next={}'.format(reverse('login'), self.url))

    def test_template_used(self):
        u = User(email='test@test.net')
        u.set_password('test')
        u.save()

        self.assertTrue(self.client.login(username=u.email, password='test'))

        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, 'accounts/profile.html')


class LoginTestCase(TestCase):

    url = reverse('login')

    def test_template_used(self):
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, 'accounts/login.html')

    def test_login_success(self):
        u = User(email='user@domain.xxx')
        u.set_password('passwd')
        u.save()

        response = self.client.post(self.url, data={
            'username': 'user@domain.xxx',
            'password': 'passwd',
        })
        self.assertRedirects(response, reverse('profile'))

    def test_logged_user_should_be_redirected_to_profile(self):
        u = User(email='wat@domain.net')
        u.set_password('test')
        u.save()

        self.assertTrue(self.client.login(username=u.email, password='test'))

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
        user = User.objects.create_user('wat@example.com', password='test')
        self.client.login(username=user.email, password='test')

    def test_anonymous_is_redirect_to_login(self):
        self.client.logout()
        resp = self.client.get(self.url)
        self.assertRedirects(
            resp, '{}?next={}'.format(reverse('login'), self.url))

    def test_template_used(self):
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, 'accounts/edit_dashboard.html')

    def test_page_should_not_display_None(self):
        resp = self.client.get(self.url)
        self.assertNotContains(resp, 'None')


class EditPersonalInfoTestCase(TestCase):

    url = reverse('edit_personal_info')

    def setUp(self):
        user = User.objects.create_user('wat@example.com', password='test')
        self.user_id = user.pk
        self.client.login(username=user.email, password='test')

    def test_anonymous_is_redirected_to_login(self):
        self.client.logout()
        resp = self.client.get(self.url)
        self.assertRedirects(
            resp, '{}?next={}'.format(reverse('login'), self.url))

    def test_form_should_have_right_fields_only(self):
        resp = self.client.get(self.url)
        self.assertEqual(
            set(resp.context['form'].fields),
            set(['full_name', 'username', 'email']))

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
        user = User.objects.create_user('wat@example.com', password='test')
        self.user_id = user.pk
        self.client.login(username=user.email, password='test')

    def test_anonymous_is_redirected_to_login(self):
        self.client.logout()
        resp = self.client.get(self.url)
        self.assertRedirects(
            resp, '{}?next={}'.format(reverse('login'), self.url))

    def test_form_should_have_right_fields_only(self):
        resp = self.client.get(self.url)
        self.assertEqual(
            set(resp.context['form'].fields), set(['job_title', 'bio']))

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
        user = User.objects.create_user('wat@example.com', password='test')
        self.user_id = user.pk
        self.client.login(username=user.email, password='test')

    def test_anonymous_is_redirected_to_login(self):
        self.client.logout()
        resp = self.client.get(self.url)
        self.assertRedirects(
            resp, '{}?next={}'.format(reverse('login'), self.url))

    def test_form_should_have_right_fields_only(self):
        resp = self.client.get(self.url)
        self.assertEqual(
            set(resp.context['form'].fields), set(['email_newsletter']))

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
        user = User.objects.create_user('wat@example.com', password='test')
        self.user_id = user.pk
        self.client.login(username=user.email, password='test')

    def test_anonymous_is_redirected_to_login(self):
        self.client.logout()
        resp = self.client.get(self.url)
        self.assertRedirects(
            resp, '{}?next={}'.format(reverse('login'), self.url))

    def test_form_should_have_right_fields_only(self):
        resp = self.client.get(self.url)
        self.assertEqual(
            set(resp.context['form'].fields),
            set(['old_password', 'new_password1', 'new_password2']))

    def test_correct_form_submit_should_update_data(self):
        data = {
            'old_password': 'test',
            'new_password1': 'newpwd',
            'new_password2': 'newpwd',
        }
        resp = self.client.post(self.url, data)
        self.assertRedirects(resp, reverse('edit_dashboard'))
        user = User.objects.get(pk=self.user_id)
        self.assertTrue(user.check_password(data['new_password1']))


class DeleteUserTest(TestCase):

    def _setup_user(self):
        self.user = User(email='test@dom.ain')
        self.user.set_password('test')
        self.user.save()
        self.assertTrue(self.client.login(username=self.user.email,
                                          password='test'))

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

        data = {
            'password': 'test'
        }
        resp = self.client.post(reverse('delete_user'), data=data)
        self.assertEqual(resp.status_code, 302)

        self.assertFalse(User.objects.filter(email=self.user.email).exists())
        self.assertNotEqual(logged_session,
                            self.client.cookies['sessionid'].value,
                            'Same sesion found, probably user wasnt logged out')

    def test_delete_user_view_should_fail_on_invalid_password(self):
        """Test the delete user view response when received an invalid password
        The invalid password logic is tested directly on the form
        """
        self._setup_user()

        data = {
            'password': 'invalid'
        }
        resp = self.client.post(reverse('delete_user'), data=data)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.context['form'].is_valid())
