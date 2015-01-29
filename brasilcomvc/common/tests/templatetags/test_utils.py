from django.test import TestCase
from django.utils.safestring import SafeData

from ...templatetags.utils import (
    to_markdown,
)


class MarkdownFilterTestCase(TestCase):

    def test_markdown_filter_should_integrate_with_render_tool(self):
        # This is not intended to test Markdown rendering, but instead to check
        # if the 3rd-party tool is correctly integrated and used.
        result = to_markdown('Sample text').strip()
        self.assertEqual(result, '<p>Sample text</p>')

    def test_markdown_filter_should_return_safe_string(self):
        result = to_markdown('Sample text')
        self.assertIsInstance(result, SafeData)
