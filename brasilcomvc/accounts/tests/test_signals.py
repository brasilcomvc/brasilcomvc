from django.test import TestCase

from cities_light import InvalidItems

from ..signals import filter_city_import


class FilterCityImportTestCase(TestCase):

    def test_filter_city_import_should_raise_invalid_items_when_not_br(self):
        items = [None, None, None, None, None, None, None, None, 'NOBR']
        self.assertRaises(InvalidItems, filter_city_import, None, items)

    def test_filter_city_import_should_succeed_when_br(self):
        items = [None, None, None, None, None, None, None, None, 'BR']
        self.assertIsNone(filter_city_import(None, items))
