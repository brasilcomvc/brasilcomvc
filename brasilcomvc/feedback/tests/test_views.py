from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Feedback


class CreateViewTestCase(TestCase):

    url = reverse('feedback:create')

    def _setup_session(self):
        # Setup the test client session
        # Based on snippets from: https://code.djangoproject.com/ticket/10899
        self.client.cookies[settings.SESSION_COOKIE_NAME] = 'fake'
        session = self.client.session
        session['deleted_email'] = 'test@domain.net'
        session.save()
        self.client.cookies[settings.SESSION_COOKIE_NAME] = session.session_key

    def test_template_used(self):
        self._setup_session()

        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'feedback/create.html')

    def test_feedback_creation(self):
        self._setup_session()

        data = {
            'question_1': 'on',
            'question_2': 'on',
            'question_3': '',
            'question_4': 'on',
            'question_5': '',
            'comments': 'A nice comment',
        }

        next_url = reverse('feedback:create')
        resp = self.client.post('{}?next={}'.format(self.url, next_url), data)
        self.assertRedirects(resp, next_url)

        self.assertEqual(Feedback.objects.count(), 1)
        feedback = Feedback.objects.get()
        self.assertEqual(feedback.email, 'test@domain.net')
        self.assertTrue(feedback.question_1)
        self.assertTrue(feedback.question_2)
        self.assertFalse(feedback.question_3)
        self.assertTrue(feedback.question_4)
        self.assertFalse(feedback.question_5)
        self.assertEqual(feedback.comments, 'A nice comment')
        self.assertNotIn('deleted_email', self.client.session,
                         'Session wasn\'t properly cleaned')
