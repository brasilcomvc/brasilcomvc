from django.template import RequestContext
from django.test import TestCase, override_settings
from django.test.client import RequestFactory


class ServicesAPIKeysTestCase(TestCase):

    factory = RequestFactory()

    @override_settings(
        FACEBOOK_API_KEY='fb-key',
        GOOGLE_API_KEY='g-key')
    def test_api_keys(self):
        context = RequestContext(self.factory.get('/'))
        self.assertEqual(context.get('FACEBOOK_API_KEY'), 'fb-key')
        self.assertEqual(context.get('GOOGLE_API_KEY'), 'g-key')
