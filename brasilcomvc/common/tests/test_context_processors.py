from django.template import RequestContext
from django.test import TestCase
from django.test.client import RequestFactory

from ..context_processors import social_auth_facebook_key


class SocialAuthFacebookKeyTest(TestCase):

    def test_context_processor(self):

        with self.settings(SOCIAL_AUTH_FACEBOOK_KEY='le-key'):
            context = social_auth_facebook_key(None)
            self.assertIn('SOCIAL_AUTH_FACEBOOK_KEY', context)
            self.assertEqual(context['SOCIAL_AUTH_FACEBOOK_KEY'], 'le-key')


class ServicesAPIKeysTestCase(TestCase):

    factory = RequestFactory()

    def test_api_keys(self):
        with self.settings(GOOGLE_API_KEY='lol'):
            context = RequestContext(self.factory.get('/'))
            self.assertEqual(context.get('google_api_key'), 'lol')
