from django import forms
from django.test import TestCase

from ...templatetags.form_utils import (
    form_field,
    form_fieldset,
)


class TestForm(forms.Form):
    test_field = forms.CharField(max_length=40)


class FormFieldTestCase(TestCase):

    def test_generate_an_id_from_the_form(self):
        # When form has a prefix, use it
        form = TestForm(prefix='foo')
        self.assertEqual(
            form_field(form['test_field'])['form_id'], form.prefix)

        # When form has no prefix, use its class name
        form = TestForm()
        self.assertEqual(form_field(form['test_field'])['form_id'], 'testform')

    def test_render_html_classes_correctly(self):
        # 1: Required field, empty form
        form = TestForm()
        form.fields['test_field'].required = True
        self.assertEqual(
            form_field(form['test_field'])['classes'], ('required',))

        # 2: Required field, empty input
        form = TestForm(data={})
        form.fields['test_field'].required = True
        self.assertEqual(
            set(form_field(form['test_field'])['classes']),
            set(['required', 'error']))

        # 3: Non required field
        form = TestForm()
        form.fields['test_field'].required = False
        self.assertEqual(
            form_field(form['test_field'])['classes'], ())


class FormFieldsetTestCase(TestCase):

    def test_generate_list_of_bound_fields_correctly(self):
        form = TestForm()
        self.assertEqual(
            [bound_field.field for bound_field in
                form_fieldset(form, fields='test_field')['fields']],
            [form.fields['test_field']])

    def test_raise_error_when_undefined_field(self):
        form = TestForm()
        self.assertRaises(
            KeyError,
            lambda: form_fieldset(form, fields='test_field undefined')),
