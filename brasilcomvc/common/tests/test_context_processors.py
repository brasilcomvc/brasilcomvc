from django.template import RequestContext
from django.test import SimpleTestCase, override_settings
from django.test.client import RequestFactory

from ..context_processors import blog_url


class ServicesAPIKeysTestCase(SimpleTestCase):

    factory = RequestFactory()

    @override_settings(
        FACEBOOK_API_KEY='fb-key',
        GOOGLE_ANALYTICS_ID='ga-key',
        GOOGLE_API_KEY='g-key')
    def test_api_keys(self):
        context = RequestContext(self.factory.get('/'))
        self.assertEqual(context.get('FACEBOOK_API_KEY'), 'fb-key')
        self.assertEqual(context.get('GOOGLE_ANALYTICS_ID'), 'ga-key')
        self.assertEqual(context.get('GOOGLE_API_KEY'), 'g-key')


class BlogURLTestCase(SimpleTestCase):

    def test_unit(self):
        with self.settings(BLOG_URL='http://blog'):
            ctx = blog_url(None)
        self.assertIn('BLOG_URL', ctx)
        self.assertEquals(ctx['BLOG_URL'], 'http://blog')

    def test_integration(self):
        with self.settings(BLOG_URL='http://blog'):
            ctx = RequestContext(RequestFactory().get('/'))
        self.assertIn('BLOG_URL', ctx)
        self.assertEquals(ctx['BLOG_URL'], 'http://blog')


class ContactInfoTestCase(SimpleTestCase):

    def test_unit(self):
        with self.settings(CONTACT_EMAIL='contato@brasil.com.vc', CONTACT_PHONE='551100000000'):
            ctx = blog_url(None)
        self.assertIn('CONTACT_EMAIL', ctx)
        self.assertEquals(ctx['CONTACT_EMAIL'], 'contato@brasil.com.vc')
        self.assertIn('CONTACT_PHONE', ctx)
        self.assertEquals(ctx['CONTACT_PHONE'], '551100000000')

    def test_integration(self):
        with self.settings(CONTACT_EMAIL='contato@brasil.com.vc', CONTACT_PHONE='551100000000'):
            ctx = RequestContext(RequestFactory().get('/'))
        self.assertIn('CONTACT_EMAIL', ctx)
        self.assertEquals(ctx['CONTACT_EMAIL'], 'contato@brasil.com.vc')
        self.assertIn('CONTACT_PHONE', ctx)
        self.assertEquals(ctx['CONTACT_PHONE'], '551100000000')
