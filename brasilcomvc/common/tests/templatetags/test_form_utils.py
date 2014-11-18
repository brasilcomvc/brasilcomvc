from django import forms
from django.test import TestCase

from ...templatetags.form_utils import (
    form_field,
    form_fieldset,
)


class TestForm(forms.Form):
    test_field = forms.CharField(max_length=40)


class FormFieldTestCase(TestCase):

    def test_generate_an_id_from_a_form_with_prefix(self):
        form = TestForm(prefix='foo')
        self.assertEqual(
            form_field(form['test_field'])['form_id'], form.prefix)

    def test_generate_an_id_from_a_form_without_prefix(self):
        form = TestForm()
        self.assertEqual(form_field(form['test_field'])['form_id'], 'testform')

    def test_render_html_classes_correctly_for_required_field(self):
        form = TestForm()
        form.fields['test_field'].required = True
        self.assertEqual(
            form_field(form['test_field'])['classes'], ('required',))

    def test_render_html_classes_correctly_for_empty_required_field(self):
        form = TestForm(data={})
        form.fields['test_field'].required = True
        self.assertEqual(
            set(form_field(form['test_field'])['classes']),
            set(['required', 'error']))

    def test_render_html_classes_correctly_for_non_required_field(self):
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
