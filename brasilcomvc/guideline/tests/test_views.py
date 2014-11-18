from django.core.urlresolvers import reverse
from django.test import TestCase


class UIGuidelineViewTest(TestCase):

    def test_ui_guideline_template_used(self):
        resp = self.client.get(reverse('guideline:ui'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'guideline/ui.html')

    def test_ui_guideline_context(self):
        resp = self.client.get(reverse('guideline:ui'))
        self.assertEqual(resp.status_code, 200)

        self.assertIn('empty_form', resp.context)
        self.assertEqual(resp.context['empty_form'].data, {})

        self.assertIn('invalid_form', resp.context)
        self.assertFalse(resp.context['invalid_form'].is_valid())
