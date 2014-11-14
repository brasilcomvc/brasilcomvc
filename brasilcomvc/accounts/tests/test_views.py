from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from brasilcomvc.common.views import AnonymousRequiredMixin

from ..views import Signup


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
        self.assertRedirects(resp, '{}?next={}'.format(reverse('login'), self.url))

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
