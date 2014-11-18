from datetime import datetime

from django.core import mail
from django.test import TestCase

from ..email import send_template_email


class EmailTestMixin(object):
    '''
    Ease email testing by checking Django's outbox against a subject text.
    '''

    def only_email_sent(self, subject):
        self.assertEqual(len(mail.outbox), 1)
        self.emails_sent(subject)

    def emails_sent(self, *subjects):
        self.assertTrue(
            set([email.subject for email in mail.outbox]) >=
            set(subjects))


class TemplateEmailTestCase(EmailTestMixin, TestCase):

    def test_email_should_be_sent(self):
        send_template_email('test', 'user@localhost', 'test_email.html')
        self.only_email_sent('test')
        self.assertEqual(mail.outbox[0].to[0], 'user@localhost')

    def test_email_should_render_plain_text_correctly(self):
        timestamp = str(datetime.now())
        send_template_email(
            'test', 'user@localhost', 'test_email.html', {'value': timestamp})
        email = mail.outbox[-1]
        self.assertNotIn('<span', email.body)
        self.assertIn(timestamp, email.body)

    def test_email_should_render_html_correctly(self):
        timestamp = str(datetime.now())
        send_template_email(
            'test', 'user@localhost', 'test_email.html', {'value': timestamp})
        email = mail.outbox[-1]
        self.assertEqual(len(email.alternatives), 1)
        html, mimetype = email.alternatives[0]
        self.assertIn('<span data-test>{}</span>'.format(timestamp), html)
