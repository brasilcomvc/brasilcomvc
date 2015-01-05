from django.template import RequestContext
from django.test import TestCase
from django.test.client import RequestFactory


class ServicesAPIKeysTestCase(TestCase):

    factory = RequestFactory()

    def test_api_keys(self):
        with self.settings(GOOGLE_API_KEY='lol'):
            context = RequestContext(self.factory.get('/'))
            self.assertEqual(context.get('google_api_key'), 'lol')
