from datetime import datetime

from django.core import mail
from django.test import TestCase

from ..email import send_template_email


class TemplateEmailTestCase(TestCase):

    def test_email_should_be_sent(self):
        send_template_email('test', 'user@localhost', 'test_email.html')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'test')
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
