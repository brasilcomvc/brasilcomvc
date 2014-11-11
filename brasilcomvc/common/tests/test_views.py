from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.test import RequestFactory, TestCase
from django.views.generic import View

from ..views import AnonymousRequiredMixin, LoginRequiredMixin


User = get_user_model()


class RequiresLogin(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        return HttpResponse('OK')


class RequiresAnonymous(AnonymousRequiredMixin, View):

    def get(self, *args, **kwargs):
        return HttpResponse('OK')


class LoginRequiredMixinTestCase(TestCase):

    def test_anonymous_user_should_be_redirected_to_login_url(self):
        view = RequiresLogin.as_view()
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'], '{}?next=/'.format(settings.LOGIN_URL))

    def test_authenticated_user_should_access_protected_view(self):
        view = RequiresLogin.as_view()
        request = RequestFactory().get('/')
        request.user = User()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'OK')


class AnonymousRequiredMixinTestCase(TestCase):

    def test_anonymous_user_should_access_protected_view(self):
        view = RequiresAnonymous.as_view()
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'OK')

    def test_authenticated_user_should_be_redirected_to_login_redirect_url(
            self):
        view = RequiresAnonymous.as_view()
        request = RequestFactory().get('/')
        request.user = User()
        response = view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], settings.LOGIN_REDIRECT_URL)
