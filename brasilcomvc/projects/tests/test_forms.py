from django.test import TestCase

from ..forms import ProjectSearchForm


class ProjectSearchFormTest(TestCase):

    def test_required(self):
        f = ProjectSearchForm({})
        self.assertFalse(f.is_valid())
        self.assertIn('q', f.errors)
        self.assertIn('lat', f.errors)
        self.assertIn('lng', f.errors)
        self.assertNotIn('radius', f.errors)

    def test_valid(self):
        f = ProjectSearchForm({
            'q': 'some place',
            'lat': '1.0',
            'lng': '1.0',
        })
        self.assertTrue(f.is_valid())

    def test_clean_radius_return_default_when_omitted(self):
        f = ProjectSearchForm({
            'q': 'some place',
            'lat': '1.0',
            'lng': '1.0',
        })
        self.assertTrue(f.is_valid())
        self.assertEquals(f.cleaned_data['radius'], 30)

    def test_clean_radius_return_received_value(self):
        f = ProjectSearchForm({
            'q': 'some place',
            'lat': '1.0',
            'lng': '1.0',
            'radius': 1000,
        })
        self.assertTrue(f.is_valid())
        self.assertEquals(f.cleaned_data['radius'], 1000)
