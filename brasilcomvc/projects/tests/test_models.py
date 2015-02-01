# coding: utf8
from __future__ import unicode_literals
import json
import re

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from pygeocoder import Geocoder, GeocoderError
import responses

from ..models import Project, project_img_upload_to


User = get_user_model()


class ProjectTestCase(TestCase):

    def _mock_pygeocoder_request(self, plain_json):
        responses.add(
            responses.GET,
            re.compile(Geocoder.GEOCODE_QUERY_URL),
            body=json.dumps(plain_json),
            content_type='application/json',
            status=200)

    def test_project_slug_gets_generated_correctly(self):
        project = Project(
            owner=User.objects.create_user('test@example.com', '123'),
            name='This is a Test Project')
        project.save()
        self.assertEqual(project.slug, 'this-is-a-test-project')
        old_slug = project.slug
        project.name = 'Some New Name'
        project.save()
        self.assertEqual(project.slug, old_slug)

    def test_project_img_upload_to(self):
        project = Project(slug='wat-is-a-slug')
        filename = 'wat.png'
        expected = 'projects/wat-is-a-slug/img.jpeg'
        self.assertEqual(project_img_upload_to(project, filename), expected)

    @responses.activate
    def test_auto_geocode_should_fail_with_invalid_address(self):
        project = Project(address='Th1s iz such an 1nv4l1d @ddress')
        self._mock_pygeocoder_request({
            'results': [],
            'status': GeocoderError.G_GEO_ZERO_RESULTS})
        self.assertRaises(ValidationError, project.clean)
        self.assertIsNone(project.latlng)

    @responses.activate
    def test_auto_geocode_should_work_with_valid_address(self):
        self._mock_pygeocoder_request({
            'results': [
                {'geometry': {'location': {'lat': -23.5528, 'lng': -46.6307}}},
            ],
            'status': GeocoderError.G_GEO_OK})
        project = Project(address='Sé, São Paulo, Brasil')
        project.clean()
        self.assertIsNotNone(project.latlng)
        self.assertEqual(project.latlng.y, -23.5528)  # latitude
        self.assertEqual(project.latlng.x, -46.6307)  # longitude
