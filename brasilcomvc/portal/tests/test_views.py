from django.core.urlresolvers import reverse
from django.http import Http404
from django.test import RequestFactory, TestCase

from ..views import blog_redirect


class BlogRedirectTestCase(TestCase):

    def test_blog_redirect_with_empty_setting(self):
        req = RequestFactory().get('/blog')
        with self.assertRaises(Http404):
            with self.settings(BLOG_URL=''):
                resp = blog_redirect(req)

    def test_blog_redirect_with_valid_setting(self):
        req = RequestFactory().get('/blog')
        with self.settings(BLOG_URL='http://blog'):
            resp = blog_redirect(req)
        self.assertEquals(resp.status_code, 301)
        self.assertEquals(resp['Location'], 'http://blog')

    def test_integration(self):
        with self.settings(BLOG_URL='http://blog'):
            resp = self.client.get(reverse('portal:blog_redirect'))
        self.assertEquals(resp.status_code, 301)
        self.assertEquals(resp['Location'], 'http://blog')

